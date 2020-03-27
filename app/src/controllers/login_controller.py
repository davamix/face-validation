from flask import session
from flask import render_template
from flask import request
from flask.views import MethodView

class LoginController(MethodView):
    def __init__(self):
        pass

    def get(self):
        return render_template("login_username.html", title="Login")

    def post(self):
        data = request.form["username"]
        session["username"] = data

        return render_template("login_face.html", title="Login", username=data)