from wtforms import Form
from wtforms import StringField
from wtforms import validators

class CommentForm(Form):
    username = StringField('Usuario',
        [ 
           validators.DataRequired(message='El usuario es requerido'),
           validators.length(min=4, max=25, message='Ingrese nombre de usuario válido')
        ]
        )
    clave = StringField('Clave')
    nombre_completo = StringField('Nombre Completo')