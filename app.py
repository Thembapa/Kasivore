from flask import Flask, render_template
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


## Global variebles
GID = "67980471209-beho86sujost0htubv5iti646qeal2ab.apps.googleusercontent.com"


def getallusernames():
    matchdoc = []
    matchdoc = ['Themba', 'thembapa@gmail.com', 'Mandy', 'test']
    return matchdoc


@app.route('/')
def index():
    userlist = json.dumps(getallusernames())
    print(userlist)
    return render_template('index.html', userNames=userlist, GID = GID)


if __name__ == "__main__":
    app.run()
