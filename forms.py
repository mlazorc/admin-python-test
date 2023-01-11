from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import validators


def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(FlaskForm):

    username = StringField('Usuario',[ validators.DataRequired(message="'El ingreso de usuario es obligatorio.'"), validators.Length(max=25, min=4, message="El usuarió debe tener entre 4 y 25 carácteres") ])
    clave = StringField('Contraseña',[ validators.DataRequired(message='El ingreso de clave es obligatorio.'), validators.Length(max=25, min=4, message="El usuarió debe tener entre 4 y 25 carácteres")])
    nombre_completo = StringField('Nombre completo',[validators.DataRequired(message='Ingrese nombre completo del usuario'), validators.Length(min=4, max=25, message='El nombre debe tener un minímo de 4 y y máximo de 25 carácteres')])
    honeyPot = TextAreaField('', [lenght_honeypot])