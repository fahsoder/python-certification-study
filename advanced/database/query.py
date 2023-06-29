### Database Queries ###

from connection import collection

# Find all documents
all_documents = collection.find()
for document in all_documents:
    print(document)

# Find documents that match a specific condition
query = {"age": {"$gt": 30}}  # Find documents where age is greater than 30
results = collection.find(query)
for document in results:
    print(document)
