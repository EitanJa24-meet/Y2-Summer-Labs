from flask import Flask, render_template
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fortune')
def fortune():
    fortunes = [
    "You will find great success in the near future.",
    "A new opportunity will present itself to you soon.",
    "Someone close to you has good news to share.",
    "Your hard work will soon pay off in unexpected ways.",
    "You will discover a new talent or passion.",
    "A pleasant surprise is waiting for you this week.",
    "Your positive attitude will attract good things.",
    "An old friend will re-enter your life with exciting news.",
    "You will soon embark on a wonderful journey.",
    "Good fortune will come your way in the form of a new friendship.",
    "An unexpected event will bring you joy.",
    "You will achieve your goals sooner than you think.",
    "Watan will haunt you"
]
    
    num = random.randint(0,14)
    fortune_random = fortunes[num]

    return render_template("fortune.html", Fortune = fortune_random)

    
if __name__ == '__main__':
    app.run(debug=True)


