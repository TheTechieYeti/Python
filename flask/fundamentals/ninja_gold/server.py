from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime
app = Flask(__name__)  
app.secret_key ='testsecretkey'

@app.route('/')         
def index():
    if "gold"  and 'activities' and 'time' not in session:
        session["gold"] = 0
        session["activities"] = ""
        session["time"] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])         
def process():
    location = request.form["building"]
    dt = datetime.now().strftime('%y/%m/%d %I:%m %p')
    session["time"] = dt
    if location == "farm":
        gold_this_turn = random.randint(10,20)
    if location == "cave":
        gold_this_turn = random.randint(5,10)
    if location == "house":
        gold_this_turn = random.randint(2,5)
    if location == "casino":
        gold_this_turn = random.randint(-50,50)
    session["gold"] += gold_this_turn
    if gold_this_turn >= 0:
        new_message = f"<p class = 'text-success'> Yay you won {gold_this_turn} from {location}. {dt}</p>"
        session["activities"] += new_message
    elif gold_this_turn <0:
        new_message = f"<p class = 'text-danger'>Bummer dude. You lost {gold_this_turn} from {location}. {dt}</p>"
        session["activities"] += new_message
    # dt = datetime.now()
    # ts = datetime.timestamp(dt)
    # session["time"] = ts
    return redirect('/')




@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    