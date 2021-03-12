from flask import render_template, request, redirect, url_for
from src import app
from src.models.user import UsersModel

@app.route('/users')
def listUsers():
    usersModel = UsersModel()
    data =  usersModel.lists()
    return render_template('users/index.html', users=data)

@app.route('/users/create', methods =['GET','POST'])
def createUser():
    if request.method == 'GET':
        return render_template('users/create.html')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password = request.form.get('password')

    usersModel = UsersModel()
    usersModel.create(name,lastname,phone,email,password)

    return redirect(url_for('users'))


