from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}

# Home route
@app.route("/")
def home():
    return jsonify({"message": "User Management API is running!"})

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id]), 200

# POST: Create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(data.get("id"))
    if not user_id:
        return jsonify({"error": "ID is required"}), 400

    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User created", "user": users[user_id]}), 201

# PUT: Update user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

# DELETE: Remove user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)