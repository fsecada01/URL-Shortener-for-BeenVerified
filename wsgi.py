from backend import flask_app

if __name__ == "__main__":
    flask_app.app_context().push()
    flask_app.run(port=5000, debug=True)
