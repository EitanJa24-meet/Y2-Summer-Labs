from flask import Flask, render_template,url_for,redirect,request
import random

app = Flask(__name__,
template_folder='templates',
static_folder='static')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        birthmonth = request.form['Birthmonth']
        return redirect(url_for('fortune',
            BM = birthmonth))


@app.route('/fortune/<BM>', methods=['GET', 'POST'])
def fortune(BM):
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
    num = len(BM)-1
    if num > 13:
        fortune_num = "!!please pick a month that has less than 13 characters!!"
    else:
        fortune_num = fortunes[num]

    return render_template("fortune.html", Fortune = fortune_num)


if __name__ == '__main__':
    app.run(debug=True)



