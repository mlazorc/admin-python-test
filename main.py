from flask import Flask, jsonify, redirect, url_for, Response 
from flask import render_template
from flask import request 
import forms 
import connect as connect
from usuario import Usuario


db = connect.dbConnection()
app = Flask(__name__)
app.secret_key = '1234567890'
@app.route('/', methods=['GET', 'POST'])
def index():
    usuarios = db['antuapp']
    userReceived = usuarios.usuario.find()
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.clave.data)
        print (comment_form.nombre_completo.data)
    title = "Antuapp"
    

    return render_template('index.html', title=title, form=comment_form, usuarios=userReceived)


#POST METHOD
@app.route('/usuario', methods=['POST'])
def addUsuario():
    usuarios = db['antuapp']
    username = request.form['username']
    clave = request.form['clave']
    nombre_completo = request.form['nombre_completo']
    if username and clave and nombre_completo:
        usuario = Usuario(username, clave, nombre_completo)
        usuarios.usuario.insert_one(usuario.toDBCollection())
        response = jsonify({
            'username': username,
            'clave': clave,
            'nombre_completo': nombre_completo
        })
        return redirect(url_for('index'))
    else:
        return notFound()


@app.route('/edit/<string:user>', methods=['POST'])
def edit(user):
    usuarios = db['antuapp']
    username = request.form['username']
    clave = request.form['clave']
    nombre_completo = request.form['nombre_completo']

    if username and clave and nombre_completo:
        usuarios.usuario.update_one({'username': user}, {'$set': {'username': username, 'clave':clave, 'nombre_completo': nombre_completo}})
        jsonify({'message': user + ' actualizado correctamente'})
        return redirect(url_for('index'))
    else:
        return notFound()

@app.route('/delete/<string:username>')
def delete(username):
    usuarios = db['antuapp']
    usuarios.usuario.delete_one({'username': username})
    return redirect(url_for('index'))


@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
   app.run(debug=True, port=8000)