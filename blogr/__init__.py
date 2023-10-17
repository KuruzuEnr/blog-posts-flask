from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #crear aplcoiacion
    app=Flask(__name__)
    
    #cargar config
    app.config.from_object('config.Config')
    db.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor=CKEditor(app)

    import locale
    locale.setlocale(locale.LC_ALL, 'es_ES')

    #registrar vista
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)
    
    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User,Post

    #migracion de modelos de models
    with app.app_context():
        db.create_all()



    return app