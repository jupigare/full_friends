from flask import Flask, request, redirect, render_template, flash
# from mysqlconnection import MySQLConnector
app = Flask(__name__)
# mysql = MySQLConnector('fullfriends')
app.secret_key = 'ThisIsSecret'
def validate():
    errors = 0
    #Check first name
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'firstNameError')
        errors += 1
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers','firstNameError')
        errors += 1
app.run(debug=True)
