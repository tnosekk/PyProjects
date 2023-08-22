from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qwerrewq"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import Note, User

    with app.app_context():
        create_database()

    return app


def create_database():
    if not path.exists("website/" + DB_NAME):
        db.create_all()
        print("Created Database!")
