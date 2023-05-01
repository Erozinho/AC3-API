from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config ['SECRET KEY'] = 'API123'

    from website.registrar import registrar
    from website.registros import registros
    from website.deletar import apagar

    app.register_blueprint(registrar, url_prefix="/")
    app.register_blueprint(registros, url_prefix="/")
    app.register_blueprint(apagar, url_prefix="/")


    return app
