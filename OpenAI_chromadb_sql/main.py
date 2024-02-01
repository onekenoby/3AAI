import os
import chromadb.utils.embedding_functions as embedding_functions
import chromadb
import dotenv
from train import sql_collection
from functions import get_chatGPT_response
import psycopg2
import openai


# ------------------------------ Setup ------------------------------


dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
hostname = os.getenv("HOSTNAME")
port = os.getenv("PORT")


# ------------------------------ Query and results ------------------------------


collection_name = "sql_collection"
persist_directory = "./chromadb"

# Check if the OPENAI_API_KEY environment variable is set. Prompt the user to set it if not.
if "OPENAI_API_KEY" not in os.environ:
    openai.api_key = input(
        "Please enter your OpenAI API Key. You can get it from https://platform.openai.com/account/api-keys\n"
    )
model_name = "gpt-3.5-turbo-1106"
client = chromadb.PersistentClient(path=persist_directory)

while True:
    # Get the user's query
    query = input("Insert your query or type exit: ")
    if query == "exit":
        break
    elif query != "":
        print(f"\nThinking using {model_name}...\n")
        results = sql_collection.query(
            query_texts=[query], n_results=2, include=["documents", "metadatas"]
        )
        response = get_chatGPT_response(query, results["documents"][0], model_name)
        response = response.replace("```sql\n", "")
        response = response.replace("```", "")
        print(response)
        try:
            connection = psycopg2.connect(database=dbname, user=user, password=password, host=hostname, port=port)
            cursor = connection.cursor()
            cursor.execute(response)
            record = cursor.fetchall()
            print("Data from Database: \n", record)
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL:", error)
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection has been closed")
                print("--------------------------------------------------")
    elif query == "":
        print("Please insert a valid query")
        print("--------------------------------------------------")
