from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from CI with GitHub Actions by Manukyan'

@app.route('/v2')
def v2():
    return 'Second action'
