### Database Insertions ###

from connection import collection

# Insert a single document
document = {"name": "John Doe", "age": 25}
insert_result = collection.insert_one(document)
print("Inserted document ID:", insert_result.inserted_id)

# Insert multiple documents
documents = [
    {"name": "Jane Smith", "age": 30},
    {"name": "Alice Johnson", "age": 35},
]
insert_results = collection.insert_many(documents)
print("Inserted document IDs:", insert_results.inserted_ids)
