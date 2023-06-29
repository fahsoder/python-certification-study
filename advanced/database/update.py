### Databse Updates ###

from connection import collection

# Update a single document
query = {"name": "John Doe"}
new_values = {"$set": {"age": 26}}  # Set the age field to 26
update_result = collection.update_one(query, new_values)
print("Matched documents:", update_result.matched_count)
print("Modified documents:", update_result.modified_count)

# Update multiple documents
query = {"age": {"$lt": 30}}  # Find documents where age is less than 30
new_values = {"$inc": {"age": 1}}  # Increment the age field by 1
update_results = collection.update_many(query, new_values)
print("Matched documents:", update_results.matched_count)
print("Modified documents:", update_results.modified_count)
