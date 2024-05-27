from flask import jsonify
from . import bp

@bp.route('/route1', methods=['GET'])
def get_route1():
    return jsonify({'message': 'This is route 1'})