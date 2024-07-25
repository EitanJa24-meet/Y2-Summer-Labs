# importing libraries
from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase

# firebase data
firebaseConfig = {
  "apiKey": "AIzaSyDYIRwbDW3efTmgObZp-Ea2UuHjIyycvpA",
  "authDomain": "idea-platform-y2.firebaseapp.com",
  "storageBucket": "idea-platform-y2.appspot.com",
  "projectId": "idea-platform-y2",
  "messagingSenderId": "553305009222",
  "appId": "1:553305009222:web:e235a9a92622310bbc6e47",
  "databaseURL":"https://idea-platform-y2-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db= firebase.database()

# defining
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

# signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    username= request.form['name']
    try:
      user = auth.create_user_with_email_and_password(email, password)
      session['localId'] = user['localId']
      uid = session.get('localId')
      name = {"name": username}
      db.child("users").child(uid).set(name)
      return redirect(url_for('home'))
    except Exception as e:
        print(e) 
        return redirect(url_for('error'))

  else:
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      session['localId'] = user['localId']
      return redirect(url_for('home'))
    except Exception as e:
        print(e) 
        return redirect(url_for('error'))
  else:
    return render_template('login.html')


@app.route("/home", methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    return redirect(url_for('input'))

  else:  
    return render_template("home.html")

@app.route('/input', methods=['GET', 'POST'])
def input():
  if request.method == 'POST':
    piph = request.form['piph']
    description = request.form['description']
    category = request.form['categories']
    publicity = request.form['publicity']
    try:
      uid = session.get('localId')
      name = db.child('users').child(uid).get().val()
      new_piph = {"name": name['name'],"piph": piph, "description": description, "category": category, "Publicity": publicity}
      db.child('piphs').child(uid).push(new_piph)
      return redirect(url_for('home'))
    except Exception as e:
      print(e)
      return redirect(url_for('error')) 

  else:
    return render_template('input.html')

@app.route('/library', methods=['GET', 'POST'])
def library():
  uid = session.get('localId')
  user_ideas=db.child("piphs").child(uid).get().val()
  if not user_ideas:
    user_ideas = {}
  return render_template("library.html", user_ideas = user_ideas)

@app.route('/signout', methods=['POST'])
def signout():
  session['user'] = None
  auth.current_user = None
  return redirect(url_for('login'))

@app.route('/all', methods=['GET', 'POST'])
def all():
  if request.method == "GET":
    try:
      piphs = db.child('piphs').get().val()  
      return render_template("all.html",piphs=piphs, category='All')
    except Exception as e:
      print(e)
      return redirect(url_for('error'))
  else:
    piphs = db.child('piphs').get().val()  
    category = request.form['categories']
    return render_template("all.html",piphs=piphs, category=category)




@app.route("/error")
def error():
  return render_template('error.html')


# running the code
if __name__ == '__main__':
  app.run(debug=True)