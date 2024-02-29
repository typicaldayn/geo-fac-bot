import requests
from selenium.webdriver.common.by import By
from File_system.save_pdf import save_pdf

from Scraping.configure_driver import configure_driver


def get_rozklad(url="https://geo.knu.ua/navchannya/rozklad-zanyat/"):
    # url = "https://geo.knu.ua/navchannya/rozklad-zanyat/"
    driver = configure_driver(url)
    courses = _get_courses(driver)
    links = _get_links(driver)
    rozklad = _bind_courses_to_links(courses, links)
    return rozklad


def _bind_courses_to_links(courses, links):
    result = {}
    index = 0
    for course in courses:
        result[course] = links[index]
        index += 1
    return result


def _get_links(driver):
    links = driver.find_elements(by=By.TAG_NAME, value='a')
    rozklad_links = []
    for link in links:
        if link.get_attribute('class') == 'elementor-button elementor-button-link elementor-size-sm':
            rozklad_links.append(link.get_attribute('href'))
    return rozklad_links


def _get_courses(driver):
    courses = driver.find_elements(by=By.TAG_NAME, value="h4")
    courses_list = []
    for course in courses:
        courses_list.append(course.text)
    return courses_list


def get_rozklad_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        save_pdf(response.content)
    else:
        print(f"Failed to retrieve file. Status code: {response.status_code}")
