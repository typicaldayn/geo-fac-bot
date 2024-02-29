from selenium.webdriver.common.by import By

from Model.Person import Person
from Scraping.configure_driver import configure_driver


def get_staff(url, department_name=''):
    driver = configure_driver(url)
    staff = _scrape_staff(driver, department_name)
    return staff


def _scrape_staff(driver, department_name):
    tag_name = 'h4'
    if department_name == 'Кафедра фізичної географії та геоекології':
        tag_name = 'h3'
    staff_objects = driver.find_elements(By.TAG_NAME, tag_name)
    staff: [Person] = []
    for staff_object in staff_objects:
        person = Person(name=staff_object.text, contact='')
        staff.append(person)

    return staff
