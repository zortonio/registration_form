from flask import Flask, render_template, request, redirect, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods = ['POST'])
def new_user():
    # Validation
    if len(request.form['Email']) < 1:
        flash("Email cannot be left blank!")
    elif not EMAIL_REGEX.match(request.form['Email']):
        flash("Invalid Email!")

    if len(request.form['First_Name']) < 1:
        flash("First Name cannot be left blank!")
    elif not request.form['First_Name'].isalpha():
        flash("First Name cannot contain numbers.")

    if len(request.form['Last_Name']) < 1:
        flash("Last Name cannot be left blank!")
    elif not request.form['Last_Name'].isalpha():
        flash("Last Name cannot contain numbers.")

    if len(request.form['Password']) < 1:
        flash("Password cannot be left blank!")
    elif len(request.form['Password']) < 8:
        flash("Password must be at least 8 characters!")

    if len(request.form['Password_Check']) < 1:
        flash("Please confirm your password!")
    elif request.form['Password'] != request.form['Password_Check']:
        flash("Passwords must match!")

    if '_flashes' in session:
        flash("Please correct the above errors and resubmit.")
        return redirect('/')
    else:
        flash("Thank you for submitting your information!")
        return redirect('/')

app.run(debug=True)
