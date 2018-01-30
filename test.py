from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import init as init

driver = init.init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")
init.navigate_to_website(driver,"https://ningpekin.github.io/BlueWhaleMontreal")
# driver.wait = WebDriverWait(driver, 1000)
element=init.find_element_by_id(driver,"input-0")
init.send_input(driver,element,"Metro")
element=init.find_element_by_xpath(driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
element.click()
driver.implicitly_wait(30)
driver.close()