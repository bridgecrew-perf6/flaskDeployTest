from http import HTTPStatus
import os
from flask import Flask, Response, send_from_directory

# import pyrebase
# firebaseConfig = {
#   'apiKey': "AIzaSyAaZ9AwAOB0yMnssVI51xuE7stT0g_CB_8",
#   'authDomain': "dappstoreserver.firebaseapp.com",
#   'projectId': "dappstoreserver",
#   'storageBucket': "dappstoreserver.appspot.com",
#   'messagingSenderId': "947027556793",
#   'appId': "1:947027556793:web:d5253f62471076cec99e68",
#   'measurementId': "G-M86B6W0CSZ"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)

# template_dir = os.path.abspath('./react/')
statics_dir = os.path.abspath('./build/')

app = Flask(__name__, static_folder=statics_dir)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    elif path == '':
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return Response(status=HTTPStatus.NOT_FOUND, response="The page does not exist. Error 404.")

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)