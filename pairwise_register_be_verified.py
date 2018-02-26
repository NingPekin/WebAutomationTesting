from allpairspy import AllPairs
# username["valid","invalid","null","specific characters"]
# email["valid","invalid","specific characters"]
# password["valid","too short","null","specific characters"]
# button["done","cancel"]

import pytest
import  init
import unittest_register
from allpairspy import AllPairs

def function_to_be_tested(username, email, password,button):
    # do something
    driver = init.init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")
    driver.implicitly_wait(100)
    init.navigate_to_website(driver, "https://ningpekin.github.io/BlueWhaleMontreal")
    btn_register = init.find_element_by_xpath(driver, "/html/body/nav/div/div/ul/li[3]/a")
    btn_register.click()
    input_username=init.find_element_by_id(driver,'username')
    init.send_input(driver,input_username,username)
    input_email=init.find_element_by_id(driver,'email')
    init.send_input(driver,input_email,email)
    input_password=init.find_element_by_id(driver,'password')
    init.send_input(driver,input_password,password)
    if(button=="done"):
        btn_done=init.find_element_by_xpath(driver,"/html/body/div[1]/div/div/form/div[4]/button[1]")
        btn_done.click()

    elif(button=="cancel"):
        btn_cancle=init.find_element_by_class(driver,button)
        btn_cancle.click()
        assert (driver.current_url=="https://ningpekin.github.io/BlueWhaleMontreal/")

    driver.close()


class Test__parameterized(object):

    @pytest.mark.parametrize(
        ["username", "email", "password","button"],
        [
            value_list for value_list in AllPairs([
                ["testpairwise", "test","","!@#@#"],
                ["testpairwise@gmail.com", "test","!@$!@$!@%"],
                ["testpairwise", "0", "", "!$!@@#@#@%"],
                ["done", "cancel"]
        ])
        ])

    def test(self, username, email, password,button):

        assert function_to_be_tested(username, email, password,button)


# output:
#pass  0: ['testpairwise', 'testpairwise@gmail.com', 'testpairwise', 'done']
#fail  1: ['test', 'test', '0', 'done']
#fail  2: ['', '!@$!@$!@%', '', 'done']
#fail  3: ['!@#@#', '!@$!@$!@%', '!$!@@#@#@%', 'cancel']
#fail  4: ['!@#@#', 'test', 'testpairwise', 'cancel']
#fail  5: ['', 'testpairwise@gmail.com', '!$!@@#@#@%', 'cancel']
#fail  6: ['test', 'testpairwise@gmail.com', '', 'cancel']
#fail  7: ['testpairwise', '!@$!@$!@%', '0', 'cancel']
#fail  8: ['!@#@#', 'testpairwise@gmail.com', '0', 'done']
#fail  9: ['testpairwise', 'test', '!$!@@#@#@%', 'done']
#fail 10: ['test', '!@$!@$!@%', 'testpairwise', 'done']
#fail 11: ['', 'test', 'testpairwise', 'done']
#fail 12: ['', 'test', '0', 'done']
#fail 13: ['test', 'test', '!$!@@#@#@%', 'done']
#fail 14: ['testpairwise', 'test', '', 'done']
#fail 15: ['!@#@#', 'test', '', 'done']