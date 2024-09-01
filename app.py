
# app.py
from flask import Flask
from session_generator import SessionGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return 'Session Generator is running!'

if __name__ == '__main__':
    SessionGenerator().start()
    app.run(port=8080)
