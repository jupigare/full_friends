from flask import Flask, request, redirect, render_template, flash
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
app.secret_key = 'ThisIsSecret'
regex_name = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friendsdb")
    return render_template('index.html')

@app.route('/friends', methods=['POST'])
def create():
    errors = 0
    #Check first name
    if request.form['first_name'] == '':
        flash('First name cannot be blank', 'firstNameError')
        errors += 1
    elif not regex_name.match(request.form['first_name']):
#     elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('First name cannot have numbers','firstNameError')
        errors += 1
    else: 
        flash('Success! First name is valid.', 'success')
      #Check last name
    if request.form['last_name'] == '':
        flash('Last name cannot be blank', 'lastNameError')
        errors += 1
    elif not regex_name.match(request.form['last_name']):
#     elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Last name cannot have numbers', 'lastNameError')
        errors += 1
    else:
        flash('Success! Last name is valid.', 'success')
    
    #Check occupation
    if request.form['occupation'] == '':
        flash('Occupation cannot be blank', 'occupationError')
        errors += 1
    else:
        flash('Success! Occupation is valid.', 'success')
    
# See if there are any errors
    if errors > 0:
        flash('No data added to table. Please resolve above errors.', 'err')
    else:
    	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    	data = {
	             'first_name': request.form['first_name'],
	             'last_name': request.form['last_name'],
	             'occupation': request.form['occupation']
	           }
        mysql.query_db(query, data)
        flash('Success! {} {} added to database.'.format(request.form['first_name'],request.form['last_name'], 'success'))
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
