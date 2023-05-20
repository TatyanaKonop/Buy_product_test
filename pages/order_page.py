import time


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Order_page(Base):
    def __init__self(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    final_sum = "//*[@id='bx-soa-total']/div[2]/div[4]/span[2]"

    #gettings
    def get_final_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_sum)))


    #actions


    #Metods

    def value_final_sum(self, sum_str):
        print(self.get_final_sum().text)
        self.assert_value(self.get_final_sum(), sum_str)












