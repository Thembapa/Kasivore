from flask import Flask, render_template
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


## Global variebles
GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"
menubuttons = [{'ButtonName': 'HOME', 'ButtonURL': '/0'}, {'ButtonName': 'INDEX', 'ButtonURL': '/all'},
               {'ButtonName': 'CONTROL', 'ButtonURL': '/control'}, {'ButtonName': 'REGISTER', 'ButtonURL': '/register'}]

@app.route('/UserNames/<username>')
def getallusernames(username = None):
    currentUser = ""
    matchdoc = ['Themba', 'thembapa@gmail.com', 'Mandy', 'test']

    if username is not None:
        if username.lower() in (name.lower() for name in matchdoc):
            currentUser = "Error: Email already in use " + username
        else:
            currentUser = ""
    return currentUser


@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/login')
def Login():
    return render_template('LogIn.html', GID = GID)


if __name__ == "__main__":
    app.run()
