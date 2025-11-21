from groq import Groq
import google.generativeai as genai
from dotenv import load_dotenv
import os
from database import menu_collection, history_collection
from utils.prompts import system_prompt

load_dotenv()

#client = Groq(api_key=os.getenv("GROQ_API_KEY"))

client = genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class RoomServiceAgent:
    def __init__(self):
        self.menu = self.load_menu()
        self.chat_history = []   

    def load_menu(self):
        return {item["name"].lower(): item for item in menu_collection.find()}

    def save_interaction(self, user_msg, agent_msg):
        history_collection.insert_one({"user": user_msg, "agent": agent_msg})

    def generate_response(self, user_message):
        """
        Uses conversation context so bot does NOT restart every time.
        """
        self.chat_history.append({"role": "user", "content": user_message})

        chat_input = [ {"role": "system", "content": system_prompt}
        ] + self.chat_history[-5:]  
        response = client.chat.completions.create(model="gemini-1.5-flash",messages=chat_input,max_tokens=200,temperature=0)
        bot_reply = response.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": bot_reply})
        return bot_reply

    def handle_order(self, order_list, room=None):
        """
        Handles structured cart order:
        [ { "item": "Pasta", "qty": 2 }, ... ]
        """
        order_text = "\n".join([f"{o['qty']} × {o['item']}" for o in order_list])
        room_text = f"Room Number: {room}" if room else "Room number not provided."

        user_message = f"""
        Cart Order Summary:
        {order_text}

        {room_text}

        Please confirm: YES to confirm, NO to modify.
        """

        reply = self.generate_response(user_message)
        self.save_interaction(user_message, reply)
        return reply
