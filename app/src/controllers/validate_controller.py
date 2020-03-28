# from flask import render_template
import base64
from flask import session
from flask import request
from flask.views import MethodView
from src.services.user import UserService
from src.services.validation import ValidationService

class ValidateController(MethodView):
    def __init__(self):
        self.user_service = UserService()
        self.validation_service = ValidationService()

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        print(session["username"])

        # 1. Get the embedding from DB using session["username"]
        user_embeddings = self.user_service.get_user_embeddings(session["username"])

        if data:
            # Decode the image
            image = base64.b64decode(data)

            # 2. Generate the embeddings for the image
            embeddings = self.validation_service.get_embeddings(image)

             # 3. Compare the embeddings
            dists = [[(e1 - e2).norm().item() for e2 in embeddings] for e1 in user_embeddings]

            print(f"DISTANCE: {dists}")
            
            # Only for testing purposes. The image is saved in the container
            # with open("image.png", "wb") as f:
            #     f.write(content)

            # TODO:
            # 4. Return "Ok" if the embeddings matches, otherwise, return nothing ("", 204)
        else:
            print("NO DATA")

        return "", 204