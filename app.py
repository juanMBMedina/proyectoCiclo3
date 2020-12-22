from flask import Flask, render_template, request, flash, redirect
from flask import send_from_directory
import utils
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/inicio/')
def inicio():
    return render_template('inicio.html')

@app.route('/recuperar/')
def recuperar():
    return render_template('recuperar_clave.html')

@app.route('/registro/')
def registro():
    return render_template('registro.html')

@app.route('/gestionA/', methods=['GET','POST'])
def gestionA():
    if request.method == 'POST':
        email_user = request.form['correo']
        pass_user   = request.form['clave']
        if utils.userLoggin(email_user, pass_user):
            return render_template("gestionA.html")
        else:
            return render_template('inicio.html')
    else:
        return render_template('gestionA.html')
"""
    try:
        if request.method == 'POST':
            
            if utils.userLoggin(email_user, pass_user):
                flash ('Usuario correcto')
                return render_template("gestionA.html")
            else:
                return render_template('inicio.html')
        elif request.method=='GET':
            flash('Hay un GET')
            return render_template('inicio.html')
    except:
        return render_template("inicio.html")
"""

@app.route('/gestionB/')
def gestionB():
    return render_template('gestionB.html')

@app.route('/hola/')
@app.route('/hola/<string:nombre>/')
@app.route('/hola/<string:nombre>/<int:edad>/')
def hola(nombre=None, edad=None):
    if nombre and edad:
        return "Hola, {0} tienes {1} años.".format(nombre, edad)
    elif nombre:
        return "Hola, {0} ".format(nombre)
    else:
        return "Hola ni edad nombre!"
    