from bottle import Bottle, route, run, template, static_file
import waitress
app = Bottle()


@app.route('/css/<filename>')
def server_static(filename):
    root = './css'
    return static_file(filename, root=root)



@app.route('/images/<filename>')
def server_static(filename):
    root = './images'
    return static_file(filename, root=root)

@app.route('/images/icons/<filename>')
def server_static(filename):
    root = './images/icons'
    return static_file(filename, root=root)


@app.route('/')
def index():
    return template('index', test="Themba Pakula")
waitress.serve(app, listen='*:9999')