from flask import Blueprint, render_template, request, redirect, url_for
from myapp.task import operationsCRUD

taskRoute = Blueprint('task', __name__, url_prefix='/task')#se liga task con el nombre que pone el usuario con la carpeta
task_list = ['tasks 1', 'tasks 2', 'tasks 3']
#Creacion de rutas en el modulo rutas, todas estas son rutas
@taskRoute.route('/')#aquí muestra todo el contenido de la tabla
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items)#haciendo consulta a base de datos
    return render_template('dashboard/task/index.html', tasks=task_list)

@taskRoute.route('/<int:id>')#Solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')#aquí podemos meter la función de borrar
def delete(id:int):
        if id != None and id != "":
            del task_list[id]
            return redirect(url_for('task.index'))

#Ruta para crear una nueva 'tarea'
@taskRoute.route('/create', methods=('GET','POST'))#Aquí se puede meter la función crear
def create():
    task = request.form.get('task')
    if task != None and task != "":#verifica que la ruta no esté vacía
        task_list.append(task)
        return redirect(url_for('task.index'))
    return render_template('dashboard/task/create.html')

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])#Aquí se actualiza un contenido en específico
def update(id:int):
    task = request.form.get('task')
    if task != None and task != "":
        task_list[id] = task
        return redirect(url_for('task.index'))
        
    return render_template('dashboard/task/update.html')