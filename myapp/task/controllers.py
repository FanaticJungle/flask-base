import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from myapp.task import operationsCRUD
from myapp.task import forms
from myapp import config
from werkzeug.utils import secure_filename

taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')
#Creacion de rutas en el modulo rutas, todas estas son rutas
@taskRoute.route('/')#aquí muestra todo el contenido de la tabla
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items)#haciendo consulta a base de datos
    return render_template('dashboard/task/index.html', tasks=operationsCRUD.getAll())

@taskRoute.route('/<int:id>')#Solo muestra la que tenga este id previo seleccionado
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')#aquí podemos meter la función de borrar
def delete(id:int):
        if id != None and id != "":
            operationsCRUD.delete(id)
            return redirect(url_for('task.index'))

#Ruta para crear una nueva 'tarea'
@taskRoute.route('/create', methods=('GET','POST'))#Aquí se puede meter la función crear
def create():
    form = forms.Task()
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data)
       return redirect(url_for('tasks.index'))
    return render_template('dashboard/task/create.html', form=form)

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])#Aquí se actualiza un contenido en específico
def update(id:int):
    task = operationsCRUD.getById(id, True)
    form = forms.Task()
    
    if request.method == 'GET':
        form.name.data = task.name
    
    if form.validate_on_submit():
        operationsCRUD.update(id, form.name.data)
        
        print(form.file.data)
        print(form.file.data.filename)
        f = form.file.data
        if f and config.allowed_extensions_file(form.file.data.filename):
            
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.instance_path, current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('tasks.index'))
        
    return render_template('dashboard/task/update.html', form=form, id=id)