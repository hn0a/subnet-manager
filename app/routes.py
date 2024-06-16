from flask import Blueprint, request, jsonify, render_template

main = Blueprint('main', __name__)

subnets = {}

@main.route('/')
def index():
    return render_template('index.html', subnets=subnets.values())

@main.route('/subnets', methods=['GET', 'POST'])
def manage_subnets():
    if request.method == 'POST':
        data = request.get_json()
        subnets[data['id']] = data
        return jsonify(data), 201
    return jsonify(list(subnets.values()))

@main.route('/subnets/<int:subnet_id>', methods=['PUT', 'DELETE'])
def modify_subnet(subnet_id):
    if request.method == 'PUT':
        if subnet_id in subnets:
            data = request.get_json()
            subnets[subnet_id].update(data)
            return jsonify(subnets[subnet_id])
        return jsonify({"error": "Subnet not found"}), 404
    elif request.method == 'DELETE':
        if subnet_id in subnets:
            del subnets[subnet_id]
            return '', 204
        return jsonify({"error": "Subnet not found"}), 404
