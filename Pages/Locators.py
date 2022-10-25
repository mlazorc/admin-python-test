# This file contains locator classes, wich will be used on each page to identify an element in the view
# Each locator will must have the value of the XPATH of the element that is required to be identified in the view
class LocatorLogin(object):
    LOGO = "//img[@src='/admin/img/logotipo.png']"
    USUARIO = "//input[@id='AdministradorUsuario']"
    CLAVE = "//input[@id='AdministradorClave']"
    BTNINGRESAR = "//button[contains(.,'Ingresar')]"
    MODAL = "//div[@class='modal-wrapper'][contains(.,'Usuario o password incorrecto.')]"


class LocatorNavegacion(object):
    BTNHAMBURGUESA = "//*[@id='sidebar-left']/div[1]/div[2]"
    MENUMASGESTION = "//*[@id='menu']/ul/li[24]/a"
    MENUVENCIMIENTOS = "//*[@id='menu']/ul/li[24]/ul/li[1]/a"
    MENUCARGAVENCIMIENTOS = "//*[@id='menu']/ul/li[24]/ul/li[1]/ul/li[5]/a"
    VISTACARGAVENCIMIENTOS = "//*[@id='menu']/ul/li[24]/ul/li[1]/ul/li[5]/ul/li[1]/a"
    VISTAVENCIMIENTOS = "//*[@id='menu']/ul/li[24]/ul/li[1]/ul/li[1]/a"


class LocatorCargaVencimientos(object):
    URLVISTA = "http://certificacion.qaandain.oneapp.cl/admin/admin/vencimiento/vencimientos/carga"
    TITULOFORMULARIO = "//*[@id='CargaVencimientos']/section/header/h2"
    INPUTARCHIVO = "//input[@id='VencimientoArchivo']"
    SELECTORMES = "//select[@id='VencimientoPeriodoMonth']"
    SELECTORANNIO = "//select[@id='VencimientoPeriodoYear']"
    BTNCARGAR = "//button[@id='cargar']"
    BTNAYUDA = "//*[@id='CargaVencimientos']/section/div/div/div/div[2]/div[1]/div[2]/a"
    TABLAAYUDA = "//*[@id='collapseHelp']/div/div/div/table"