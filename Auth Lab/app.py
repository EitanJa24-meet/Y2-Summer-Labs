from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCsYbkxcCc3ujAuViYFFTmb8qwSU3GhBtM",
  "authDomain": "auth-lab-ej.firebaseapp.com",
  "projectId": "auth-lab-ej",
  "storageBucket": "auth-lab-ej.appspot.com",
  "messagingSenderId": "499286627230",
  "appId": "1:499286627230:web:c67e9f9536cee8591f3c8f",
  "databaseURL":""}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    try:
        session['user'] = auth.create_user_with_email_and_password(email, password)
        session['quotes'] = []
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        return redirect(url_for('thanks'))
  else:
    return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    try:
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        session['quotes'] = []
        return redirect(url_for('home'))
    except Exception as e:
      print(e)
      return redirect(url_for('display'))
  else:
    return render_template("signin.html")

  # If the method is 'POST' take the inputs and signin the user with email & password.

@app.route('/home')
def home():
  return render_template("home.html")

@app.route('/thanks')
def thanks():
  return render_template("thanks.html")

@app.route('/display')
def display():
  return render_template("display.html")

@app.route('/signout', methods=['POST'])
def signout():
  session['user'] = None
  auth.current_user = None
  return redirect(url_for('signin'))

if __name__ == '__main__':
  app.run(debug=True)