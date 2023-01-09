from wtforms import Form
from wtforms import StringField, TextAreaField
from wtforms import validators


def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    username = StringField('Usuario',
        [ 
           validators.DataRequired(message='El ingreso de usuario es oblogatorio.'),
           validators.length(min=4, max=25, message='Ingrese nombre de usuario válido')
        ]
        )
    clave = StringField('Clave',
        [
            validators.DataRequired(message='El ingreso de clave es obligatorio.')
        ]
        )
    nombre_completo = StringField('Nombre Completo')
    honeyPot = TextAreaField('', [lenght_honeypot])