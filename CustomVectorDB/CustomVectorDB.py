from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import json
import sqlite3

class CustomVectorDB:

    # Classe CustomVectorDB necessita del percorso di una cartella esistente per essere inizializzata
    # Se non esiste, il db sqlite viene creato
    # Se non esiste, la tabella sql_queries viene creata con i campi (id, sql, metadata, vector)
    def __init__(self, path):
        self.conn = sqlite3.connect(path+'/vector_db.sqlite')
        self.cursor = self.conn.cursor()
        self.embedding = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sql_queries (
                    id INTEGER PRIMARY KEY,
                    sql TEXT,
                    metadata TEXT,
                    vector TEXT
                )''')
        self.conn.commit()

    # Funzione che prende in input la query e il valore di soglia (opzionale)
    # Se trova più di un risultato restituisce il record con la similarità più alta
    # In ordine restituisce ID, SQL, METADATA, SIMILARITY
    # Restituisce una lista vuota se non trova nulla
    def retrieve_sql(self, input_sentence, threshold=0.8):
        input_vector = self.embedding.encode(input_sentence.lower())
        self.cursor.execute('''SELECT id, sql, metadata, vector FROM sql_queries''')
        results = self.cursor.fetchall()
        relevant_results = []
        for result in results:
            stored_vector = json.loads(result[3])
            similarity = cosine_similarity([input_vector], [stored_vector])[0][0]
            if similarity > threshold:
                relevant_results.append([result[0], result[1], result[2], similarity])
        
        if len(relevant_results)>1:
            relevant_results = sorted(relevant_results,key=lambda x: x[3], reverse=True)
            return relevant_results[0]
        else:
            return relevant_results

    # Funzione che prende in input una lista di json annidati per inserimento in banca dati
    # Vedere il file training.json come riferimento per struttura json
    # NB: da implementare gestione di errore (es. viene un json con una struttura che non corrisponde a quella utilizzata al momento)
    def add_sql(self, data):
        for i, doc in enumerate(data):
            vector = self.embedding.encode(doc['metadata'].lower())
            vector_list = [i for i in vector]
            self.cursor.execute('''INSERT INTO sql_queries (sql, metadata, vector) VALUES (?, ?, ?)''', (doc['sql'], doc['metadata'], str(vector_list)))
        self.conn.commit()

    # Funzione che prende in input lista di ids per eliminazione di record in banca dati
    # NB: da implementare gestione di errore (es. viene passato un id che non esiste)
    def delete_sql(self,ids):
        for i in ids:
            self.cursor.execute('DELETE FROM sql_queries WHERE id = '+i)
        self.conn.commit()

    # Funzione che restituisce tutte i record presenti in banca dati
    # Restituisce un oggetto vuoto se non ci sono record
    def getAll_sql(self):
        self.cursor.execute('''SELECT * FROM sql_queries''')
        results = self.cursor.fetchall()

        return results

    # Funzione che prende in input la query da ricercare in banca dati (ricerca su stringa esatta)
    # Restituisce un oggetto vuoto se non trova nulla
    def get_sql(self,query):
        self.cursor.execute("SELECT * FROM sql_queries WHERE metadata = '"+query+"'")
        result = self.cursor.fetchall()

        return result