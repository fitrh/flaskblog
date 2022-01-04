import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
DOTENV = os.path.join(BASE_DIR, ".env")
load_dotenv(DOTENV)
DB = {
    "driver": os.getenv("DB_DRIVER"),
    "name": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "pass": os.getenv("DB_PASS"),
}
DB_AUTH = f"{DB['user']}:{DB['pass']}@{DB['host']}"
DB_URI = f"{DB['driver']}://{DB_AUTH}/{DB['name']}"

app = Flask(__name__)
app.config["SECRET_KEY"] = "f7b3ed1c6060bdb873a6001735ea9914"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CKEDITOR_FILE_UPLOADER"] = "/post/upload/images"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASS")
mail = Mail(app)


from flaskblog import routes
