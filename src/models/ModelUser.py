#Se llama a User
from .entities.User import User
 

class ModelUser():

    @classmethod 
    def login(self, db, user): #referencia al propio objeto, conexion a la db(app.py),
                                #user son los datos enviados desde app.py
        #Se realiza la consulta
        try:
            cursor = db.connection.cursor()
            sql = """SELECT Id, Nombre, Apellidos, Telefono, Password,Tipo_usuario,Cambio_contraseña,Estatus_usuario  FROM usuarios
            WHERE Nombre = '{}'""".format(user.nombre_user) #permite saber si el usuario
                                                        #existe dentro de la DB
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], row[3], User.check_password(row[4], user.password_user),row[5],row[6],row[7])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)   
        finally:
            cursor.close()#Cierro la conexión
    
    @classmethod #Esta funcion es utilizada por login_manager_app en app.py para recuperar los datos
    #del usuario
    def get_by_id(self, db, id): #referencia al propio objeto, conexion a la db, para hacer la autenticacion
        try:
            cursor = db.connection.cursor()
            sql = """SELECT Id, Nombre, Apellidos, Telefono,Tipo_usuario,Cambio_contraseña,Estatus_usuario FROM usuarios
            WHERE id = '{}'""".format(id) #permite saber si el usuario
                                                        #existe dentro de la DB
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1],row[2],None, row[3], row[4], row[5], row[6])
            else:
                return None

        except Exception as ex:
            raise Exception(ex)     
        finally:
            cursor.close()#Cierro la conexión