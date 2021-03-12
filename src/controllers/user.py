from flask import render_template, request, redirect, url_for
from src import app
from src.models.user import UsersModel

app.secret_key = "mysecretkey"

@app.route('/users')
def listUsers():
    usersModel = UsersModel()
    data = usersModel.lists()
    return render_template('users/index.html', users=data)


@app.route('/users/create', methods=['GET', 'POST'])
def createUser():
    if request.method == 'GET':
        return render_template('users/create.html')
    name = request.form['name']
    lastname = request.form['lastname']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']

    usersModel = UsersModel()
    usersModel.create(name,lastname,phone,email,password)

    return redirect(url_for('listUsers'))


@app.route('/update/<id>', methods = ['POST', 'GET'])
def updateUser(id, name, lastname,phone,email,password):
    usersModel = UsersModel()
    data = usersModel.lists()

    usersModel.update(name, lastname,phone,email,password)
    return render_template('updateUser.html', contact= data)
