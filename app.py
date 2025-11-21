import streamlit as st
import requests

# Fetch menu from backend
menu_response = requests.get("http://localhost:8000/menu")
menu = menu_response.json() 



# Optional: Show raw menu data for debugging
# st.write(menu)

# Extract unique filter options, skipping items missing fields
MEALS = sorted(list(set(item.get("meal", "Unknown") for item in menu if "meal" in item)))
CATS = sorted(list(set(item.get("cat", "Unknown") for item in menu if "cat" in item)))
VEG_FILTERS = {"All": None, "Veg only": True, "Non-Veg only": False}

MENU = [item for item in menu if all(field in item for field in ["meal", "cat", "veg", "price", "name", "available"])]

# ------------------------
# Streamlit Page Settings
# ------------------------
st.set_page_config(
    page_title="Hotel Room Service Assistant",
    page_icon="🍽️",
    layout="centered"
)

# ------------------------
# Custom CSS for Modern UI
# ------------------------
st.markdown("""
<style>
.chat-container {
    max-width: 700px;
    margin: auto;
    padding: 20px;
}
.user-msg {
    background: #DCF8C6;
    color: #000;
    padding: 12px 18px;
    border-radius: 15px;
    margin-bottom: 10px;
    align-self: flex-end;
    max-width: 80%;
}
.bot-msg {
    background: #F1F0F0;
    color: #000;
    padding: 12px 18px;
    border-radius: 15px;
    margin-bottom: 10px;
    align-self: flex-start;
    max-width: 80%;
}
.cart-item {
    margin-bottom: 8px;
}
.menu-section {
    margin-bottom: 14px;
    padding: 6px;
}
</style>
""", unsafe_allow_html=True)

st.title("🍽️ Hotel Room Service Chatbot")
st.write("Select your meal and filter by category in the menu on the left, then build your order. Use the chat for special requests.")

# ------------------------
# Session State
# ------------------------
if "order_cart" not in st.session_state:
    st.session_state.order_cart = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "room_number" not in st.session_state:
    st.session_state.room_number = ""

# ------------------------
# Sidebar: Menu Filtering & Selection
# ------------------------
st.sidebar.title("🧾 Menu Selection")
meal_selected = st.sidebar.selectbox("Meal", options=MEALS)
cat_selected = st.sidebar.selectbox("Category", options=["All"] + CATS)
veg_pref = st.sidebar.radio("Veg/Non-Veg", options=list(VEG_FILTERS.keys()))

filtered_menu = [
    item for item in MENU
    if item.get("meal") == meal_selected
    and (cat_selected == "All" or item.get("cat") == cat_selected)
    and (VEG_FILTERS[veg_pref] is None or item.get("veg") == VEG_FILTERS[veg_pref])
]

st.sidebar.markdown("#### Available Items")
item_names = [f"{i['name']} (₹{i['price']})" for i in filtered_menu]

selected_item = st.sidebar.selectbox("Choose an item", options=([""] + item_names) if item_names else [""])
if selected_item:
    idx = item_names.index(selected_item)
    menu_entry = filtered_menu[idx]
    qty = st.sidebar.number_input("Quantity", min_value=1, max_value=10, value=1)
    if st.sidebar.button("Add to Cart"):
        st.session_state.order_cart.append({
            "item": menu_entry["name"],
            "qty": qty,
            "meal": menu_entry["meal"],
            "veg": menu_entry["veg"],
            "cat": menu_entry["cat"],
            "price": menu_entry["price"]
        })
        st.sidebar.success(f"Added {qty} × {menu_entry['name']}")

# ------------------------
# ADD ROOM NUMBER INPUT (only change requested)
# ------------------------
st.sidebar.markdown("### 🏨 Enter Room Number")
st.session_state.room_number = st.sidebar.text_input(
    "Room Number",
    value=st.session_state.room_number,
    placeholder="e.g., 101"
)

# ------------------------
# Sidebar: Cart
# ------------------------
st.sidebar.markdown("#### 🛒 Your Order Cart")
if st.session_state.order_cart:
    total = 0
    for e in st.session_state.order_cart:
        price = e["qty"] * e["price"]
        st.sidebar.markdown(
            f"<div class='cart-item'>{e['qty']} × <b>{e['item']}</b> (₹{price})</div>",
            unsafe_allow_html=True
        )
        total += price
    st.sidebar.markdown(f"**Total: ₹{total}**")

    if st.sidebar.button("Place Order"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/order",
                json={"order": st.session_state.order_cart, "room": st.session_state.room_number}
            )
            reply = response.json().get("response", "[Order error]")
        except Exception as ex:
            reply = f"⚠️ Error: {ex}"

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.session_state.order_cart = []
else:
    st.sidebar.info("No items added yet.")

# ------------------------
# Main Chat Panel
# ------------------------
user_input = st.chat_input("Any special instructions or questions?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Assistant typing..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/order",
                json={"message": user_input}
            )
            bot_reply = response.json().get("response", "[Error: No reply]")
        except Exception:
            bot_reply = "⚠️ Unable to reach backend server."
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)
# ------------------------
