from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    status = data.get('status')
    user_id = data.get('user_id')
    email = data.get('college_email')
    roll_number = data.get('college_roll_number')
    numbers = data.get('numbers', [])
    alphabets = data.get('alphabets', [])
    
    response = {
        'status': status,
        'user_id': user_id,
        'college_email': email,
        'college_roll_number': roll_number,
        'numbers': numbers,
        'alphabets': alphabets
    }
    return jsonify(response)

@app.route('/api/data', methods=['GET'])
def get_data():
    operation_code = '12345'
    return jsonify({'operation_code': operation_code})

if __name__ == '__main__':
    app.run(debug=True)
