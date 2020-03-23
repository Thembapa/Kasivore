from flask import Flask, render_template, session, redirect, request
import json
from passlib.hash import sha256_crypt
# set the project root directory as the static folder, you can set others.
import KasivoreData
import kasivoreCommon

app = Flask(__name__, static_url_path='')
app.secret_key = "kasivoretest"

## Global variebles
GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"
menubuttons = {'Home': '/', 'About': '/About', 'Legal': '/Legal', 'Pay': '/Pay', 'Contact': '/Contact', 'Help': 'Help'}


##App functions
def IsSignedIn():
    if 'CurrentUser' in session:
        return True
    else:
        return False


### Application Fuctions###
def changetolowercase(Distionary):
    outdict = {}
    for k in Distionary:
        outdict[k.lower()] = Distionary[k]

    return outdict


def get_user(username):
    user_details = {}

    return user_details


def send_WelcomeEmail(user_name, email):
    if 'activatetocken' in session:
        tocken = session['activatetocken']
        print('tocken' + tocken)
        subject = 'Welcome to Kasivore'
        link = 'https://kasivore.com/activate/' + tocken
        Body = 'Please click the link to activate you account: ' + link
        kasivoreCommon.sendmail(subject, Body, email)
        session.pop('activatetocken')
        print('send email to' + email + 'for ' + user_name)


@app.route('/UserNames/<username>')
def getallusernames(username=None):
    currentUser = ""
    DBemails = KasivoreData.pgsql_call_Tablefunction('app', 'fn_getEmails')
    matchdoc = []
    for users in DBemails:
        useremail = str(users[0])
        matchdoc.append(useremail.lower())

    if username is not None:
        if username.lower() in matchdoc:
            currentUser = "Error: In use:  " + username
        else:
            currentUser = ""
    return currentUser


@app.route('/activate/<username>')
def activate(username=None):
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    if username is not None:
        Accountstatus = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_ActivateAccount', {'_userName': username})
        print(Accountstatus)

    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


##HTML pages redirect
@app.route('/Help')
def Help():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    return render_template('Help.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/About')
def About():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    return render_template('About.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Contact')
def Contact():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    return render_template('Contact.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Welcome/<username>/<email>')
def Welcome(username=None, email=None):
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'

    if username is not None and email is not None:
        send_WelcomeEmail(username, email)

    return render_template('Welcome.html', username=username, email=email, ErrorMsq=ErrorMsq, GID=GID,
                           menubuttons=menubuttons, Signup=IsSignUp, profilepicture=profilepicture,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Legal')
def Legal():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    return render_template('Legal.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Pay')
def Pay():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'
    return render_template('Pay.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/')
@app.route('/index')
def index():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        profilepicture = 'Online.png'
        userMenuList = {'Sigout': '/login', 'Profile': '#', 'Customise': '#'}
        loginUrl = '#'

        # test = 'themba'
    # password = sha256_crypt.encrypt(test)
    # print(sha256_crypt.verify(test, password))
    # print(password)
    return render_template('index.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        session.pop('CurrentUser')

    if request.method == 'POST':
        if request.form["hf_Error"] != '':
            ErrorMsq = request.form["hf_Error"]
            print('error:' + ErrorMsq)
            IsSignUp = '1'
            return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                                   profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)

        print(sha256_crypt.encrypt(request.form["txt_pass1"]))
        parameters = {'_usertypeid': '2', '_emailaddress': request.form["txtUser1"],
                      '_userpassword': sha256_crypt.encrypt(request.form["txt_pass1"])}
        CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create', parameters)
        print(CreatedID)
        username = ''
        email = ''
        activatetocken = ''
        Welcomepage = '/Welcome/'
        for id in CreatedID:
            user_id = id[0]
            username = id[1]
            email = id[2]
            session['activatetocken'] = id[3]
            Welcomepage = Welcomepage + username + '/' + email
        print('Userid: ' + str(user_id))
        if user_id != '0':
            return redirect(Welcomepage)
    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/login', methods=['GET', 'POST'])
def Login():
    profilepicture = 'login.png'
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        session.pop('CurrentUser')

    if request.method == 'POST':
        if request.form["hf_Error1"] != '':
            ErrorMsq = request.form["hf_Error1"]
            print('error:' + ErrorMsq)
        else:
            parameters = {'_userName': request.form["txtUser"]}
            CurrentUser = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_getUser', parameters)
            print(CurrentUser)
            password = ''
            for user in CurrentUser:
                password = user[2]

            try:
                print(sha256_crypt.verify(request.form["txt_pass"], password))
                if sha256_crypt.verify(request.form["txt_pass"], password):
                    for values in CurrentUser:
                        print(values[10])
                        if values[10] != '0':
                            session['CurrentUser'] = CurrentUser
                            print('You are loged in: ' + str(CurrentUser))
                            return redirect('/')
                        else:
                            ErrorMsq = 'Account not active!'
                else:
                    ErrorMsq = 'No match found!'

            except Exception as e:
                print(e)
                ErrorMsq = 'No match found!'

    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                           profilepicture=profilepicture, userMenuList=userMenuList, loginUrl=loginUrl)


if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="192.168.178.1", port=8080)
    app.run()
