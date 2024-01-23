# pip install 'vanna[postgres]'
from vanna.flask import VannaFlaskApp
import vanna
from vanna.remote import VannaDefault
import os
import dotenv

dotenv.load_dotenv()


vanna_api_key = os.getenv("VANNA_API_KEY")
host = os.getenv("POSTGRES_HOST")

# Local DB
dbname = os.getenv("POSTGRES_DATABASE")
user = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")
vanna_model_name = os.getenv("VANNA_MODEL")

# Remote DB
remote_host = os.getenv("POSTGRES_HOST_REMOTE")
remote_port = os.getenv("POSTGRES_PORT_REMOTE")
remote_dbname = os.getenv("POSTGRES_DATABASE_REMOTE")
remote_user = os.getenv("POSTGRES_USERNAME_REMOTE")
remote_password = os.getenv("POSTGRES_PASSWORD_REMOTE")


vn = VannaDefault(model=vanna_model_name,  api_key=vanna_api_key)
vn.connect_to_postgres(host=remote_host, dbname=remote_dbname, user=remote_user, password=remote_password, port=remote_port)

VannaFlaskApp(vn).run()