from models.company import Company
from services.company_service import CompanyService


def main():
    service = CompanyService()

    company = Company(
        name="Microsoft",
        website_url="https://microsoft.com",
        company_size="10000+",
        company_type="Product",
    )

    saved_company = service.get_or_create(company)

    print(f"ID: {saved_company.id}")
    print(f"Name: {saved_company.name}")


if __name__ == "__main__":
    main()