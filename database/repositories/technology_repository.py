from database.connection import get_connection
from models.technology import Technology

class TechnologyRepository:

    def get_by_name(self, name):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT id, name
                FROM technologies
                WHERE name = %s;
            """

            cursor.execute(query, (name,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Technology(
                id=row["id"],
                name=row["name"],
            )
        finally:
            cursor.close()
            connection.close()

    def create(self, technology):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            INSERT INTO technologies (name)
            VALUES (%s);
        """

            cursor.execute(query, (technology.name,))

            connection.commit()

            technology.id = cursor.lastrowid

            return technology

        finally:
            cursor.close()
            connection.close()