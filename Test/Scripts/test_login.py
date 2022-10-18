import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Pages.Locators import LocatorLogin
from Pages.PageObjects.LoginPage import LoginPage
from Pages.TestBase.Funciones import Funciones


def test_correct_login():
    global driver
    navegador = Service("/Users/marcolazo/Documents/Andain/PythonEnv/admin/admin-env/utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    time.sleep(5)
    try:
        sitio = driver.current_url
        url = "http://certificacion.qaandain.oneapp.cl/admin/admin/usuarios"
        assert sitio == url, "No fue posible acceder al sitio"
        print("Test 1: Credenciales correctas")
        print("Prueba Ok")
    except AssertionError as msg:
        print(msg)
    driver.quit()

def test_fake_login():
    global driver, modal
    navegador = Service("/Users/marcolazo/Documents/Andain/PythonEnv/admin/admin-env/utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("fake", "fake")
    time.sleep(5)
    try:
        modal = driver.find_element(By.XPATH, LocatorLogin.MODAL)
        if modal.is_displayed():
            print("Test 2: Crendenciales incorrectas")
            print("Prueba Ok")
    except AssertionError as msg:
        print(msg)
        print("El elemento {} no está presente".format(modal))

    driver.quit()
