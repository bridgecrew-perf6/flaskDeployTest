from flask import Flask
import pyrebase
firebaseConfig = {
  'apiKey': "AIzaSyAaZ9AwAOB0yMnssVI51xuE7stT0g_CB_8",
  'authDomain': "dappstoreserver.firebaseapp.com",
  'projectId': "dappstoreserver",
  'storageBucket': "dappstoreserver.appspot.com",
  'messagingSenderId': "947027556793",
  'appId': "1:947027556793:web:d5253f62471076cec99e68",
  'measurementId': "G-M86B6W0CSZ"
}
firebase = pyrebase.initialize_app(firebaseConfig)

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)