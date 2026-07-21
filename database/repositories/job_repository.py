from database.connection import get_connection


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
                    description,
                    location_raw,
                    address,
                    city,
                    country,
                    salary_raw,
                    salary_min,
                    salary_max,
                    salary_currency,
                    salary_period,
                    experience_level,
                    employment_type,
                    language,
                    visa_sponsorship,
                    job_url,
                    source_site,
                    external_job_id,
                    is_external
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                )
            """

            cursor.execute(
                query,
                (
                    company_id,
                    job.job_title,
                    job.description,
                    job.location_raw,
                    job.address,
                    job.city,
                    job.country,
                    job.salary_raw,
                    job.salary_min,
                    job.salary_max,
                    job.salary_currency,
                    job.salary_period,
                    job.experience_level,
                    job.employment_type,
                    job.language,
                    job.visa_sponsorship,
                    job.job_url,
                    job.source_site,
                    job.external_job_id,
                    job.is_external,
                )
            )

            connection.commit()

            job.id = cursor.lastrowid

            return job

        finally:
            cursor.close()
            connection.close()