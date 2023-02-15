import traceback
import uuid
import sys

from flask import Flask, render_template, url_for, request, redirect, session, make_response, send_from_directory
import flask.json
import gevent.pywsgi


def get_abslute_path(subfolder, path):
    if subfolder is None:
        return app.root_path
    else:
        return app.root_path + subfolder + path



app = Flask(__name__)
app.jinja_env.globals.update(get_abslute_path=get_abslute_path)
#app.config["SECRET_KEY"] = secrets.token_urlsafe(7)


@app.route("/")

@app.route("/login")
def login():
    return "Not yet implemented."


if __name__ == "__main__":
    #http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    #http_server.serve_forever()
    app.run(debug=True)
