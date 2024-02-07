import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import dotenv
import os

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

documents_directory = "documents"
collection_name = "documents_collection"
persist_directory = "./chroma_storage"
client = chromadb.PersistentClient(path=persist_directory)
google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=GOOGLE_API_KEY)

collection = client.get_or_create_collection(name=collection_name, embedding_function=google_ef)
check_collection = collection.peek(100)
check_collection.pop('embeddings')
print(check_collection)
print("----------------------------------")
print("Total documents:", collection.count())

print(collection.get(ids='2'))

# To delete a document from the collection
# collection.delete(ids='1')

