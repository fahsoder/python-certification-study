### Database Connection ###

# lets use mongodb
# use `pip install pymongo` to add pymongo lib 

from pymongo import MongoClient

# Connect to MongoDB Atlas
# Replace the placeholders with your actual connection details
client = MongoClient("<your_connection_string>")
db = client["mydatabase"]  # Replace "mydatabase" with your database name
collection = db["mycollection"]  # Replace "mycollection" with your collection name
