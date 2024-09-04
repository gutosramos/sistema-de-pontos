from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!!!! teste de integração 3"


if __name__ == '__main__':
    app.run(debug=True)
