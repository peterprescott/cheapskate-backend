import os
import git
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/cicd')
def cicd():
    return 'Maybe maybe working!'


@app.route('/git', methods=['GET','POST'])
def pull():
    repo = git.Repo(os.path.join('~','cheapskate-backend'))
    repo.remotes.origin.pull()
    return 'Updated'
