import os
from flask import Flask, render_template, session, redirect, request, send_from_directory, url_for
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json
from passlib.hash import sha256_crypt
# set the project root directory as the static folder, you can set others.
import KasivoreData
import kasivoreCommon
import secrets
import string
from werkzeug.utils import secure_filename

from configfile import TWILIOKEY, TWILIOTOCKEN, TWILIOWHATSAPP, MYWHATSAPP, MYWHATSSMS, TWILIOSMS, GOOGLEID, EMAIL_INFO, MAPS

app = Flask(__name__, static_url_path='')
app.secret_key = "kasivoretest"
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
USER_FOLDERS = 'static/useraccounts/'
app.config['USER_FOLDERS'] = USER_FOLDERS

## Global variebles
# GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"  # Live
GID = GOOGLEID  # test
MAPS_API = 'https://maps.googleapis.com/maps/api/js?key='+ MAPS +'&callback=initAutocomplete'
menubuttons = {'Home': '/', 'About': '/About', 'Legal': '/Legal', 'Pay': '/Pay', 'Service': '/service',
               'Contact': '/Contact', 'Help': 'Help'}

print ('Maps: ' + MAPS_API)
##App functions
def IsSignedIn():
    if 'CurrentUser' in session:
        for user in session['CurrentUser']:
            if user[8] != '' and user[8] is not None:
                session['profilepicture'] = '/useraccounts/' + user[8]
            else:
                session['profilepicture'] = '/images/Profilepictures/login.png'
        return True
    else:
        session['profilepicture'] = '/images/Profilepictures/login.png'
        return False


### Application Fuctions###
def changetolowercase(Distionary):
    outdict = {}
    for k in Distionary:
        outdict[k.lower()] = Distionary[k]

    return outdict


def error_Report(ErrorType, msg):
    
    kasivoreCommon.sendmail(ErrorType, msg, 'themba@kasivore.com')
    


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
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
    if username is not None:
        Accountstatus = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_ActivateAccount', {'_userName': username})
        print(Accountstatus)

    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp, MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


##HTML pages redirect
@app.route('/Help')
def Help():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
    return render_template('Help.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/About')
def About():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
    return render_template('About.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(TWILIOKEY, TWILIOTOCKEN)

    # this is the Twilio sandbox testing number
    from_whatsapp_number = TWILIOWHATSAPP
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_Themba = MYWHATSAPP
    # Sms

    if request.method == 'POST':
        if request.form["hf_Error"] != '':
            ErrorMsq = request.form["hf_Error"]
            print('error:' + ErrorMsq)
            IsSignUp = '1'
        else:
            EmailAdress = request.form["txtemail"]
            infodress = EMAIL_INFO
            Contactperson = request.form["txtname"]
            usermsg = request.form["txtmessage"]
            Body = 'Hi ' + Contactperson + '\n\n Thank you for contacting us. Your input is important to us\n We will get back to you soonest\n\n Kasivore Team'
            kasivoreCommon.sendmail('Kasivore feeback', Body, EmailAdress)
            kasivoreCommon.sendmail('Kasivore feeback', usermsg, infodress)
            ErrorMsq = 'Email sent!!!'

    if 1 == 0:
        client.messages.create(body='We can use this for OTP, From Themba!!',
                               from_=TWILIOSMS,
                               to=MYWHATSSMS)
        # WhatsApp
        client.messages.create(body='Someone clicked on the contact us menu!!!',
                               from_=from_whatsapp_number,
                               to=to_whatsapp_Themba)

    return render_template('Contact.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/WBot', methods=['GET', 'POST'])
def WBot():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    response = ''
    if msg.lower() == 'hi':
        response = '''Welcome to Kasivore \nHow can we help you? \n\n1. New account \n2. Billing \n3. About Us\n99. Main Menu'''
    elif msg.lower() == '1':
        response = '''go to https://kasivore.com  to open a new account
                           '''
    elif msg.lower() == '2':
        response = '''your bill has been sent to you email account
                           '''
    elif msg.lower() == '3':
        response = '''Kasivore is a... thinking...   '''
    elif msg.lower() == '99':
        response = '''Welcome to Kasivore \nHow can we help you? \n\n1. New account \n2. Billing \n3. About Us\n99. Main Menu'''
    else:
        response = '''You made an invilid selection!'\nUse Options below: \n\n1. New account \n2. Billing \n3. About Us\n99. Main Menu'''
    # Create reply
    resp = MessagingResponse()
    resp.message("{}".format(response))

    return str(resp)


@app.route('/Welcome/<username>/<email>')
def Welcome(username=None, email=None):
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'

    if username is not None and email is not None:
        send_WelcomeEmail(username, email)

    return render_template('Welcome.html', username=username, email=email, ErrorMsq=ErrorMsq, GID=GID,MAPS = MAPS_API,
                           menubuttons=menubuttons, Signup=IsSignUp, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Legal')
def Legal():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
    return render_template('Legal.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Pay')
def Pay():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
    return render_template('Pay.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Profile/<formname>', methods=['GET', 'POST'])
@app.route('/Profile', methods=['GET', 'POST'])
def Profile(formname=None):
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    CurrentProfileForm = ''
    username = ''
    passowrd = ''
    userid = 0
    if IsSignedIn():
        userMenuList = {'Sigout': '/login', 'Profile': '/Profile'}
        loginUrl = '#'
        session["CurrentProfileForm"] = 'AccountForm'
        CurrentProfileForm = 'AccountForm'
        CurrentUser = session['CurrentUser']

        for user in CurrentUser:
            username = user[1]
            passowrd = user[2]
            userid = user[0]
        if request.method == 'POST':

            CurrentProfileForm= formname
            if formname == "AccountForm":
                if request.form['hf_ppUpload'] == "1":
                    # Change profile picture
                    try:
                        upload = request.files['ppUpload']
                        filename = secure_filename(upload.filename)

                        filename = username + '/profilepicture/' + filename
                        folder = username + '/profilepicture'
                        #Check if file directory exists, create new folder if not exists
                        if (os.path.isdir(os.path.join(app.config['USER_FOLDERS'], folder))) == False:
                            os.makedirs(os.path.join(app.config['USER_FOLDERS'], folder))

                        upload.save(os.path.join(app.config['USER_FOLDERS'], filename))
                        print('images/' + filename)
                        session['profilepicture'] = '/useraccounts' + '/'+ filename

                        ##Update Database
                        parameters = {'_profilepicture': filename, '_userid': userid}
                        CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create_user', parameters)
                    except Exception as identifier:
                        error_Report('Kasivore uploadError' , str(identifier) )
                    

                elif request.form["txt_pass2"] != '':
                    # change Password
                    print('passowrd 2' +request.form["txt_pass2"])
                    if request.form["hf_Error"] != '':
                        ErrorMsq = request.form["hf_Error"]
                    else:
                        print('Validate password')
                        try:
                            if sha256_crypt.verify(request.form["txtOldPassword"], passowrd):
                                parameters = {'_resettoken': passowrd,
                                              '_userpassword': sha256_crypt.encrypt(request.form["txt_pass1"])}
                                isCreated = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_changepassword',
                                                                                    parameters)
                                print(isCreated)
                                return redirect('/login')
                            else:
                                ErrorMsq = 'No match found!'

                        except Exception as e:
                            print(e)
                            ErrorMsq = 'No match found!'
                else:
                    # change user type
                    print('Radio: ' + request.form["radioService"])
                    parameters = {'_usertypeid': request.form["radioService"], '_userid': userid}
                    CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create_user', parameters)
            elif formname == "Bioform":
                ##Update personal details 
                print('txtbirthday: ' + request.form["txtbirthday"])
                parameters = {'_userid': userid, '_firstname': request.form["txtName"] , '_lastname': request.form["txtSurname"], '_Tell': request.form["txtTell"], '_nationality': request.form["country"], '_idnumber': request.form["txtIDNO"], '_passportnumber': request.form["txtPassport"], '_dateofbirth': request.form["txtbirthday"], '_gender': request.form["Gender"]}
                # txtName , txtSurname ,txtTell,country, txtIDNO, txtPassport,txtbirthday, Gender
                CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create_user', parameters)
            elif formname == "Addressform":
                print('txt_Address1: ' + request.form["txt_Address1"])
                parameters = {'_userid': userid, '_addedby': userid , '_addressestype':1, '_addreslabel':'Home', '_physical1': request.form["txt_Address1"], '_physical2': request.form["txt_Address2"], '_physical3': request.form["txt_Address3"], '_physical4': request.form["txt_Address4"], '_physical5': request.form["txt_Address5"], '_physicalcode': request.form["txt_PostalCode"]}
                # txtName , txtSurname ,txtTell,country, txtIDNO, txtPassport,txtbirthday, Gender
                CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_add_Address', parameters)
            elif formname == "BusinessAddressform":
                print('txt_Address1: ' + request.form["txt_Address1"])
                parameters = {'_userid': userid, '_addedby': userid , '_addressestype':2, '_addreslabel':'Business', '_physical1': request.form["txt_Address1"], '_physical2': request.form["txt_Address2"], '_physical3': request.form["txt_Address3"], '_physical4': request.form["txt_Address4"], '_physical5': request.form["txt_Address5"], '_physicalcode': request.form["txt_PostalCode"]}
                # txtName , txtSurname ,txtTell,country, txtIDNO, txtPassport,txtbirthday, Gender
                CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_add_Address', parameters)
            elif formname == "Businessform":
                ##Update personal details 
                print('txtbirthday: ' + request.form["txtbirthday"])
                parameters = {'_addedby': userid, '_ServiceID': request.form["hf_ServiceID"] , '_companyname': request.form["txtCompanyName"] , '_registrationnumber': request.form["txtReg"], '_typeofservice': request.form["hf_Category"], '_isactive': '1', '_tagline': request.form["txttag"], '_description': request.form["txtcomment"]}
                # txtName , txtSurname ,txtTell,country, txtIDNO, txtPassport,txtbirthday, Gender
                CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_add_serviceprovider', parameters)
            elif formname == "showcaseForm":
                if request.form['hf_imageID'] != "":
                    parameters = { '_addedby': userid, '_isthumbnail': '1', '_ImageID': request.form['hf_imageID']}
                    isSaved = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_add_serviceprovider', parameters)
                elif request.form['hf_ImageUpload'] == "1":
                    # Change profile picture                   
                    upload = request.files['WorkDoneImage']
                    
                    filename = secure_filename(upload.filename)

                    filename = username + '/Showcase/' + filename
                    folder = username + '/Showcase'
                    #Check if file directory exists, create new folder if not exists
                    if (os.path.isdir(os.path.join(app.config['USER_FOLDERS'], folder))) == False:
                        os.makedirs(os.path.join(app.config['USER_FOLDERS'], folder))

                    upload.save(os.path.join(app.config['USER_FOLDERS'], filename))
                    print('images/' + filename)

                    ##Update Database
                    parameters = { '_addedby': userid, '_imageurl': filename, '_imagename': filename}
                    isSaved = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_add_serviceprovider', parameters)
    else:
        return redirect("/login")

    ##Get Fresh Data
    Categories = KasivoreData.pgsql_call_Tablefunction('app', 'fn_gettypesofservices')
   
    parameters = {'_userName': username}
    CurrentUser = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_getUser', parameters)
    session['CurrentUser'] = CurrentUser

    S_parameters = {'_userid': userid}
    serviceprovider = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_get_serviceprovider',S_parameters)
    SampleImages = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_get_SampleImages',S_parameters)
    return render_template('profile.html', CurrentProfileForm=CurrentProfileForm, ErrorMsq=ErrorMsq, GID=GID, MAPS= MAPS_API,Categories = Categories,serviceprovider = serviceprovider,SampleImages = SampleImages,
                           menubuttons=menubuttons, userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/newpassword/<token>', methods=['GET', 'POST'])
def newpassword(token=None):
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        session.pop('CurrentUser')

    if token is not None:
        session['pastoken'] = token

    if request.method == 'POST':
        if request.form["hf_Error"] != '':
            ErrorMsq = request.form["hf_Error"]
            print('error:' + ErrorMsq)
            IsSignUp = '1'

        print(sha256_crypt.encrypt(request.form["txt_pass1"]))
        parameters = {'_resettoken': session['pastoken'],
                      '_userpassword': sha256_crypt.encrypt(request.form["txt_pass1"])}
        isCreated = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_changepassword', parameters)
        print(isCreated)
        return redirect('/login')

    return render_template('NewPassword.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/Signup', methods=['GET', 'POST'])
def Signup():

    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = 'login'
    if IsSignedIn():
        session.pop('CurrentUser')

    if request.method == 'POST':
        if request.form["hf_Error"] != '':
            ErrorMsq = request.form["hf_Error"]
            print('error:' + ErrorMsq)
            IsSignUp = '1'
            return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,
                                   userMenuList=userMenuList, loginUrl=loginUrl)

        print(sha256_crypt.encrypt(request.form["txt_pass1"]))
        parameters = {'_usertypeid': '2', '_emailaddress': request.form["txtUser1"],
                      '_userpassword': sha256_crypt.encrypt(request.form["txt_pass1"])}
        CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create_user', parameters)
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
    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


def passwordresetEmail(email, resetcode):
    subject = 'Kasivore Password Reset'
    link = 'https://kasivore.com/newpassword/' + resetcode
    Body = 'Please follow the link to set a new password: ' + link
    kasivoreCommon.sendmail(subject, Body, email)


def google_sign_up(email, username, temp_password):
    subject = 'Welcome to Kasivore'
    Body = 'Your account details are as follows, Username: ' + username + ' Password: ' + temp_password
    kasivoreCommon.sendmail(subject, Body, email)


@app.route('/service')
def service():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        session.pop('CurrentUser')
    return render_template('/service.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/JsonTest', methods=['GET', 'POST'])
def JsonTest(post=None):
    if request.is_json:
        req = request.get_json()

        JsoanArray = {}
        JsoanArray = {'ServerData': [
            req
        ]

        }
        print(JsoanArray)

        return JsoanArray
    else:
        print("No Json")

    return {'Employees': [
        {
            'firstname': 'Mandy',
            'lastname': 'Sibisi',
            'age': 65
        },
        {
            'firstname': 'Nhlanhla',
            'lastname': 'Dlamini',
            'age': 45
        }
        ,
        {
            'firstname': 'Themba',
            'lastname': 'Pakula',
            'age': 75
        }
        ,
        {
            'firstname': 'Lebo',
            'lastname': 'Zulu',
            'age': 17
        }
    ]}


def googleSignIn(email, username):
    print(email)
    print(username)
    Name = username.split(' ')
    FirstName = Name[0]
    lastname = Name[len(Name) - 1]
    if getallusernames(email) == '':

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))

        parameters = {'_usertypeid': '2', '_emailaddress': email,
                      '_userpassword': sha256_crypt.encrypt(password)}
        CreatedID = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_create_user', parameters)

        for createduser in CreatedID:
            user_id = createduser[0]
            username = createduser[1]
            email = createduser[2]  # Activation tocken
            Accountstatus = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_ActivateAccount',
                                                                    {'_userName': createduser[3]})
            google_sign_up(email, username, password)
            parameters = {'_userName': username}
            CurrentUser = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_getUser', parameters)
            session['CurrentUser'] = CurrentUser

    else:

        parameters = {'_userName': username}
        CurrentUser = KasivoreData.pgsql_call_Tablefunction_P('app', 'fn_getUser', parameters)
        session['CurrentUser'] = CurrentUser
        print('SignIn')


@app.route('/login/<email>/<username>', methods=['GET', 'POST'])
@app.route('/login/<resetpassword>', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def Login(resetpassword=None, email=None, username=None):
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'

    if IsSignedIn():
        session['profilepicture'] = '/images/Profilepictures/login.png'
        session.pop('CurrentUser')
        if 'ProfileProgress' in session:
            session.pop('ProfileProgress')

    if email is not None and username is not None:
        print('Google signIn')
        print(request.method)
        googleSignIn(email, username)
        return redirect('/')

    elif request.method == 'POST':
        if resetpassword is not None:
            if request.form["txtEmailReset"] != '':
                resetCode = KasivoreData.pgsql_get_scalar('app', 'fn_getResetCode',
                                                          {'_emial': request.form["txtEmailReset"]})
                if resetCode == '':
                    ErrorMsq = 'No match found'
                else:
                    passwordresetEmail(request.form["txtEmailReset"], resetCode)
                    Loginlink = '/login'
                    return '''Email sent to reset password <a href=''' + Loginlink + '''>Signin</a>'''
        else:
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

    return render_template('LogIn.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


@app.route('/')
@app.route('/index')
def index():
    userMenuList = {}
    ErrorMsq = ''
    IsSignUp = ''
    loginUrl = '/login'
    if IsSignedIn():
        userMenuList = {'Sigout': 'javascript: sinOut();', 'Profile': '/Profile'}
        loginUrl = '#'
        session['ProfileProgress'] = 'p25'

        # test = 'themba'
    # password = sha256_crypt.encrypt(test)
    # print(sha256_crypt.verify(test, password))
    # print(password)
    return render_template('index.html', ErrorMsq=ErrorMsq, GID=GID, menubuttons=menubuttons, Signup=IsSignUp,MAPS = MAPS_API,
                           userMenuList=userMenuList, loginUrl=loginUrl)


if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="192.168.178.1", port=8080)
    app.run( port=8080)
