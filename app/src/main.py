from pathlib import Path
from flask import Flask

from controllers.login_controller import LoginController
from controllers.validate_controller import ValidateController

from database import Database

templates_path = Path(Path.cwd(), "src", "templates")

app = Flask(__name__, template_folder = templates_path)
app.secret_key = b"session_secret_key"

app.add_url_rule("/login", view_func=LoginController.as_view("Login"))
app.add_url_rule("/validate", view_func=ValidateController.as_view("Validate"))

# Initialize DB
db = Database()
db.initialize_tables()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)