import json

from bottle import Bottle, route, run, template, static_file
import waitress
app = Bottle()


## Global variebles
GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"


@app.route('/css/<filename>')
def server_static(filename):
    root = './css'
    return static_file(filename, root=root)


@app.route('/Scripts/<filename>')
def server_static(filename):
    root = './Scripts'
    return static_file(filename, root=root)


@app.route('/images/<filename>')
def server_static(filename):
    root = './images'
    return static_file(filename, root=root)

@app.route('/images/icons/<filename>')
def server_static(filename):
    root = './images/icons'
    return static_file(filename, root=root)


def GetAllUserNames():
    matchdoc = []
    matchdoc = ['Themba', 'thembapa@gmail.com', 'Mandy', 'test']
    return matchdoc


@app.route('/Home')
def home():
    UserList = json.dumps(GetAllUserNames())
    print(UserList)
    # return template('Index.html', userNames=UserList)
    return template('views/Home', userNames=UserList)


@app.route('/')
def index():
    
    UserList = json.dumps(GetAllUserNames())
    print(UserList)
    #return template('Index.html', userNames=UserList)
    return template('views/index', userNames=UserList,GID = GID)
waitress.serve(app, listen='*:9999')