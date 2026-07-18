from database.connection import get_connection
from models.company import Company


class CompanyRepository:

    def get_by_name(self, name):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    id,
                    name,
                    website_url,
                    company_size,
                    company_type
                FROM companies
                WHERE name = %s
            """

            cursor.execute(query, (name,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Company(
                id=row["id"],
                name=row["name"],
                website_url=row["website_url"],
                company_size=row["company_size"],
                company_type=row["company_type"],
            )
        finally:
            cursor.close()
            connection.close()

    def create(self, company):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO companies (
                name,
                website_url,
                company_size,
                company_type
            )
                VALUES (%s, %s, %s, %s)
        """

            cursor.execute(
            query,
            (
                company.name,
                company.website_url,
                company.company_size,
                company.company_type,
            )
        )

            connection.commit()

            company.id = cursor.lastrowid

            return company

        finally:
            cursor.close()
            connection.close()