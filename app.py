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
##HTML pages redirect
@app.route('/Help')
def Help():
    return render_template('Help.html',)


@app.route('/About')
def About():
    return render_template('About.html',)


@app.route('/Contact')
def Contact():
    return render_template('Contact.html',)


@app.route('/Legal')
def Legal():

    return render_template('Legal.html',)

@app.route('/Pay')
def Pay():
    return render_template('Pay.html',)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',)

@app.route('/login')
def Login():
    if 'CurrentUser' in session:
        s = session['CurrentUser']
        print('you are signed in as: ', s)
    return render_template('LogIn.html', GID = GID)


if __name__ == "__main__":
    app.run(host='192.168.0.194', port=8080)
    #app.run(host='192.168.0.194', port=8080)
