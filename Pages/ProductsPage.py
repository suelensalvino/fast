from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    txt_page_title = 'PRODUCTS'
    class_page_title = 'title'
    id_btn_menu = 'react-burger-menu-btn'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_products_page(self):
        try:
            # Página de título do elemento
            element_class_title = self.driver.find_element(By.CLASS_NAME, self.class_page_title)
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            return element_class_title.text == self.txt_page_title and element_menu
        except NoSuchElementException:
            return False