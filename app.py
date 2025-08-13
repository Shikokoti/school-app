from flask import Flask

#Create a flask application instance
app = Flask (__name__)

#added a app route using the decorator @app.route
@app.route('/')
def index ():
    return " Welcome to Tara School"

#adding new routes
@app.route("/courses")
def courses ():
    return "This is the courses page"

#creating path parameters
@app.route("/courses/<course_id>")
def course_details(course_id):
    return f"This is course: {course_id} "

#add a path
@app.route("/courses/<path: course_file>")
def course_file(course_file):
    return f"Currently serving : {course_file}"


@app.route("/about")
def about ():
    return "What to know about us"

@app.route("/contact")
def contact ():
    return "Contact Us Here"



if __name__ == "__main__":
    app.run(port=5000, debug=True)