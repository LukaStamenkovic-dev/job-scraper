from database.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def get_or_create(self, company):
        existing_company = self.repository.get_by_name(company.name)

        if existing_company is not None:
            return existing_company

        return self.repository.create(company)