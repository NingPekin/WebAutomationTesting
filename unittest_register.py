import unittest

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import init

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = init.init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")
        self.driver.implicitly_wait(100)


    def test_register_page(self):
        init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
        btn_register=init.find_element_by_xpath(self.driver,"/html/body/nav/div/div/ul/li[3]/a")
        btn_register.click()
        self.assertEqual(self.driver.current_url,"https://ningpekin.github.io/BlueWhaleMontreal/register.html")

    # def test_cancel(self):
    #     self.test_register_page()
    #     btn_cancle=init.find_element_by_class(self.driver,"cancel")
    #     btn_cancle.click()
    #     self.assertEqual(self.driver.current_url,"https://ningpekin.github.io/BlueWhaleMontreal/")


    # def test_invalid_email(self):
    #     self.test_register_page()
    #     input_email=init.find_element_by_id(self.driver,'email')
    #     # invalid email
    #     init.send_input(self.driver,input_email,"invalid.com")
    #     error_email=init.find_element_by_xpath(self.driver,"/html/body/div[1]/div/div/form/p[1]").text
    #     self.assertEqual(error_email,"Your email is invalid.")
    #
    #     # valid email
    #     init.send_input(self.driver,input_email,"test@test.com")
    #
    # def test_invalid_password(self):
    #     self.test_register_page()
    #     input_password=init.find_element_by_id(self.driver,'password')
    #     # invalid email
    #     init.send_input(self.driver,input_password,"123")
    #     error_email=init.find_element_by_xpath(self.driver,"/html/body/div[1]/div/div/form/p[2]").text
    #     self.assertEqual(error_email,"Your password must be at least 6 characters.")
    #
    def test_valid_info(self):
        self.test_register_page()
        input_username=init.find_element_by_id(self.driver,'username')
        init.send_input(self.driver,input_username,"automation_test")
        input_email=init.find_element_by_id(self.driver,'email')
        init.send_input(self.driver,input_email,"test@test.com")
        input_password=init.find_element_by_id(self.driver,'password')
        init.send_input(self.driver,input_password,"123456")
        init.find_element_by_xpath(self.driver,"/html/body/div[1]/div/div/form/div[4]/button[1]").click()

        # check alert
        try:
            time.sleep(2)
            alertBox = self.driver.switch_to_window()
            # print (type(alert))
            alertBox.accept()
            print("alert accepted")
        except NoAlertPresentException:
            pass


        # self.assertEqual(alert,"This username is already registered")

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
        unittest.main()