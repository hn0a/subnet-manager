from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

subnets = []

@app.route('/')
def index():
    return render_template('index.html', subnets=subnets)

@app.route('/subnets', methods=['GET'])
def get_subnets():
    return jsonify(subnets)

@app.route('/subnets', methods=['POST'])
def add_subnet():
    subnet = request.json
    subnets.append(subnet)
    return jsonify(subnet), 201

@app.route('/subnets/<int:id>', methods=['PUT'])
def update_subnet(id):
    subnet = next((s for s in subnets if s['id'] == id), None)
    if subnet is None:
        return jsonify({'error': 'Subnet not found'}), 404
    subnet['name'] = request.json.get('name', subnet['name'])
    subnet['cidr'] = request.json.get('cidr', subnet['cidr'])
    return jsonify(subnet)

@app.route('/subnets/<int:id>', methods=['DELETE'])
def delete_subnet(id):
    global subnets
    subnets = [s for s in subnets if s['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0')
