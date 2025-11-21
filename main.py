from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from agent import RoomServiceAgent
from fastapi.responses import JSONResponse
from database import menu_collection

app = FastAPI()
agent = RoomServiceAgent()

# -----------------------------------------
# ONE MODEL that includes both use-cases
# -----------------------------------------
class OrderItem(BaseModel):
    item: str
    qty: int

class OrderPayload(BaseModel):
    message: Optional[str] = None
    order: Optional[List[OrderItem]] = None
    room: Optional[str] = None


@app.get("/")
def home():
    return {"status": "Room service agent is running."}


@app.get("/menu")
async def get_menu():
    return list(menu_collection.find({}, {"_id": 0}))


# ----------------------------------------------------
# UPDATED /order endpoint — nothing else changed
# ----------------------------------------------------
@app.post("/order")
async def order_endpoint(payload: OrderPayload):

    # 1️⃣ Chat Message
    if payload.message:
        reply = agent.generate_response(payload.message)
        agent.save_interaction(payload.message, reply)
        return {"response": reply}

    # 2️⃣ Cart Order
    if payload.order:
        reply = agent.handle_order(
            [item.dict() for item in payload.order],
            room=payload.room
        )
        return {"response": reply}

    return JSONResponse({"response": "[Error] Bad input"}, status_code=400)
