from flask import request,  abort, Blueprint
from db.cert import Provider
from models.cert import Cert
cert = Blueprint('cert', __name__)

@cert.route('/cert', methods=["POST"])
def add_cert():
    body = request.json
    answer = Provider.create_task(body)
    return str(answer)

@cert.route('/cert/check', methods=["POST"])
def check_cert():
    body = request.json
    answer = Provider.get_cert_id(body)
    if answer == {} or answer is None:
        return "Certificate not found", 404
    else:
        cert = Cert(body['data'])
        check = Cert.check_expired_time(cert)
        if not check:
            return "Certificate is not valid (outdated or blocked)", 400
    return "Certificate is valid"