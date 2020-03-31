import io
import base64
from PIL import Image
from flask import session
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask.views import MethodView
from services.user import UserService
from services.validation import ValidationService


class ValidateController(MethodView):
    def __init__(self):
        self.user_service = UserService()
        self.validation_service = ValidationService()

    def get(self):
        return render_template("face.html", title="Login")

    def post(self):
        print("Redirecting...")
        print(request.endpoint)
        if request.endpoint != "main":
            return redirect(url_for("main"))
        
        # dist = None
        # data = request.get_json()
        # print(f"# Username: {session['username']}")

        # # 1. Get the embedding from DB using session["username"]
        # user_embeddings = self.user_service.get_user_embeddings(session["username"])
        # if user_embeddings is None:
        #     print("# User does not exists or has no embeddings")

        # if data:
        #     # Decode the image
        #     image_bytes = base64.b64decode(data)

        #     image = Image.open(io.BytesIO(image_bytes))
        #     image = image.convert(mode="RGB")

        #     # 2. Generate the embeddings for the image
        #     embeddings = self.validation_service.get_embeddings(image)

        #     if embeddings is None:
        #         print("# No face detected")
        #     else:
        #         # 3. Compare the embeddings
        #         # dists = [[(e1 - e2).norm().item() for e2 in embeddings] for e1 in user_embeddings]
        #         dist = self.validation_service.get_distance(user_embeddings, embeddings)
                
        #         print(f"DISTANCE: {dist}")


        #     # Only for testing purposes. The image is saved in the container
        #     # with open("image.png", "wb") as f:
        #     #     f.write(content)

        #     # TODO:
        #     dist = 0
        #     if dist is not None and dist < 1:
        #         print("Redirecting...")
        #         return render_template("login_username.html", title="Login")
        # else:
        #     print("# NO DATA")

        # # 4. Return "Ok" if the embeddings matches, otherwise, return nothing ("", 204)
        
        # return "", 204