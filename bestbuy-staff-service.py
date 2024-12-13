import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Environment variables
PORT = int(os.getenv("FLASK_RUN_PORT", 5000))  # Default port is 5000
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

# In-memory staff data
staff = []

# Required fields for staff information
REQUIRED_FIELDS = {"id", "name", "position", "department", "email", "phone"}


def validate_payload(payload):
    """Validate the incoming JSON payload for required fields."""
    missing_fields = REQUIRED_FIELDS - payload.keys()
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, None


@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json  # Get JSON payload
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Validate required fields
    is_valid, error_message = validate_payload(data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Add to in-memory staff list
    staff.append(data)
    return jsonify(data), 201


@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(staff), 200


@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    member = next((s for s in staff if s['id'] == id), None)
    if member:
        return jsonify(member), 200
    return jsonify({'error': 'Staff member not found'}), 404


@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    data = request.json  # Get JSON payload
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    # Find the staff member to update
    member = next((s for s in staff if s['id'] == id), None)
    if not member:
        return jsonify({'error': 'Staff member not found'}), 404

    # Update the staff member with new data
    member.update(data)
    return jsonify(member), 200


@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    global staff
    # Filter out the staff member with the given ID
    updated_staff = [s for s in staff if s['id'] != id]

    if len(updated_staff) == len(staff):  # No staff member was deleted
        return jsonify({'error': 'Staff member not found'}), 404

    staff = updated_staff
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
