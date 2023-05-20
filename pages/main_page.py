import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://shop-belux.by/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    button_plumbing = "/html/body/header/div[4]/div/ul/li[2]/a/span[2]"

    #gettings
    def get_button_plumbing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_plumbing)))

    #actions

    def click_button_plumbing(self):
        self.get_button_plumbing().click()
        print("click button plumbing")

    # methods

    def select_menu_plumbing(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_plumbing()
        time.sleep(10)





