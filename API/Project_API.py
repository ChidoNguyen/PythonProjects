from flask import Flask

app = Flask(__name__)

#!! self reminder -> windows cmd requires "python3 -m flask run" to work !!
@app.route('/')
def home_page():
    return "<p>Hello World!</p>"