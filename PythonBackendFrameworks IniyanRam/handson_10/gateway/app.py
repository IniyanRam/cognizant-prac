from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
@app.route('/api/courses/<path:path>', methods=['GET','POST','PUT','DELETE'])
def proxy_courses(path): return requests.request(request.method, 'http://localhost:5001/api/courses/' + path).content
@app.route('/api/students/<path:path>', methods=['GET','POST','PUT','DELETE'])
def proxy_students(path): return requests.request(request.method, 'http://localhost:5002/api/students/' + path).content
if __name__ == '__main__': app.run(port=5000)
