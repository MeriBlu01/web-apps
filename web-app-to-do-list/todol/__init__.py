# Indicate that the package was made

# Import Flask library
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import DeclarativeBase

'''
class Base(DeclarativeBase):
    pass
'''

# Create SQLAlchemy's instance
db = SQLAlchemy()


def create_app():
    # Variable to save the application using the Flask instance
    app = Flask(__name__)

    # App config
    app.config.from_mapping(
    DEBUG = True,
    SECRET_KEY = 'dev',
    # Config the SQLite database, relative to the app instance folder
    SQLALCHEMY_DATABASE_URI = "sqlite:///usuarios.db"
    )

    # Initialize the app with the extension
    db.init_app(app)

    # Register Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    # With the following the models would be sent to the already created DBs
    with app.app_context():
        db.create_all()

    return app