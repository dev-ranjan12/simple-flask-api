from flask import Flask, jsonify, request

app = Flask(__name__)

data_store = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data_store if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error":"Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item["id"] = len(data_store)+1
    data_store.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data_store if item["id"] == item_id),None)
    if not item:
        return jsonify({"error":"Item not found"}),404
    
    updated_data = request.json
    item.update(updated_data)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data_store
    data_store = [item for item in data_store if item["id"] != item_id]
    return jsonify({"message":"Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)

