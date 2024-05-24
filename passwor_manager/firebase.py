# firebase.py

import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

firebase_config = {
    "apiKey": os.getenv("apikey"),
    "authDomain": os.getenv("authDomain"),
    "projectId": os.getenv("projectId"),
    "storageBucket": os.getenv("storageBucket"),
    "messagingSenderId": os.getenv("messagingSenderId"),
    "appId": os.getenv("appId"),
    "measurementId": os.getenv("measurementId"),
    "databaseURL": os.getenv("databaseURL")
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
