import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import openai
import dotenv
import os



dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=OPENAI_API_KEY, model_name="text-embedding-3-small")

# Create a client
client = chromadb.PersistentClient(path="./chromadb")

sql_collection = client.get_or_create_collection(name="sql_collection", embedding_function=openai_ef)


def add_docs(text, tags):
    sql_collection.add(
    documents=[
      text
      ],
    metadatas=[
          {
            "tags": tags
          }
        ],
    ids=[
          (f"{sql_collection.count() + 1}")
        ]
      )

#print(sql_collection.count())

sql = """
SELECT ae_value, pkt_time
FROM measurement
WHERE id_topic = 5
ORDER BY pkt_time ASC
LIMIT 100;
"""

description = "mostrami per il sensore 5 i primi 100 risultati in ordine temporale del valore ae"

#add_docs(sql, description)


#print("document added successfully!")
#print(sql_collection.count())

