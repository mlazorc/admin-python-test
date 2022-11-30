import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.PageObjects.CargarVencimientosPage import CargarVencimientosPage
from Pages.PageObjects.LoginPage import LoginPage
from Pages.TestBase.Funciones import Funciones
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options

def test_acceso_vista():
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argment("--remote-debugging-port=9222")
    navegador = '/usr/local/bin/chromedriver'
    command_executor = "http://localhost:4444/wd/hub"
    driver = webdriver.Chrome(navegador, command_executor, options)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    vistaCarga = "http://certificacion.qaandain.oneapp.cl/admin/admin/vencimiento/vencimientos/carga"
    url = driver.current_url
    try:
        assert url == vistaCarga, "No fue posible acceder a la vista de cargas"
        print("Test 1: Acceso correcto a la vista de carga de vencimientos")
        print("Prueba Ok")
    except TimeoutException as error:
        print(error.msg)
        print("No fue posible acceder a la vista...Prueba fallida!")
    time.sleep(5)
    driver.quit()

def test_carga_masiva_vencimientos():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    navegador = '/usr/local/bin/chromedriver'
    command_executor = "http://localhost:4444/wd/hub"
    driver = webdriver.Chrome(navegador, command_executor, options)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    carga.cargaVencimientos("/Users/sebastiandelvillar/Downloads/test_carga_3.csv", "Octubre", "2022", 2)
    try: 
        parrafo = driver.find_element(By.XPATH, "//*[@class='modal-text']")
        textoAlerta = "Se ha ingresado una solicitud de carga." + "\n" + "Cuando el archivo este listo, se enviará un correo de notificación."
        assert parrafo.text == textoAlerta, "Carga no realizada"
        print("Test: 2 Carga masiva de vencimientos realizada con éxito")
        print("Prueba OK")
        driver.quit()
    except TimeoutException as error:
        print(error.msg)
        print("No fue posible realizar carga del archivo...Prueba Fallida!")
        driver.quit()

    print("Test 2: Carga de vencimientos realizada con éxito")
    time.sleep(5)
    driver.quit()



def test_archivoCarga_invalido():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    navegador = '/usr/local/bin/chromedriver'
    command_executor = "http://localhost:4444/wd/hub"
    driver = webdriver.Chrome(navegador, command_executor, options)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    carga.cargaVencimientos("/Users/sebastiandelvillar/Downloads/GC-13741_CP.xlsx", "Octubre", "2022", .5)
    time.sleep(5)
    try:
        parrafo = driver.find_element(By.XPATH, "//*[@class='modal-text']")
        text = "No ha sido posible realizar la carga por los siguientes motivos:" + "\n" + "Archivo inválido."
        assert parrafo.text == text, "Prueba fallida"
        print("Test 3: Carga archivo formato incorrecto")
        print("Prueba OK")
        driver.quit()
    except TimeoutException as error:
        print(error.msg)
        print("No se encontro el elemento {}".format(parrafo.text))
        driver.quit()
