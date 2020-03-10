from flask import Flask, render_template, session
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
app.secret_key = "kasivoretest"


## Global variebles
GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"
menubuttons = [{'ButtonName': 'HOME', 'ButtonURL': '/0'}, {'ButtonName': 'INDEX', 'ButtonURL': '/all'},
               {'ButtonName': 'CONTROL', 'ButtonURL': '/control'}, {'ButtonName': 'REGISTER', 'ButtonURL': '/register'}]


### Application Fuctions###
def changetolowercase(Distionary):
    outdict = {}
    for k in Distionary:
        outdict[k.lower()] = Distionary[k]

    return outdict

@app.route('/UserNames/<username>')
def getallusernames(username = None):
    currentUser = ""
    matchdoc = {'Themba@something.com': 'Themba Somthing', 'thembapa@gmail.com': 'Themba Pakula',
                'Mandy@love.com': 'Mandy Pakula', 'test@test.com': 'Test forever'}

    matchdoc = changetolowercase(matchdoc)

    if username is not None:
        if username.lower() in (name.lower() for name in matchdoc):
            currentUser = "Error: Email already in use " + username
            session['CurrentUser'] = matchdoc[username.lower()]
        else:
            currentUser = ""
    return currentUser


@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/login')
def Login():
    if 'CurrentUser' in session:
        s = session['CurrentUser']
        print('you are signed in as: ', s)
    return render_template('LogIn.html', GID = GID)


if __name__ == "__main__":
    app.run(port=8080)
