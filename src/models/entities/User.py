#Se utiliza para chequear el password
from werkzeug.security import check_password_hash, generate_password_hash

#Saber si se encuentra activo
from flask_login import UserMixin

#Esta clase es un reflejo de la tabla usuarios que se tiene en la db
class User(UserMixin):

    def __init__(self, Id, Nombre, Apellido, Telefono, Password, Tipo_usuario, Cambio_contraseña, Estatus_usuario  ) -> None:
        self.id = Id
        self.nombre_user = Nombre
        self.apellido_user = Apellido
        self.password_user = Password
        self.telefono_user = Telefono
        self.tipo_usuario_user = Tipo_usuario
        self.cambio_contraseña_user = Cambio_contraseña
        self.estatus_usuario_user = Estatus_usuario

    @classmethod  #No se instancia la clase    
    def check_password(self, hashed_password, password_user):#hashed_password -> es el dato que esta guardado en la db
                                                            #password_user -> este es el password en texto plano
        return check_password_hash(hashed_password, password_user)#convierte la contraseña de la db en texto plano
 
#Aqui yo genere mi password hash para albadti, solo se ejecuta esta clase
    #python .\src\models\entities\User.py       
print(generate_password_hash('albadti'))