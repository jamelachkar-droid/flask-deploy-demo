from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de données en mémoire (liste d'items factices)
items = [
    {"id": 1, "name": "Apple", "price": 1.20},
    {"id": 2, "name": "Banana", "price": 0.50},
    {"id": 3, "name": "Cherry", "price": 3.00},
]

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World!"}), 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items}), 200

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Le champ 'name' est obligatoire"}), 400
    
    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "price": data.get("price", 0.0),
    }
    items.append(new_item)
    return jsonify({"message": "Item ajouté avec succès", "item": new_item}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)