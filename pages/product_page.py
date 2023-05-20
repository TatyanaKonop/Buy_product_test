from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locator
    button_cart = "//div[@id='resbuttoncart']"
    mini_cart = "// div[ @ id = 'mini_cart1']"
    button_make_order = "//*[@id='mini_cart1']/div/div[1]/a"
    # input_quantity = "//input[@id ='quant-40453']"
    input_quantity = '//*[@id ="quant-40453"]'
    price_product = '/html/body/main/section[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]'

    #gettings

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,self.button_cart)))

    def get_mini_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mini_cart)))

    def get_button_make_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))

    def get_input_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_quantity)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    #actions
    def click_button_cart(self):
        self.get_button_cart().click()
        print('click button cart')

    def click_button_make_order(self):
        self.get_button_make_order().click()
        print('click button make order')

    def input_quantity(self, quant):
        self.get_input_quantity().send_keys(quant)
        print('input quantity of product ')

    #methods

    def add_product_in_chart(self):
        self.get_current_url()
        self.click_button_cart()


    def open_cart(self):
        self.get_current_url()
        self.move_to_element(self.get_mini_cart())
        self.click_button_make_order()
        self.screenshots()



    def check_quantity_of_product(self):
        value_price = self.get_price_product().text
        print(f' product price {value_price}')
        value_price_number = value_price.replace(" руб.", "")
        value_price_number_point = value_price_number.replace(',', '.')
        return float(value_price_number_point)






