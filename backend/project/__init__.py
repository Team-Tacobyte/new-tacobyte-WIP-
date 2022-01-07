from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def page_not_found(e):
    return render_template('not-found.html'), 404


def create_app():
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)

    # make this in a .env file for more security
    socket_location = "/opt/lampp/var/mysql/mysql.sock"
    app.config["SECRET_KEY"] = "secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:rootpass@localhost:3306/tacobyte"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Bio

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        print("ok")
        db.create_all()
        db.session.commit()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
