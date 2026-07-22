from flask import Blueprint, jsonify, request
from extensions import db
from .models import Course, Student, Enrollment, Department

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data, status_code=200):
    return jsonify({'status': 'success', 'data': data}), status_code

@courses_bp.route('/', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return make_response_json([c.to_dict() for c in courses], 200)

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
    
    if 'name' not in data or 'code' not in data or 'credits' not in data:
        return jsonify({'status': 'error', 'message': 'Missing fields name, code, or credits'}), 400
    
    new_course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data.get('department_id')
    )
    db.session.add(new_course)
    db.session.commit()
    
    return make_response_json(new_course.to_dict(), 201)

@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400

    course.name = data.get('name', course.name)
    course.code = data.get('code', course.code)
    course.credits = data.get('credits', course.credits)
    course.department_id = data.get('department_id', course.department_id)

    db.session.commit()
    return make_response_json(course.to_dict(), 200)

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return make_response_json({'message': 'Deleted'}, 200)

@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    course = Course.query.get_or_404(course_id)
    students = Student.query.join(Enrollment).filter(Enrollment.course_id == course_id).all()
    return make_response_json([s.to_dict() for s in students], 200)
