from database.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.company_repository = CompanyRepository()

    def get_or_create(self, company):
        existing_company = self.company_repository.get_by_name(company.name)

        if existing_company is not None:
            return existing_company

        return self.company_repository.create(company)