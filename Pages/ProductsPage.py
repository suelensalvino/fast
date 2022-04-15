from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    txt_title_products = 'PRODUCTS'
    class_title = 'title'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver)

    def is_products_page(self):
        is_products_url = self.driver.current_url == self.url
        try:
            title_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text
            is_products_title = title_page.upper() == self.txt_title_products
        except NoSuchElementException:
            is_products_title = False
        return is_products_url and is_products_title