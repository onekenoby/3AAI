import chromadb
from train import sql_collection

# Show me the first 10 items of the collection
check_collection = sql_collection.peek()
check_collection.pop('embeddings')
print(check_collection)

print("Total documents:", sql_collection.count())
