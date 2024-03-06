from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import json
import sqlite3

class CustomVectorDB:

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

    def retrieve_sql(self, input_sentence, threshold=0.9):
        input_vector = self.embedding.encode(input_sentence.lower())
        self.cursor.execute('''SELECT sql, metadata, vector FROM sql_queries''')
        results = self.cursor.fetchall()
        relevant_results = []
        for result in results:
            stored_vector = json.loads(result[2])
            similarity = cosine_similarity([input_vector], [stored_vector])[0][0]
            if similarity > threshold:
                relevant_results.append([result[0], result[1], float(similarity)])
        
        if len(relevant_results)>1:
            relevant_results = sorted(relevant_results,key=lambda x: x[2], reverse=True)

        return relevant_results

    def add_sql(self, data):
        for i, doc in enumerate(data):
            vector = self.embedding.encode(doc['metadata'].lower())
            vector_list = [i for i in vector]
            self.cursor.execute('''INSERT INTO sql_queries (sql, metadata, vector) VALUES (?, ?, ?)''', (doc['sql'], doc['metadata'], str(vector_list)))
        self.conn.commit()

    def delete_sql(self,ids):
        for i in ids:
            self.cursor.execute('DELETE FROM sql_queries WHERE id = '+i)
        self.conn.commit()

    def getAll_sql(self):
        self.cursor.execute('''SELECT * FROM sql_queries''')
        results = self.cursor.fetchall()

        return results

    def get_sql(self,query):
        self.cursor.execute("SELECT * FROM sql_queries WHERE metadata = "+query)
        result = self.cursor.fetchall()

        return result