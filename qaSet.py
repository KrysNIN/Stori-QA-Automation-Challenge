import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class challengeSet():
#-------------------#
    def __init__(self, driver):
        self.driver = driver        
        self.empty = (By.XPATH, '/html/body/div[1]')
        self.sug_class = (By.XPATH, '/html/body/div[1]/div[2]/fieldset/input')
        self.mex = (By.XPATH, '/html/body/ul/li/div')
        self.drop = (By.XPATH, '/html/body/div[1]/div[3]/fieldset/select')
        self.option1 = (By.XPATH, '//*[@id="dropdown-class-example"]/option[2]')
        self.option2 = (By.XPATH, '/html/body/div[1]/div[3]/fieldset/select/option[3]')
        self.winbutton = (By.XPATH, '//*[@id="openwindow"]')
        self.tabbutton = (By.XPATH, '//*[@id="opentab"]')
        self.iframe = (By.XPATH, '//*[@id="courses-iframe"]')
        self.allcourses = (By. CSS_SELECTOR, 'body > div > div:nth-child(3) > section.courses-section > div.text-center > a')
        self.alertimput = (By. XPATH, '//*[@id="name"]')
        self.alertbutton = (By.CSS_SELECTOR, '#alertbtn')
        self.confirmbutton = (By.CSS_SELECTOR, '#confirmbtn')
        self.table = (By. CSS_SELECTOR, '#product')
        self.wtable = (By.CSS_SELECTOR, 'body > div:nth-child(5) > div.right-align > fieldset:nth-child(2) > div.tableFixHead')
        self.text2 = (By.XPATH, '/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]')
    #-------------------------------------------------------#

    def scrolldown(self, num):
        self.x = 0
        while True:
            self.x += 1
            self.driver.execute_script('scrollBy(0,50)')
            time.sleep(0.1)
            if self.x > num:
                break

    def switch_to_win(self, tab_index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[tab_index])

    # Test 1
    def home(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sug_class)).click()        
        time.sleep(2)

    # Test 2 
    def dropdown(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.drop)).click()     
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.option1)).click()        
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.empty)).click()
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.drop)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.option2)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.empty)).click()
        time.sleep(2)

    # Test 3
    def sugest(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sug_class)).click()        
        self.driver.find_element(*self.sug_class).send_keys('Mex')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.mex)).click()
        time.sleep(2)

    # Test 4
    def switchwindow(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.winbutton)).click()
        self.switch_to_win(1)
        time.sleep(5)
        self.driver.maximize_window()
        self.scrolldown(100)    
        time.sleep(2)
        
        self.text = "guarantee"
        if self.text not in self.driver.page_source:
            raise AssertionError("Guarantee text not found")
        time.sleep(10)
    
    # Test 5
    def switchtab(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.tabbutton)).click()
        self.switch_to_win(1)
        time.sleep(1)
        self.scrolldown(100)
        time.sleep(1)
        self.switch_to_win(0)
        time.sleep(1)
        self.scrolldown(30)
        time.sleep(1)
        self.frame = self.driver.find_element(*self.iframe)
        self.driver.switch_to.frame(self.frame)
        time.sleep(1)
        self.courses = self.driver.find_element(*self.allcourses)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', self.courses)
        time.sleep(1)
        self.driver.get_screenshot_as_file(".//test.png")
        time.sleep(3)

    # Test 6
    def switchalert(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.alertimput)).click()
        self.driver.find_element(*self.alertimput).send_keys('Stori Card')
        time.sleep(1)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.alertbutton)).click()
        self.alert = self.driver.switch_to.alert
        time.sleep(2)
        self.alert.accept()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.alertimput)).click()        
        self.driver.find_element(*self.alertimput).send_keys('Stori Card')
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.confirmbutton)).click()        
        time.sleep(2)
        self.alert = self.driver.switch_to.alert        
        self.alertext = self.alert.text
        self.alert.accept()
        time.sleep(2)

        with open("alert.txt", "w") as file:
            file.write(self.alertext)
        time.sleep(2)

    # Test 7
    def tables(self):        
        table = self.driver.find_element(*self.table)
        rows = table.find_elements(By.TAG_NAME, "tr")
        count_25 = 0
        names = [] 

        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")

            if cells:
                price = int(cells[2].text)

                if price == 25:
                    count_25 += 1
                    names.append(cells[1].text)
        
        print(f"\nTotal Courses at $25: {count_25}")        
        print("\nCourses Names: ")
        print()

        for i in names:            
            print(i)
            print()
    
    # Test 8
    def webtable(self):
        table = self.driver.find_element(*self.wtable)
        rows = table.find_elements(By.TAG_NAME, "tr")
        names = [] 

        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            names.append(cells[0].text)

        print()
        print(f"Names of all the Engineers: ")
        print()

        for i in names:
            print(i)
            print()
    
    # Test 9
    def printext(self):
        self.scrolldown(30)        
        self.frame = self.driver.find_element(*self.iframe)
        self.driver.switch_to.frame(self.frame)
        self.scrolldown(20)
        time.sleep(3)
        element = self.driver.find_element(*self.text2)
        text = element.text
        print (f"\nParagraph: {text}")