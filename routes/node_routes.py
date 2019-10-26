from flask import request,  abort, Blueprint
from db.node import Provider
import json
node = Blueprint('node', __name__)

@node.route('/nodes', methods=["GET"])
def get_nodes():
    answer = Provider.get_nodes({})
    return json.dumps(answer)

