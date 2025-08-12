from flask import Flask

#Create a flask application instance
app = Flask (__name__)

#added a app route using the decorator @app.route
@app.route('/')
def index ():
    return "<p> Welcome to Tara School </p>"

#adding new routes
@app.route("/courses")
def courses ():
    return "This is the courses page"

#creating path parameters
def course_details():
    return f"This is course: {Computer_Science} "

@app.route("/about")
def about ():
    return "What to know about us"

@app.route("/contact")
def contact():
    return "Contact Us Here"



if __name__ == "__main__":
    app.run(port=5000, debug=True)