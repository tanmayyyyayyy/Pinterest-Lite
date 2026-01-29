#Criação do site > precisa ser "__init__.py"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/comunidade.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)

LoginManager = LoginManager(app)
LoginManager.login_view = "homepage"#Onde o usuário será redirecionado se não tiver login.

from pinterestlite import routes