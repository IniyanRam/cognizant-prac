from flask import Flask
from config import Config
from courses.routes import courses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def resource_not_found(e):
        return {"status": "error", "message": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(e):
        return {"status": "error", "message": "Internal Server Error"}, 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
