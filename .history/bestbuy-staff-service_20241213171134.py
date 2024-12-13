from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory staff data
staff = []

@app.route('/staff', methods=['POST'])
def create_staff():
    new_staff = request.json
    staff.append(new_staff)
    return jsonify(new_staff), 201

@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(staff), 200

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    member = next((s for s in staff if s['id'] == id), None)
    if member:
        return jsonify(member), 200
    return jsonify({'error': 'Not Found'}), 404

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    member = next((s for s in staff if s['id'] == id), None)
    if not member:
        return jsonify({'error': 'Not Found'}), 404
    updates = request.json
    member.update(updates)
    return jsonify(member), 200

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    global staff
    staff = [s for s in staff if s['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
