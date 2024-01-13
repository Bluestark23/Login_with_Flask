#Importacion de flask
from flask import Flask, render_template,request, redirect, url_for, flash

#login manager
from flask_login import LoginManager, login_user, logout_user, login_required

#Importacion de config.py
from config import config

#Se establece la conexion con la base de dato
from flask_mysqldb import MySQL

#proteccion para el login, tokken csrf_token
from flask_wtf.csrf import CSRFProtect 

#Models
from models.ModelUser import ModelUser

#Entities:
from models.entities.User import User



#Routes
from routes.rutas import app_home



#Instancia de flask
app=Flask(__name__)


#Inicializo la conexion con mysql
db=MySQL(app)

#Manejo de login
login_manager_app = LoginManager(app)
#Este es un cargador para el usuario
@login_manager_app.user_loader
def load_user(id):
     return ModelUser.get_by_id(db,id)




#Ruta inicial de la URL
@app.route('/')
def index():#Al acceder me redirije a la ruta login
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])  
def login():
    if request.method == 'POST':
           #Se recupera username y password del html login.html
            user = User(0, request.form['username'],None,None ,request.form['password'],None,None,None)
            logged_user=ModelUser.login(db, user)#Se retorna los datos obtenidos de ModelUser.login
            if logged_user != None:
                if logged_user.password_user:
                     login_user(logged_user)#lo almacena como usuario logeado
                     return redirect(url_for('app_home.home'))#Redirecciona a app_scaizen.scaizen
                else:
                    flash("Contraseña invalida...")#Se muestra un mensaje por flash en el html
                    return render_template('auth/login.html') 
            else:
                flash("Usuario no encontrado...")#Se muestra un mensaje por flash en el html
                return render_template('auth/login.html')

    else:   
            return render_template('auth/login.html')



#cerrar sesion
@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('login'))

#Manejo de errores
def status_401(error):
     return redirect(url_for('login'))

def status_404(error):
     return render_template('error/error_404.html')#Renderiza una plantilla error_404.html y lo muestra


csrf = CSRFProtect()


if __name__=='__main__':
    #configuracion hecha en config.py
    app.config.from_object(config['development'])
    
    csrf.init_app(app)

    #Declaro el blueprint
    app.register_blueprint(app_home)


    #Se configura el manejo de errores
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()