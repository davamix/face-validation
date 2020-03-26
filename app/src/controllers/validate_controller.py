from flask import render_template
from flask import request
from flask.views import MethodView

class ValidateController(MethodView):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        data = request.get_json()

        if data:
            print(f"DATA: {data}")
        else:
            print("NO DATA")

        return "", 204