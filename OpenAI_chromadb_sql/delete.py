import chromadb
from train import sql_collection

print(sql_collection.count())

sql_collection.delete(
    where={"tags": "mostrami per il sensore 5 solamente i primi 100 risultati del valore ae"}
)
print("Document deleted successfully!")
print(sql_collection.count())
