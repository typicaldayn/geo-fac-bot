from selenium.webdriver.common.by import By
from Model.Department import Department
from Scraping.configure_driver import configure_driver


def get_departments(url=''):
    # url = "https://geo.knu.ua/fakultet/pidrozdily/kafedry/"
    # driver = configure_driver(url)
    # departments = _make_departments(driver)
    departments = _construct_departments()
    return departments


def _construct_departments():
    gidrology: Department = Department(name='Кафедра гідрології та гідроекології', url='https://geo.knu.ua/new/kafedry/kafedra-gidrologiyi-ta-gidroekologiyi/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-gidrologiyi-ta-gidroekologiyi/vykladachi-kafedry-gidrologiyi-ta-gidroekologiyi/' )
    geodezii:Department = Department(name='Кафедра геодезії та картографії', url='https://geo.knu.ua/new/kafedry/kafedra-geodeziyi-ta-kartografiyi/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-geodeziyi-ta-kartografiyi/vykladachi-kafedry-geodeziyi-ta-kartografiyi/')
    geografii_ukraini: Department = Department(name='Кафедра географії України', url='https://geo.knu.ua/new/kafedry/kafedra-geografiyi-ukrayiny/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-geografiyi-ukrayiny/vykladachi-kafedry-geografiyi-ukrayiny/')
    krainoznavstva: Department = Department(name='Кафедра країнознавства та туризму', url='https://geo.knu.ua/new/kafedry/kafedra-krayinoznavstva-ta-turyzmu/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-krayinoznavstva-ta-turyzmu/vykladachi-kafedry-krayinoznavstva-ta-turyzmu/')
    economgeo: Department = Department(name='Кафедра економічної та соціальної географії', url='https://geo.knu.ua/new/pidrozdily/kafedry/kafedra-ekonomichnoyi-ta-soczialnoyi-geografiyi/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-ekonomichnoyi-ta-soczialnoyi-geografiyi/vykladachi-kafedry-ekonomichnoyi-ta-soczialnoyi-geografiyi/')
    zemleznavstva: Department = Department(name='Кафедра землезнавства та геоморфології', url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-zemleznavstva-ta-geomorfologiyi/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-zemleznavstva-ta-geomorfologiyi/vykladachi-kafedry-zemleznavstva-ta-geomorfologiyi/')
    meteorology: Department = Department(name='Кафедра метеорології та кліматології', url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-meteorologiyi-ta-klimatologiyi/', staff_url='https://geo.knu.ua/new/fakultet/pidrozdily/kafedry/kafedra-meteorologiyi-ta-klimatologiyi/vykladachi-kafedry-meteorologiyi-ta-klimatologiyi/')
    physgeo: Department = Department(name='Кафедра фізичної географії та геоекології', url='https://physgeo.knu.ua/', staff_url='https://physgeo.knu.ua/department/staff.html')
    departments: [Department] = [gidrology, geodezii, geografii_ukraini,
                                krainoznavstva, economgeo, zemleznavstva, meteorology, physgeo]
    return departments

#
# for department in get_departments():
#     print(department.name)
#     for person in department.get_staff:
#         print(person.name)

# def _make_departments(driver):
#     departments: [Department] = []
#     for department in departments_objects:
#         new_department = Department(get_staff(), get_department_link(), department.text)
#         departments.append(department.text)
#
#     return departments


# def _get_departments_links_and_names(driver):
#     departments_names = driver.find_elements(By.TAG_NAME, 'h4')
#     departments_links = driver.find_elements(By.TAG_NAME, 'a')
#     deparments: [Department] = []
#     for element in departments_links:
#         link = element.get_attribute('href')
#         if link is not None and link.__contains__('')
#
# _get_departments_links_and_names(configure_driver('https://geo.knu.ua/fakultet/pidrozdily/kafedry/'))