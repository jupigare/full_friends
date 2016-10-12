from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'ThisIsSecret'
# def validate():
#     errors = 0
#     #Check first name
#     if request.form['first_name'] == '':
#         flash('Name cannot be blank', 'firstNameError')
#         errors += 1
#     elif any(char.isdigit() for char in request.form['first_name']) == True:
#         flash('Name cannot have numbers','firstNameError')
#         errors += 1
#     else:
#         pass
#       #Check last name
#     if request.form['last_name'] == '':
#         flash('Name cannot be blank', 'lastNameError')
#         errors += 1
#     elif any(char.isdigit() for char in request.form['last_name']) == True:
#         flash('Name cannot have numbers', 'lastNameError')
#         errors += 1
#     else:
#         pass
#     #Check occupation
#     if request.form['occupation'] == '':
#         flash('Occupation cannot be blank', 'occupationError')
#         errors += 1
#     else:
#         pass
# #See if there are any errors
#     if errors > 0:
#         return False
#     else:
#         return True
@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friendsdb")
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def editInfo(id):
    print id
    return redirect('/')

@app.route('/friends/<id>/edit')
def viewEdit(id):
    return render_template('edit.html')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    return redirect('/')

app.run(debug=True)
