from flask import Flask, Blueprint, render_template

# Login manager
from flask_login import LoginManager,login_required

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User

# MySQL
from flask_mysqldb import MySQL


app = Flask(__name__)

# Crear el Blueprint
app_home = Blueprint('app_home', __name__, url_prefix='/home')

# Configurar el login manager
login_manager_app = LoginManager(app)

@app_home.route('/')
@login_required
def home():
    return render_template('home.html')
 

if __name__ == '__main__':
    app.run(debug=True)
