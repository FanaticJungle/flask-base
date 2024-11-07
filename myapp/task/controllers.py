from flask import Blueprint

taskRoute = Blueprint('task', __name__, url_prefix='/task')#se liga task con el nombre que pone el usuario con la carpeta

#Creacion de rutas en el modulo rutas, todas estas son rutas
@taskRoute.route('/')#aquí muestra todo el contenido de la tabla
def index():
    return 'Index'

@taskRoute.route('/<int:id>')#Solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')#aquí podemos meter la función de borrar
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))#Aquí se puede meter la función crear
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])#Aquí se actualiza un contenido en específico
def update(id:int):
    return 'update '+str(id)