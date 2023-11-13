from flask import Flask, jsonify, request

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-11-13", "heart_rate": 75},
    {"heart_id": 2, "date": "2021-12-14", "heart_rate": 97},
    {"heart_id": 3, "date": "2023-11-15", "heart_rate": 85},
    {"heart_id": 4, "date": "2023-11-16", "heart_rate": 90},
    {"heart_id": 5, "date": "2023-11-16", "heart_rate": 105},
    {"heart_id": 6, "date": "2023-11-16", "heart_rate": 100},
]

@app.route('/heart', methods=['POST'])
def add_heart_record():
    new_record = request.get_json()
    heart_data.append(new_record)
    return jsonify({"message": "Heart record added successfully"}), 201

@app.route('/hearts', methods=['GET'])
def get_all_heart_records():
    return jsonify(heart_data)

@app.route('/heart/<int:heart_id>', methods=['GET'])
def get_heart_record(heart_id):
    record = next((record for record in heart_data if record['heart_id'] == heart_id), None)
    if record:
        return jsonify(record)
    return jsonify({"message": "Heart record not found"}), 404

@app.route('/heart/<int:heart_id>', methods=['PUT'])
def update_heart_record(heart_id):
    record = next((record for record in heart_data if record['heart_id'] == heart_id), None)
    if record:
        updated_record = request.get_json()
        record.update(updated_record)
        return jsonify({"message": "Heart record updated successfully"})
    return jsonify({"message": "Heart record not found"}), 404

@app.route('/heart/<int:heart_id>', methods=['DELETE'])
def delete_heart_record(heart_id):
    global heart_data
    heart_data = [record for record in heart_data if record['heart_id'] != heart_id]
    return jsonify({"message": "Heart record deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
