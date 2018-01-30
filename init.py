from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


def init_chrome_driver(file_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=file_path,
                              chrome_options=options)
    driver.wait = WebDriverWait(driver, 10)
    return driver

def init_firefox_driver(file_path):
    driver = webdriver.Firefox(executable_path=file_path)
    driver.wait = WebDriverWait(driver, 10)
    return driver

def navigate_to_website(driver, site):
    driver.get(site)

def find_element_by_name(driver,name):
    return driver.find_element_by_name(name)

def find_element_by_id(driver,id):
    return driver.find_element_by_id(id)

def find_element_by_xpath(driver,xpath):
    return driver.find_element_by_xpath(xpath)

def find_element_by_class(driver,class_name):
    return driver.find_element_by_class_name(class_name)


def send_input(driver,element,query):
    element.clear()
    element.send_keys(query)
    element.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source


def wait_for_page_load(self, timeout=30):
    old_page = self.browser.find_element_by_tag_name('html')
    yield
    WebDriverWait(self.browser, timeout).until(
        staleness_of(old_page)
    )
# init_chrome_driver("/home/ning/PycharmProjects/testBlueWhale/chromedriver")
# init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")
# driver=init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")
# navigate_to_website(driver,"http://www.python.org")