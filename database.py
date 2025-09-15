import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

class Database(object):

    def __init__(self):
        pass


    @staticmethod
    def connect():
        host = os.getenv("DATABASE_HOST")
        port = os.getenv("DATABASE_PORT")
        username = os.getenv("DATABASE_USERNAME")
        password = os.getenv("DATABASE_PASSWORD")
        database = os.getenv("DATABASE_DB")

        try:

            connection = psycopg.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                database=database
            )

            if connection:

                return connection

        except Exception as error:

            return {
                'error' : str(error)
            }

    def get_projects(self):

        connection = self.connect()

        if 'error' in connection:

            return connection['error']

        else:
            cursor = connection.cursor()
            query = "SELECT * FROM PROJECTS"

            try:

                cursor.execute(query)
                rows = cursor.fetchall()

                return rows

            except Exception as error:

                return {
                    'error' : str(error)
                }



