from Model.Person import Person
from Scraping.get_staff import get_staff


class Department:
    def __init__(self, url, name, staff_url):
        self.staff_url = staff_url
        self.name = name
        self.url = url
        self.__staff = get_staff(staff_url, name)

    __staff: [Person]

    @property
    def get_staff(self):
        return self.__staff

