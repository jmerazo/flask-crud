from src.connection_bd.bd import mysql
from flask import request, redirect, flash

class UsersModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.get_db().cursor()
        cursor.execute('select * from user') 
        data = cursor.fetchall()
        cursor.close()
        print(data)
        return data

    def create(self, name,lastname,phone,email,password):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute('insert into user (name,lastname,phone,email,password) values (% s,% s,% s,% s,% s)', (name,lastname,phone,email,password))
        flash('User added successfully!')
        cursor.close()

    def update(name, lastname,phone,email,password,id):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute('update register set name = ?,lastname = ?,phone = ?,email = ?,password = ? WHERE id = ?', (name, lastname,phone,email,password,id))
        data = cursor.fetchall()
        cursor.close()
        print(data)
            
    def delete(id):
        cursor = mysql.get_db().cursor()
        #cursor = mysql.cursor()
        cursor.execute('delete from register where id = ?', (id))
        cursor.close()