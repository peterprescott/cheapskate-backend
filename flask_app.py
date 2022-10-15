import os
import git
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/cicd')
def cicd():
    return 'Really really working!'


@app.route('/git', methods=['GET','POST'])
def pull():
    repo = git.Repo(os.path.join('~','cheapskate-backend'))
    repo.remotes.origin.pull()
    return 'Updated'
