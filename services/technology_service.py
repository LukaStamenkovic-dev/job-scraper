from database.repositories.technology_repository import TechnologyRepository

class TechnologyService:

    def __init__(self):
        self.technology_repository = TechnologyRepository()

    def get_or_create(self, technology):
        existing_technology = self.technology_repository.get_by_name(technology.name)

        if existing_technology is not None:
            return existing_technology

        return self.technology_repository.create(technology)