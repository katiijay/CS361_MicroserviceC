from app import app
from flask import jsonify, request
from .calls.parkalerts import get_alerts

@app.route('/alerts', methods=['GET'])
def get_park_alerts():
    parkcode = request.args.get('parkcode')
    results = get_alerts(parkcode)
    return jsonify(results)
