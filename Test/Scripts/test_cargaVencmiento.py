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
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location ='/usr/bin/chromium'
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service = service, options=options)
    navegador = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(options=options, service=navegador)

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
        driver.save_screenshot("../../Evidencia/fake_login.png")
    except TimeoutException as error:
        print(error.msg)
        print("No fue posible acceder a la vista...Prueba fallida!")
        driver.save_screenshot("../../Evidencia/fake_login.png")
    time.sleep(5)
    driver.quit()

def test_carga_masiva_vencimientos():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location ='/usr/bin/chromium'
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service = service, options=options)
    navegador = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    carga.cargaVencimientos("../../utils/test_carga_3.csv", "Octubre", "2022", 2)
    try: 
        parrafo = driver.find_element(By.XPATH, "//*[@class='modal-text']")
        textoAlerta = "Se ha ingresado una solicitud de carga." + "\n" + "Cuando el archivo este listo, se enviar?? un correo de notificaci??n."
        assert parrafo.text == textoAlerta, "Carga no realizada"
        print("Test: 2 Carga masiva de vencimientos realizada con ??xito")
        print("Prueba OK")
        driver.save_screenshot("../../Evidencia/fake_login.png")
        driver.quit()
    except TimeoutException as error:
        print(error.msg)
        print("No fue posible realizar carga del archivo...Prueba Fallida!")
        driver.save_screenshot("../../Evidencia/fake_login.png")
        driver.quit()

    print("Test 2: Carga de vencimientos realizada con ??xito")
    time.sleep(5)
    driver.quit()



def test_archivoCarga_invalido():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location ='/usr/bin/chromium'
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service = service, options=options)
    navegador = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=navegador)
    f = Funciones(driver)
    f.Navegar("http://certificacion.qaandain.oneapp.cl/admin", 2)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.accesoLogin("admin", "andain5546")
    carga = CargarVencimientosPage(driver)
    carga.accesoVista(2)
    carga.cargaVencimientos("../../utils/test_carga_3.xlsx", "Octubre", "2022", .5)
    time.sleep(5)
    try:
        parrafo = driver.find_element(By.XPATH, "//*[@class='modal-text']")
        text = "No ha sido posible realizar la carga por los siguientes motivos:" + "\n" + "Archivo inv??lido."
        assert parrafo.text == text, "Prueba fallida"
        print("Test 3: Carga archivo formato incorrecto")
        print("Prueba OK")
        driver.quit()
    except TimeoutException as error:
        print(error.msg)
        print("No se encontro el elemento {}".format(parrafo.text))
        driver.quit()
