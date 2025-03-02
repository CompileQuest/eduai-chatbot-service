from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.chatbot_routes import chatbot_bp
from app.utils.db import db
from app.models.feedback import Feedback
from app.models.user import User  
from app.config import SQLALCHEMY_DATABASE_URI



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Only if you want to auto-create tables

    app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
