from random import randint
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)  
app.secret_key ='testsecretkey'

@app.route('/')         
def index():
    if "num" not in session:     
        print(randint(1,100))    
        session["num"] = randint(1,100)
        session["list"] = list(range(1,101))
        print(session["list"])
        print(session["num"])
            
        return render_template("index.html")
    
    print(session["num"])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
        session["guess"] = int(request.form["guess"])
        print(session["guess"])
        print(type(session["guess"]))
        print(type(session["num"]))
        return redirect('/')

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    


    #     {% if "guess" in session %}
    #     {% if  session["guess"]  >  session["num"]  %}
    #         <p>Too High!</p>
    #     {% elif  session["guess"]  <  session["num"]  %}
    #         <p>Too Low!</p>
    #     <p>You are correct!</p>
    #     {% endif %}
    
    #     {% if  session["guess"]  >  session["num"]  %}
    #         <p>Too High!</p>
    #     {% elif  session["guess"]  <  session["num"]  %}
    #         <p>Too Low!</p>
    #     <p>You are correct!</p>
    #     {% endif %}

    # # c