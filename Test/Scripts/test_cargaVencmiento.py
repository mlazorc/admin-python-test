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
from webdriver_manager.chrome import ChromeDriverManager

def test_acceso_vista():
    global driver
    options = Options()
    options.add_argument('--headless')
    options.binary_location = '/usr/bin/google-chrome'
    navegador = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(executable_path=navegador, options=options)
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
    options.add_argument('--headless')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=600,400')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-accelerated-2d-canvas')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-gpu')
    navegador = Service('/usr/local/bin/chromedriver')
    webdriver.Chrome( service = navegador, options = options)
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
    options.add_argument('--headless')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=600,400')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-accelerated-2d-canvas')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-gpu')
    navegador = Service('/usr/local/bin/chromedriver')
    webdriver.Chrome( service = navegador, options = options)
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
