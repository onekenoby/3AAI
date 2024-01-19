# pip install 'vanna[postgres]'
from vanna.flask import VannaFlaskApp
import vanna
from vanna.remote import VannaDefault
import os
import dotenv

dotenv.load_dotenv()


vanna_api_key = os.getenv("VANNA_API_KEY")
host = os.getenv("POSTGRES_HOST")
dbname = os.getenv("POSTGRES_DATABASE")
user = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")
vanna_model_name = os.getenv("VANNA_MODEL")

vn = VannaDefault(model=vanna_model_name, api_key=vanna_api_key)
vn.connect_to_postgres(host=host, dbname=dbname, user=user, password=password, port=port)

VannaFlaskApp(vn).run()