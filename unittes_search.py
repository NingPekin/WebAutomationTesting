import unittest
import init as init

class WebSearch(unittest.TestCase):
    def setUp(self):
        self.driver = init.init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")

    # def test_search_metro(self):
    #     init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
    #     element=init.find_element_by_id(self.driver,"input-0")
    #     init.send_input(self.driver,element,"Metro")
    #     # element_list=init.find_element_by_class(self.driver,"ng-scope")
    #     # element_list.text
    #     # print(element_list)
    #     button=init.find_element_by_xpath(self.driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
    #     button.click()
    #     # check title
    #     new_web_title=self.driver.title
    #     self.assertEqual(new_web_title,"Metro List")
    #
    # def test_search_museum(self):
    #     init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
    #     element=init.find_element_by_id(self.driver,"input-0")
    #     init.send_input(self.driver,element,"Museum")
    #     button=init.find_element_by_xpath(self.driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
    #     button.click()
    #     # check title
    #     new_web_title=self.driver.title
    #     self.assertEqual(new_web_title,"Mususm List")
    #
    def test_search_church(self):
        init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
        element=init.find_element_by_id(self.driver,"input-0")
        init.send_input(self.driver,element,"Church")
        result=init.find_element_by_xpath(self.driver,"/html/body/md-virtual-repeat-container/div/div[2]/ul/li").text
        # test serach result in hint
        self.assertEqual("Church",result)
        button=init.find_element_by_xpath(self.driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
        button.click()
        # test title--if website redirect correcttly
        new_web_title=self.driver.title
        self.assertEqual(new_web_title,"Church List")

    def test_search_unvalide(self):
        input="People"
        init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
        element=init.find_element_by_id(self.driver,"input-0")
        init.send_input(self.driver,element,input)
        result=init.find_element_by_xpath(self.driver,"/html/body/md-virtual-repeat-container/div/div[2]/ul/li").text
        # test serach result in hint
        input1='No lists matching "People" were found.'
        self.assertEqual(input1,result)
        button=init.find_element_by_xpath(self.driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
        button.click()
        web_title=self.driver.title
# no change web page
        self.assertEqual(web_title,"Blue Whale Montreal")

    def test_search_non_sensitive_church(self):
        init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")
        element=init.find_element_by_id(self.driver,"input-0")
        init.send_input(self.driver,element,"cHUrch")
        button=init.find_element_by_xpath(self.driver,"/html/body/section[1]/div/table/tbody/tr/td[2]/div/button")
        button.click()
        # test title--if website redirect?
        new_web_title=self.driver.title
        self.assertEqual(new_web_title,"Blue Whale Montreal")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()