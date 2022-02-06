from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)  
app.secret_key ='testsecretkey'

@app.route('/')         
def index():
    return render_template("test_form.html")

@app.route('/submit', methods=["POST"])         
def submit():
    print(request.form)
    session["dojo_location"] = request.form["dojo_location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["name"] = request.form["name"]
    session["comments"] = request.form["comments"]
    return redirect('/display')

@app.route('/display')         
def display():
    return render_template("display.html")

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    