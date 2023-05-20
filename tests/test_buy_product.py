import time

from docutils.nodes import math
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.product_page import Product_page
from pages.santehnika_page import Santehnika_page


def test_buy_product_1(set_up):
    path = 'C:\\Users\\Legion\\PycharmProjects\\resource\\chromedriver.exe'
    s = Service(path)
    driver = webdriver.Chrome(service = s)

    print('start test 1')

    mp = Main_page(driver)
    mp.select_menu_plumbing()

    sp = Santehnika_page(driver)
    sp.sort_product()
    sum = 0
    n = 3
    for i in range(1,n): # покупка n-1 -количества товаров
        sp.add_product_n(i)
        pp = Product_page(driver)
        pp.add_product_in_chart()
        sum = pp.check_quantity_of_product() + sum
        driver.back()
        time.sleep(10)

    pp.open_cart()
    sum_digit = '{0:,.2f}'.format(sum).replace(',', ' ') # разбиение на разряды, отображение двух знаков после запятой
    sum_str = sum_digit.replace('.', ',') + " руб."
    print(f' sum of price {sum_str}')
    op = Order_page(driver)
    op.value_final_sum(sum_str)






