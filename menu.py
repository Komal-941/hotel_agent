from pymongo import MongoClient

# MongoDB Atlas connection details
MONGO_URL = "mongodb+srv://komal_shelar:pass1234@agenai.dqpekke.mongodb.net/AgenAI?retryWrites=true&w=majority&appName=AgenAI"
client = MongoClient(MONGO_URL)

db = client["Hotel"]              # Replace with your DB name if needed
menu_collection = db["Menu"]      # Your collection name

menu_items = [
    {"name": "Misal Pav",        "meal": "Breakfast", "cat": "Main Course", "veg": True,  "price": 80, "available": True},
    {"name": "Butter Sandwich",  "meal": "Breakfast", "cat": "Main Course", "veg": False, "price": 60, "available": True},
    {"name": "Poha",             "meal": "Breakfast", "cat": "Main Course", "veg": True,  "price": 50, "available": True},
    {"name": "Upma",             "meal": "Breakfast", "cat": "Main Course", "veg": True,  "price": 55, "available": True},
    {"name": "Idli Sambar",      "meal": "Breakfast", "cat": "Main Course", "veg": True,  "price": 70, "available": True},
    {"name": "Masala Dosa",      "meal": "Breakfast", "cat": "Main Course", "veg": True,  "price": 90, "available": True},
    {"name": "Veg Crispy",       "meal": "Lunch", "cat": "Starters", "veg": True,  "price": 110, "available": True},
    {"name": "Chicken Tandoori", "meal": "Lunch", "cat": "Starters", "veg": False, "price": 180, "available": True},
    {"name": "Chicken Kabab",    "meal": "Lunch", "cat": "Starters", "veg": False, "price": 150, "available": True},
    {"name": "Finger Chips",     "meal": "Lunch", "cat": "Starters", "veg": True,  "price": 80, "available": True},
    {"name": "Veg Manchow Soup", "meal": "Lunch", "cat": "Starters", "veg": True,  "price": 90, "available": True},
    {"name": "Chicken Soup",     "meal": "Lunch", "cat": "Starters", "veg": False, "price": 120, "available": True},
    {"name": "Butter Chicken",   "meal": "Lunch", "cat": "Main Course", "veg": False, "price": 210, "available": True},
    {"name": "Kaju Curry",       "meal": "Lunch", "cat": "Main Course", "veg": True,  "price": 190, "available": True},
    {"name": "Kaju Masala",      "meal": "Lunch", "cat": "Main Course", "veg": True,  "price": 200, "available": True},
    {"name": "Veg Mix",          "meal": "Lunch", "cat": "Main Course", "veg": True,  "price": 130, "available": True},
    {"name": "Paneer Makhani",   "meal": "Lunch", "cat": "Main Course", "veg": True,  "price": 170, "available": True},
    {"name": "Chicken Handi",    "meal": "Lunch", "cat": "Main Course", "veg": False, "price": 220, "available": True},
    {"name": "Mutton Handi",     "meal": "Lunch", "cat": "Main Course", "veg": False, "price": 260, "available": True},
    {"name": "Prawns Masala",    "meal": "Lunch", "cat": "Main Course", "veg": False, "price": 280, "available": True},
    {"name": "Mushroom Masala",  "meal": "Lunch", "cat": "Main Course", "veg": True,  "price": 160, "available": True},
    {"name": "Veg Biryani",      "meal": "Lunch", "cat": "Rice", "veg": True,   "price": 140, "available": True},
    {"name": "Chicken Biryani",  "meal": "Lunch", "cat": "Rice", "veg": False,  "price": 180, "available": True},
    {"name": "Mutton Biryani",   "meal": "Lunch", "cat": "Rice", "veg": False,  "price": 220, "available": True},
    {"name": "Steamed Rice",     "meal": "Lunch", "cat": "Rice", "veg": True,   "price": 90,  "available": True},
    {"name": "Jeera Rice",       "meal": "Lunch", "cat": "Rice", "veg": True,   "price": 110, "available": True},
    {"name": "Tandoori Roti",    "meal": "Lunch", "cat": "Bread",  "veg": True,  "price": 25, "available": True},
    {"name": "Butter Naan",      "meal": "Lunch", "cat": "Bread",  "veg": False, "price": 40, "available": True},
    {"name": "Chapati",          "meal": "Lunch", "cat": "Bread",  "veg": True,  "price": 20, "available": True},
    {"name": "Paneer Tikka",     "meal": "Dinner", "cat": "Starters", "veg": True,  "price": 140, "available": True},
    {"name": "Chicken Tikka",    "meal": "Dinner", "cat": "Starters", "veg": False, "price": 180, "available": True},
    {"name": "Hara Bhara Kabab", "meal": "Dinner", "cat": "Starters", "veg": True,  "price": 100, "available": True},
    {"name": "Paneer Butter Masala", "meal": "Dinner", "cat": "Main Course", "veg": True,  "price": 180, "available": True},
    {"name": "Chicken Curry",        "meal": "Dinner", "cat": "Main Course", "veg": False, "price": 210, "available": True},
    {"name": "Dal Tadka",            "meal": "Dinner", "cat": "Main Course", "veg": True,  "price": 120, "available": True},
    {"name": "Mix Veg Curry",        "meal": "Dinner", "cat": "Main Course", "veg": True,  "price": 130, "available": True},
    {"name": "Veg Pulao",        "meal": "Dinner", "cat": "Rice", "veg": True,  "price": 130, "available": True},
    {"name": "Chicken Biryani",  "meal": "Dinner", "cat": "Rice", "veg": False, "price": 190, "available": True},
    {"name": "Jeera Rice",       "meal": "Dinner", "cat": "Rice", "veg": True,  "price": 110, "available": True},
    {"name": "Butter Naan",      "meal": "Dinner", "cat": "Bread", "veg": False, "price": 40, "available": True},
    {"name": "Garlic Naan",      "meal": "Dinner", "cat": "Bread", "veg": False, "price": 45, "available": True},
    {"name": "Chapati",          "meal": "Dinner", "cat": "Bread", "veg": True,  "price": 20, "available": True},
    {"name": "Samosa",           "meal": "Snacks", "cat": "Snacks", "veg": True,  "price": 25, "available": True},
    {"name": "Vada Pav",         "meal": "Snacks", "cat": "Snacks", "veg": True,  "price": 20, "available": True},
    {"name": "Paneer Pakoda",    "meal": "Snacks", "cat": "Snacks", "veg": False, "price": 60, "available": True},
    {"name": "Chicken Nuggets",  "meal": "Snacks", "cat": "Snacks", "veg": False, "price": 90, "available": True},
    {"name": "Virgin Mojito",    "meal": "Drinks", "cat": "Mocktails", "veg": True,  "price": 80, "available": True},
    {"name": "Blue Lagoon",      "meal": "Drinks", "cat": "Mocktails", "veg": True,  "price": 85, "available": True},
    {"name": "Fruit Punch",      "meal": "Drinks", "cat": "Mocktails", "veg": True,  "price": 90, "available": True},
    {"name": "Masala Tea",       "meal": "Drinks", "cat": "Tea/Coffee", "veg": False, "price": 30, "available": True},
    {"name": "Black Tea",        "meal": "Drinks", "cat": "Tea/Coffee", "veg": True,  "price": 25, "available": True},
    {"name": "Filter Coffee",    "meal": "Drinks", "cat": "Tea/Coffee", "veg": False, "price": 35, "available": True},
    {"name": "Cold Coffee",      "meal": "Drinks", "cat": "Tea/Coffee", "veg": False, "price": 40, "available": True},
    {"name": "Gulab Jamun",      "meal": "Dessert", "cat": "Dessert", "veg": False, "price": 45, "available": True},
    {"name": "Ice Cream",        "meal": "Dessert", "cat": "Dessert", "veg": False, "price": 40, "available": True},
    {"name": "Brownie",          "meal": "Dessert", "cat": "Dessert", "veg": False, "price": 50, "available": True},
    {"name": "Rasgulla",         "meal": "Dessert", "cat": "Dessert", "veg": False, "price": 50, "available": True},]


count = 0
for item in menu_items:
    result = menu_collection.update_one(
        {"name": item["name"]},
        {"$set": item},
        upsert=True
    )
    count += 1

print(f"✅ Menu seeded successfully! Upserted {count} items.")
