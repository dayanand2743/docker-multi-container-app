from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route('/item', methods=['POST'])
def create_item():
    item_id = request.json.get('id')
    item_name = request.json.get('name')
    data[item_id] = item_name
    return jsonify({"message": "Item created", "item": {item_id: item_name}}), 201

@app.route('/item/<int:item_id>', methods=['GET'])
def read_item(item_id):
    item_name = data.get(item_id)
    if not item_name:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({item_id: item_name}), 200

@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item_name = request.json.get('name')
    if item_id not in data:
        return jsonify({"error": "Item not found"}), 404
    data[item_id] = item_name
    return jsonify({"message": "Item updated", "item": {item_id: item_name}}), 200

@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in data:
        return jsonify({"error": "Item not found"}), 404
    del data[item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
