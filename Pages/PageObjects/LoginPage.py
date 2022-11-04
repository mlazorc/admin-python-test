from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Pages.Locators import LocatorLogin
from Pages.TestBase.Funciones import Funciones


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def accesoLogin(self, usuario, clave):
        try:
            driver = self.driver
            if driver.find_element(By.XPATH, LocatorLogin.LOGO).is_displayed():
                f = Funciones(driver)
                f.Texto_xpath_valida(LocatorLogin.USUARIO, usuario, .5)
                f.Texto_xpath_valida(LocatorLogin.CLAVE, clave, .5)
                f.dar_click(LocatorLogin.BTNINGRESAR, .5)

        except TimeoutException as ex:
            print(ex.msg)
            print("No fue posible acceder a la aplicación, elemento {} no encontrado".format(LocatorLogin.LOGO))
