# cheapskate-backend

This is part of the
[fullstack-cheapskate](https://github.com/peterprescott/fullstack-cheapskate)
project.

- A Flask backend that runs on PythonAnywhere.com. (Tick).
- With a webhook that means we have CI/CD in sync with the Github repo.
  (Tick).
- With OpenAPI documentation.
- With proper authentication.
- With a database connection that defaults to SQLite.
- But written so you could switch in something more robust.
- With a Dockerfile that you can get it running with.

## Github webhook for PythonAnywhere CI/CD

- PythonAnywhere dashboard -> Web -> Add a new web app -> Flask.

The app path is `/home/cheapskate/mysite/flask_app.py`.

- Github repo -> Settings -> Webhooks -> Add webhook.

Endpoint: `https://cheapskate.pythonanywhere.com/git`
