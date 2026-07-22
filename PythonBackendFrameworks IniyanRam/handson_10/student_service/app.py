from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
@app.route('/api/students/<id>/enroll', methods=['POST'])
def enroll(id):
    try: response = requests.get('http://localhost:5001/api/courses/1'); response.raise_for_status()
    except requests.exceptions.ConnectionError: return jsonify({'error': 'Service Unavailable'}), 503
    return jsonify({'status': 'enrolled', 'student': id})
if __name__ == '__main__': app.run(port=5002)
