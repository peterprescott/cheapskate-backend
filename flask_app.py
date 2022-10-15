import os
import git
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello_world() -> str:
    """
    Just get started.

    Returns
    -------
    str
        A simple greeting
    """
    return 'Hello from Flask!'


@app.route('/cicd')
def cicd() -> str:
    """
    Check CI/CD status.

    Returns
    -------
    str
        A text string that you might update to prove that it changes.
    """
    return 'Working!'


@app.route('/git', methods=['GET','POST'])
def pull() -> str:
    """
    Trigger git pull.

    Returns
    -------
    str
      Confirmation that update was successful.
    """
    repo = git.Repo(os.path.join('~','cheapskate-backend'))
    repo.remotes.origin.pull()
    return 'Updated'
