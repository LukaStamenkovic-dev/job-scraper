from database.connection import get_connection

class JobTechnologyRepository:

    def create(self, job_id, technology_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            INSERT INTO job_technologies (
                job_id,
                technology_id
            )
            VALUES (%s, %s)
        """

            cursor.execute(query, (job_id, technology_id))

            connection.commit()

        finally:
            cursor.close()
            connection.close()