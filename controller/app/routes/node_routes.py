from flask import Blueprint
from db.node import Provider
import json
node = Blueprint('node', __name__)


@node.route('/nodes', methods=["GET"])
def get_nodes():
    from bootstraping import valid_ips
    Provider.update_status(valid_ips)
    answer = Provider.get_nodes({})
    return json.dumps(answer)

