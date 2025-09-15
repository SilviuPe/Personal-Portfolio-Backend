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
                dbname=database
            )

            if connection:

                return {
                    'connection' : connection
                }

        except Exception as error:

            return {
                'error' : str(error)
            }

    def get_projects(self):

        connection = self.connect()

        if 'error' in connection:

            return {
                'error': connection['error']
            }

        else:
            cursor = connection['connection'].cursor()
            query = "SELECT * FROM PROJECTS"

            try:

                cursor.execute(query)
                rows = cursor.fetchall()

                # Get column names
                columns = [col[0] for col in cursor.description]

                # Build list of dicts
                result = [dict(zip(columns, row)) for row in rows]

                return result

            except Exception as error:

                return {
                    'error' : str(error)
                }



