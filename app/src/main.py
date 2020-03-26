from pathlib import Path
from flask import Flask
# from flask_bootstrap import Bootstrap

from controllers.login_controller import LoginController

templates_path = Path(Path.cwd(), "src", "templates")

app = Flask(__name__, template_folder = templates_path)
# Bootstrap(app)

app.add_url_rule("/login", view_func=LoginController.as_view("Login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)