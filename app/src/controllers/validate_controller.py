from flask import render_template
from flask import request
from flask.views import MethodView
import base64

class ValidateController(MethodView):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        data = request.get_json()

        if data:
            content = base64.b64decode(data)
            
            # Only for testing purposes. The image is saved in the container
            with open("image.png", "wb") as f:
                f.write(content)

        else:
            print("NO DATA")

        return "", 204