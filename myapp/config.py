import psycopg2
import os

ALLOWED_EXTENSIONS_FILES = {'pdf', 'jpg', 'jpeg', 'gif', 'png'}

def allowed_extensions_file(filename): #test.png
    return '.' in filename and filename.lower().rsplit('.',1)[1] in ALLOWED_EXTENSIONS_FILES

class Config(object):
    
    #Configuracion de las Bases de Datos
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{hostname}/{databasename}".format(username="curso", password="12345", hostname="localhost", databasename="proyecto")
    
    #Configuracion del secret key para el csrf de los formularios
    SECRET_KEY= 'MyS3cr3t3K3y.'
    
    #Configulacion de la carpeta para el almacenamiento de archivos
    UPLOAD_FOLDER= os.path.realpath('.') + '/myapp/uploads'
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True