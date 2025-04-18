from flask import Flask

app = Flask(__name__)


app.secret_key = 'supersecretkey_123456'  

from app import routes










