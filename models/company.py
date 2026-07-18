class Company:
    def __init__(self, name, website_url, company_size, company_type, id = None):
        self.id = id
        self.name = name
        self.website_url = website_url
        self.company_size = company_size
        self.company_type = company_type
