from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sort', methods=['POST'])

def sort_integers():
    try:
        data = request.get_json()
        arr = data['arr']

        if not isinstance(arr, list):
            return jsonify({'error': 'Input must be a list'}), 400

        for num in arr:
            if not isinstance(num, int):
                return jsonify({'error': 'All elements must be integers'}), 400

        if len(arr) > 1000:
            return jsonify({'error': 'Input array size exceeds the limit (1000)'}), 400

        sorted_arr = sorted(arr, key=lambda x: bin(x).count('1'))
        return jsonify({'sorted_arr': sorted_arr}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
