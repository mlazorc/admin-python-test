class Usuario:
    def __init__(self, username, clave, nombre_completo):
        self.username = username
        self.clave = clave
        self.nombre_completo = nombre_completo
    
    def toDBCollection(self):
        return{
            'username': self.username,
            'clave': self.clave,
            'nombre_completo': self.nombre_completo
        }