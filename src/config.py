
#Configuracion para conectar con la base de datos

class Config: #manejo de datos de sesion 
    SECRET_KEY = 'B!1weNAt1T%kvhUI*S'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '' 
    MYSQL_DB = 'scaizenauditoria'
  
 #Servidor en modo de depuracion 
config = {
    'development': DevelopmentConfig 
}