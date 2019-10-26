from flask import Flask
from flask_cors import CORS
import config as cfg
from routes.cert_routes import cert
from routes.node_routes import node

def factory():
    app = Flask(__name__)
    CORS(app)
    register_api(app)
    return app


def register_api(app):
    app.register_blueprint(cert)
    app.register_blueprint(node)


if __name__ == '__main__':
    app = factory()
    app.run(host=cfg.host, port=cfg.port, threaded=True)
