from flask import Flask
from flask_cors import CORS
import config as cfg
from routes.cert_routes import cert
from routes.node_routes import node
import threading
import bootstraping

def factory():
    app = Flask(__name__)
    CORS(app)
    register_api(app)
    return app


def register_api(app):
    app.register_blueprint(cert)
    app.register_blueprint(node)

def flask_run():
    app.run(host=cfg.host, port=cfg.flask_port, threaded=True)

if __name__ == '__main__':
    app = factory()
    threading.Thread(target=flask_run).start()
    bootstraping.bootstrap_run()

