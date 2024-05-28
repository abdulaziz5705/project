import os
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str) -> str and list:
        db = psql.connect(
            database="project_1",
            user="postgres",
            password="5705",
            host="localhost",
            port="5432"
        )
        cursor = db.cursor()

        cursor.execute(query)
        data = ["update", "alter", "delete", "insert", "create"]
        if query_type in data:
            db.commit()
            return f" create successful"
        else:
            return cursor.fetchall()
