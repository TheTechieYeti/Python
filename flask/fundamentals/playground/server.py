from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# The "@" decorator associates this route with the function immediately foll 
@app.route('/play')
def success():
    return render_template("play.html", num = 3, color = "blue")
@app.route('/play/<int:num>')
def boxnum(num):
    return render_template("play.html", num=num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.