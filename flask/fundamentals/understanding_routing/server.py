from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def success():
    return "Dojo!"
@app.route('/say/<string:name>')
def hello(name):
    return f"Hi {name}!"
@app.route('/repeat/<int:num>/<string:word>') #BILL #how would I ensure that the user is inputing an integer? I can't convert a string to an integer? 
def thing(num, word):
    if type(num) == str:
        return "Invalid User Input"
    return word * num
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

#### Sensei Bonus: Ensure that if the user types in any route other than the ones specified, they receive and error message saying "Sorry! No response. Try Again"