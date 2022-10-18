
class LocatorLogin(object):
    LOGO = "//img[@src='/admin/img/logotipo.png']"
    USUARIO = "//input[@id='AdministradorUsuario']"
    CLAVE = "//input[@id='AdministradorClave']"
    BTNINGRESAR = "//button[contains(.,'Ingresar')]"
    MODAL = "//div[@class='modal-wrapper'][contains(.,'Usuario o password incorrecto.')]"