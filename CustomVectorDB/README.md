Esempio di utilizzio:

path = "percorso a cartella esistente"
vectordb = CVDB.CustomVectorDB(path)

with open('percorso a file json/training.json', encoding="utf-8")as file:
   data = json.load(file)

vectordb.add_sql(data)
