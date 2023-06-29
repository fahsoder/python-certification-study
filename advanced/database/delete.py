### Database Deletions ###

from connection import collection

# Delete a single document
query = {"name": "John Doe"}
delete_result = collection.delete_one(query)
print("Deleted documents:", delete_result.deleted_count)

# Delete multiple documents
query = {"age": {"$gt": 30}}  # Find documents where age is greater than 30
delete_results = collection.delete_many(query)
print("Deleted documents:", delete_results.deleted_count)
