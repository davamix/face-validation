# from flask import render_template
import base64
from flask import session
from flask import request
from flask.views import MethodView
from src.services.user import UserService

class ValidateController(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        print(session["username"])

        # TODO: 
        # 1. Get the embedding from DB using session["username"]
        user = self.user_service.get_user(session["username"])
        # 2. Generate the embedding for the image
        # 3. Compare the embeddings
        # 4. Return "Ok" if the embeddings matches, otherwise, return nothing ("", 204)

        if data:
            content = base64.b64decode(data)
            
            # Only for testing purposes. The image is saved in the container
            with open("image.png", "wb") as f:
                f.write(content)

        else:
            print("NO DATA")

        return "", 204