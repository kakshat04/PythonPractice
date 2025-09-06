import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class RunChromeTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.letskodeit.com/practice")
        self.driver.maximize_window()
        print(self.driver.title)
        print(self.driver.current_url)

    def find_element_id_name(self):
        element = self.driver.find_element(By.ID, "displayed-text")
        element.send_keys("ABC")
        self.driver.implicitly_wait(5)
        element1 = self.driver.find_element(By.NAME, "show-hide")
        print(element)
        print(element1)

        element2 = self.driver.find_element(By.ID, "hide-textbox")
        if element2.is_enabled():
            element2.click()

        self.driver.implicitly_wait(2)

        element3 = self.driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if not element3.is_displayed():
            self.driver.save_screenshot(os.getcwd() + "\screen.png")

        element4= self.driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        if not element4.is_selected():
            element4.click()
        print(element4.is_selected())
        self.driver.implicitly_wait(2)


    def find_elements_className(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "btn-style")
        for element in elements:
            print(element.text)



chrometest = RunChromeTests()
chrometest.find_element_id_name()
chrometest.find_elements_className()
