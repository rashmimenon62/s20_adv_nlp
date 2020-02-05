from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

print("AKFJHAKSFHJAKSJHFKAJSHFKAJh")
print(db)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '98172439817230aowfuha'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://nlpuser:nlpuserpassword@localhost:3306/gw_nlp?charset=utf8'

    db.init_app(app)

    print(db)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .reuters_docs import reuters_docs as reuters_docs_blueprint
    app.register_blueprint(reuters_docs_blueprint)

    return app
