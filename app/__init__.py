# app/__init__.py

from flask import Flask
from app.main import app as main_app

def create_app():
    app = Flask(__name__)

    # Mengonfigurasi aplikasi jika diperlukan
    app.config['DATABASE'] = 'oilandgas_company.db'

    # Menggabungkan rute dari main.py
    app.register_blueprint(main_app)

    return app
