import time
import json

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC

class Santehnika_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locator

    input_max_price = "//input[@id='arrFilter_P1_MAX']"
    input_min_price = "//input[@id='arrFilter_80_MIN']"
    slider_width = "//*[@id='filter-width']/div[2]/div[3]/span/table/tbody/tr/td/div[2]"
    check_button_produced_keramin = "/html/body/main/section/div/div/aside/div[2]/form/div[4]/div[2]/div[3]/label"
    check_button_produced_belux = '/html/body/main/section/div/div/aside/div[2]/form/div[4]/div[2]/div[1]/label/span'
    price_500_900 = "// *[ @ id = 'filter-price'] / div[2] / div[1] / a[3]"
    value_min_width = "// *[ @ id = 'filter-width'] / div[2] / div[3] / span / table / tbody / tr / td / div[6] / span"
    value_input_min_width = "// *[ @ id = 'arrFilter_80_MIN']"
    input_max_height = "// input[@id= 'arrFilter_82_MAX']"
    button_find = "//*[@id='set_filter']"
    search_input = '//input[@class="b-header__search_form-text"]'




    # gettings

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_max_price)))

    def get_input_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_min_price)))

    def get_slider_width_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_width)))

    def get_button_produced_keramin(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_button_produced_keramin)))

    def get_price_500_900(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_500_900)))

    def get_value_min_width(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_min_width)))

    def get_value_input_min_width(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_min_width)))

    def get_check_button_produced_belux(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_button_produced_belux)))

    def get_input_max_height(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_max_height)))

    def get_button_find(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_find)))

    def get_button_detailed_n(self, i):
        button_detailed_i = "/html/body/main/section/div/div/div[2]/div[2]/div[" +str(i) + "]/a/span"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, button_detailed_i)))

    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))

    # actions

    def click_max_price(self):
        self.get_max_price().click()
        print("click max price")

    def input_max_price(self, max_price):
        self.get_max_price().send_keys(max_price)
        print("input max price")

    def click_price_500_900(self):
        self.get_price_500_900().click()
        print("click price 500-900")


    def click_check_button_produced_belux(self):
        self.get_check_button_produced_belux().click()
        print('click check-button produced belux')

    def click_input_max_height(self):
        self.get_input_max_height().click()
        print('click input max height')

    def fill_input_max_height(self, max_height):
        self.get_input_max_height().send_keys(max_height)
        print(f"fill input max height {max_height}")

    def click_button_find(self):
        self.get_button_find().click()
        print('click button find')


    def click_button_detailed_n(self, i):
        self.get_button_detailed_n(i).click()
        print(f'click button detailed product {i}')

    def fill_search_input(self, find_word):
        self.get_search_input().send_keys(find_word)
        self.get_search_input().send_keys(Keys.RETURN)


    #Methods

    def sort_product(self):
        self.get_current_url()
        self.click_price_500_900()
        self.slider(self.get_slider_width_min(), 100)
        self.assert_value(self.get_value_min_width(), self.get_value_input_min_width().text) # проверяем соотвествии значения в ячейке input и на слайдоре
        self.click_check_button_produced_belux()
        self.fill_input_max_height(90)
        self.click_button_find()

    def add_product_n(self, i):
        self.click_button_detailed_n(i)
        time.sleep(10)











