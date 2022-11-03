from Pages.Locators import LocatorNavegacion, LocatorCargaVencimientos
from Pages.TestBase.Funciones import Funciones
from selenium.common.exceptions import TimeoutException


class CargarVencimientosPage(object):
    def __init__(self, driver):
        self.driver = driver

    def accesoVista(self, tiempo):
        try:
            driver = self.driver
            f = Funciones(driver)
            f.dar_click(LocatorNavegacion.BTNHAMBURGUESA, tiempo)
            f.dar_click(LocatorNavegacion.MENUMASGESTION, tiempo)
            f.dar_click(LocatorNavegacion.MENUVENCIMIENTOS, tiempo)
            f.dar_click(LocatorNavegacion.MENUCARGAVENCIMIENTOS, tiempo)
            f.dar_click(LocatorNavegacion.VISTACARGAVENCIMIENTOS, tiempo)
            if LocatorCargaVencimientos.URLVISTA == driver.current_url:
                "Acceso correcto a la vista"
        except TimeoutException as error:
            print(error.msg)
            print("No fue posible acceder a la vista")

    def cargaVencimientos(self, ruta, mes, annio, tiempo):
        try:
            driver = self.driver
            f = Funciones(driver)
            f.cargarArchivo(LocatorCargaVencimientos.INPUTARCHIVO, ruta, tiempo)
            f.seleccionarValor(LocatorCargaVencimientos.SELECTORMES, mes, tiempo)
            f.seleccionarValor(LocatorCargaVencimientos.SELECTORANNIO, annio, tiempo)
            f.dar_click(LocatorCargaVencimientos.BTNCARGAR, tiempo)
        except TimeoutException as error:
            print(error.msg)
            print("No fue posible realizar la carga de vencimientos")
