from qaSet import challengeSet
from selenium.webdriver.common.by import By

class challengeGet():
#-------------------#
    def __init__(self, driver):
        self.driver = driver
        self.switchwin = challengeSet(self.driver)
        self.banner = (By.CSS_SELECTOR, "body > h1")
        self.value = (By.XPATH, '/html/body/div[1]/div[3]/fieldset/select/option[3]')
        self.sugest = (By.XPATH, '//*[@id="autocomplete"]')
        self.banner2 = (By.XPATH, '//*[@id="header-part"]/div[2]/div/div/div[2]/div/div[1]/div[2]/span')
        self.coursesbanner = (By.CSS_SELECTOR, 'body > div > div:nth-child(3) > section.courses-section > div.text-center > a')
        self.text = (By.XPATH, '/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]')   
    #---------------------------------------------#
    
    def getBanner(self):
        return self.driver.find_element(*self.banner).text
    
    def getSugest(self):
        return self.driver.find_element(*self.sugest).get_attribute('value')

    def getVaule(self):
        return self.driver.find_element(*self.value).text
    
    def getGuaranteeBanner2(self):
        self.switchwin.switch_to_win(1)
        return self.driver.find_element(*self.banner2).text
    
    def getCoursesBanner(self):
        return self.driver.find_element(*self.coursesbanner).text
    
    def getText(self):
        with open("alert.txt", "r") as textfile:
            alertext = textfile.read()
            return alertext
        
    def getParagraph(self):
        return self.driver.find_element(*self.text).text