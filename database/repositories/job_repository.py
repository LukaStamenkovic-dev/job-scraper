from database.connection import get_connection
from models.job import Job


class JobRepository:

    def exists_by_job_url(self, job_url):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            SELECT 1
            FROM jobs
            WHERE job_url = %s
            LIMIT 1
        """

            cursor.execute(query, (job_url,))
            return cursor.fetchone() is not None

        finally:
            cursor.close()
            connection.close()

    def create(self, job, company_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
            INSERT INTO jobs (
                company_id,
                job_title,
                city,
                address,
                language,
                job_url,
                salary_min,
                salary_max
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

            cursor.execute(
                query,
            (
                company_id,
                job.job_title,
                job.city,
                job.address,
                job.language,
                job.job_url,
                job.salary_min,
                job.salary_max,
            )
        )

            connection.commit()

            job.id = cursor.lastrowid

            return job

        finally:
            cursor.close()
            connection.close()