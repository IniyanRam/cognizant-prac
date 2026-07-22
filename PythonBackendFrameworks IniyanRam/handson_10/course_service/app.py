from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/courses/<id>')
def get_course(id): return jsonify({'id': id, 'name': 'Course ' + id})
if __name__ == '__main__': app.run(port=5001)
