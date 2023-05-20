import datetime

from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)


    """method get current url"""
    def get_current_url(self):
        get_current_url = self.driver.current_url
        print(f'current url {get_current_url}')

        """method assert value"""
    def assert_value(self, word, result):
        value_word = word.text
        assert value_word == result
        print('assertion correct')

    """method move slider"""
    def slider(self, locator_slider, steps):
        self.action.click_and_hold(locator_slider).move_by_offset(steps, 0).release().perform()
        print("slide ")

    """method move to element"""
    def move_to_element(self, locator_element):
        self.action.move_to_element(locator_element).perform()
        print("move to element")

    """screenshot"""
    def screenshots(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Legion\\PycharmProjects\\my_project\\screens\\' + name_screenshot)








