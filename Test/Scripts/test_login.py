import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Pages.Locators import LocatorLogin
from Pages.PageObjects.LoginPage import LoginPage
from Pages.TestBase.Funciones import Funciones


def test_correct_login():
    global driver
    navegador = Service("../../utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    login = LoginPage(driver)
    login.accesoLogin("admin", "andain5546")
    time.sleep(5)
    try:
        sitio = driver.current_url
        url = "http://certificacion.qaandain.oneapp.cl/admin/admin/usuarios"
        assert sitio == url, "No fue posible acceder al sitio"
        driver.save_screenshot("../../admin-pyhton-test/Evidencia/correct_login.png")
        print("Test 1: Credenciales correctas")
        print("Prueba Ok")
    except AssertionError as msg:
        print(msg)
    driver.quit()


def test_fake_login():
    global driver, modal
    navegador = Service("../../utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin/admin/usuarios", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("fake", "fake")
    time.sleep(2)
    driver.save_screenshot("/Users/sebastiandelvillar/Documents/Testing/admin/admin-python-test/Evidencia/fake_login.png")
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
