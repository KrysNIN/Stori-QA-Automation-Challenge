import unittest
import HtmlTestRunner
from qaSet import challengeSet
from qaGet import challengeGet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class test_challenge(unittest.TestCase):
#--------------------------------------#
    def setUp(self):
        option = Options()
        option.add_argument ('--ignore-ssl-errors=yes')
        option.add_argument ('--ignore-certificate-errors')
        self.driver_service = Service(executable_path='C:\WebDriver\chromedriver.exe')
        self.driver = webdriver.Chrome(chrome_options= option, service=self.driver_service)
        self.driver.get('https://rahulshettyacademy.com/AutomationPractice/')
        self.all_handles = self.driver.window_handles
        self.parent_handles = self.driver.current_window_handle
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.search = challengeSet(self.driver)
        self.get = challengeGet(self.driver)        
    #--------------------------------------#

    #@unittest.skip('1')
    def test_1(self):
        self.search.home()
        self.assertTrue('Practice Page' in self.get.getBanner())
    
    #@unittest.skip('2')
    def test_2(self):
        self.search.dropdown()
        self.assertTrue('Option2' in self.get.getVaule())

    #@unittest.skip('3')
    def test_3(self):
        self.search.sugest()
        self.assertTrue('Mexico' in self.get.getSugest())

    #@unittest.skip('4')
    def test_4(self):
        self.search.switchwindow()
        self.assertTrue('guarantee' in self.get.getGuaranteeBanner2())
    
    #@unittest.skip('5')
    def test_5(self):
        self.search.switchtab()
        self.assertTrue('VIEW ALL COURSES.' in self.get.getCoursesBanner())

    #@unittest.skip('6')
    def test_6(self):
        self.search.switchalert()
        self.assertTrue('Hello Stori Card, Are you sure you want to confirm?' in self.get.getText())

    #@unittest.skip('7')
    def test_7(self):
        self.search.tables()
        self.assertTrue('Practice Page' in self.get.getBanner())

    #@unittest.skip('8')
    def test_8(self):
        self.search.webtable()
        self.assertTrue('Practice Page' in self.get.getBanner())

    #@unittest.skip('9')
    def test_9(self):
        self.search.printext()
        self.assertTrue('His mentorship program is most after in the software testing community with long waiting period.' in self.get.getParagraph())

    #-----------------#
    def tearDown(self):    
        self.driver.close()
        self.driver.quit()
#-------------------------#
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())