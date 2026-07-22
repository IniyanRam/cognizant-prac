from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

courses_list = []
course_id_counter = 1

def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def list_courses():
    return jsonify(courses_list)

@courses_bp.route('/', methods=['POST'])
def create_course():
    global course_id_counter
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
    
    # Validate required fields
    if 'name' not in data or 'code' not in data or 'credits' not in data:
        return jsonify({'status': 'error', 'message': 'Missing fields name, code, or credits'}), 400
    
    new_course = {
        'id': course_id_counter,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }
    course_id_counter += 1
    courses_list.append(new_course)
    
    return make_response_json(new_course, 201)

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400

    course['name'] = data.get('name', course['name'])
    course['code'] = data.get('code', course['code'])
    course['credits'] = data.get('credits', course['credits'])

    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    global courses_list
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if not course:
        return jsonify({'status': 'error', 'message': 'Course not found'}), 404
        
    courses_list = [c for c in courses_list if c['id'] != course_id]
    return make_response_json({'message': 'Deleted'}, 200)
