import unittest
import init

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = init.init_firefox_driver("/home/ning/PycharmProjects/testBlueWhale/geckodriver")

    def test_register(self):
        init.navigate_to_website(self.driver,"https://ningpekin.github.io/BlueWhaleMontreal")



    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
        unittest.main()