from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key ='testsecretkey'


@app.route('/')         
def index():
    if "increment" not in session:
        if "count" not in session:     
            session["count"]= 1
        else:
            session["count"] += 1
        if "views" not in session:     
            session["views"]= 1
        else:
            session["views"] += 1
        return render_template("index.html")
    else:
        if "count" not in session:     
                session["count"]= 0
        else:
            session["count"] += session["increment"]
            session["views"] += 1
            return render_template("index.html")
    

@app.route('/2')         
def doubles():
    if "count" not in session:
        session["count"]= 0
    else:
        session["count"] += session["increment"]
    
    return render_template("index.html")

@app.route('/increment', methods=['POST'])         
def increment():
    print(request.form)
    if "increment" not in session:
        session["increment"]= int(request.form["increment"])
    else:
        session["increment"] += int(request.form["increment"])
    print(session["increment"])
    return redirect("/")

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')
# @app.route('/checkout', methods=['POST'])         
# def checkout():
#     print(request.form)
#     return render_template("checkout.html")

# @app.route('/fruits')         
# def fruits():
#     return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    