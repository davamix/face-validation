from pathlib import Path
from flask import Flask

from controllers.login_controller import LoginController
from controllers.validate_controller import ValidateController
from controllers.main_controller import MainController

from services.configuration import ConfigurationService
from services.validation import ValidationService

# Downloading model parameters if needed
ValidationService()

print("Parameters downloaded")

templates_path = Path(Path.cwd(), "src", "templates")

app = Flask(__name__, template_folder = templates_path)
app.secret_key = b"session_secret_key" # Configure a secret key in order use session[]

app.add_url_rule("/login", view_func=LoginController.as_view("login"))
app.add_url_rule("/validate", view_func=ValidateController.as_view("validate"))
app.add_url_rule("/main", view_func=MainController.as_view("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)