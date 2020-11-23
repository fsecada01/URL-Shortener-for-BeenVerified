import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

BACKEND_DIR = os.path.join(BASE_DIR, "backend")

FRONTEND_DIR = os.path.join(BASE_DIR, "frontned")

SECRET_KEY = "dev"

SQLALCHEMY_DATABASE_URI = (
    f"sqlite:///{os.path.join(BACKEND_DIR, 'ltv_test.db')}"
)
