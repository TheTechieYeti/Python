from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Render and 8x8 checkerboard
@app.route('/<int:rows>')
def rows(rows = 8, ):
    return render_template("rows.html", rows = rows,)

# @app.route('/<int:rows>/<int:cols>')
# def rows_cols(rows, cols):
#     return render_template('rows_cols.html', rows = rows, cols = cols)

# @app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
# def rows_cols_colors(rows, cols, color1, color2):
#     return render_template('rows_cols_colors.html', rows = rows, cols = cols, color1 = color1, color2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

