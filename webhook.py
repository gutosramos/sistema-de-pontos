from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

@app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        secret = request.headers.get('X-Hub-Signature')
        if not secret or secret != 'your_secret_key':
            abort(403)
        try:
            subprocess.check_call(['/var/www/flaskapp/deploy.sh'])
        except subprocess.CalledProcessError:
            abort(500)
        return 'Deployment complete', 200
    else:
        abort(405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
