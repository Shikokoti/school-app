from flask import Flask

#Create a flask application instance
app = Flask (__name__)

#added a app route using the decorator @app.route
@app.route('/')
def index ():
    return "<p> Hello World </p>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)