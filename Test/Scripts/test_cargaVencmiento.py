import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from Pages.PageObjects.CargarVencimientosPage import CargarVencimientosPage
from Pages.PageObjects.LoginPage import LoginPage
from Pages.TestBase.Funciones import Funciones


def test_acceso_vista():
    global driver
    navegador = Service("../../utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    vistaCarga = "http://certificacion.qaandain.oneapp.cl/admin/admin/vencimiento/vencimientos/carga"
    url = driver.current_url
    assert url == vistaCarga, "No fue posible acceder a la vista de cargas"
    print("Test 1: Acceso correcto a la vista de carga de vencimientos")
    time.sleep(5)
    driver.quit()

def test_carga_masiva_vencimientos():
    global webdriver
    navegador = Service("../../utils/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    carga.cargaVencimientos("/Users/sebastiandelvillar/Downloads/test_carga_3.csv", "Octubre", "2022", .5)
    time.sleep(5)
    driver.quit()
