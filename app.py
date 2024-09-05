from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!!!! integração"

@app.route('/payload', methods=['POST'])
def webhook():
    if request.method == 'POST':
        subprocess.call(['/var/www/flaskapp/deploy.sh'])
        return 'Deploy initiated', 200
    else:
        return 'Invalid method', 400

if __name__ == '__main__':
    app.run(debug=True)
