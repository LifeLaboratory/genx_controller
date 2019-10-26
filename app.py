from flask import Flask
from flask_cors import CORS
import config as cfg


def factory():
    app = Flask(__name__)
    CORS(app)
    return app


if __name__ == '__main__':
    app = factory()
    app.run(host=cfg.host, port=cfg.port, threaded=True)
