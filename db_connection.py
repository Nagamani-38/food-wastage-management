import sqlite3

conn = sqlite3.connect("food_wastage.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS providers (
    provider_name TEXT,
    food_type TEXT,
    quantity INTEGER,
    location TEXT,
    contact TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS receivers (
    receiver_name TEXT,
    receiver_type TEXT,
    people_count INTEGER,
    location TEXT,
    contact TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS food_listings (
    food_name TEXT,
    food_type TEXT,
    meal_type TEXT,
    quantity INTEGER,
    expiry TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS claims (
    receiver_name TEXT,
    food_item TEXT,
    claim_quantity INTEGER,
    claim_status TEXT
)
""")

conn.commit()
conn.close()

print("Database connected successfully")