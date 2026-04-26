from flask import Flask, jsonify
from routes.github_routes import github_bp
from utils.logger import setup_logging

setup_logging()

app = Flask(__name__)

app.register_blueprint(github_bp)

if __name__ == "__main__":
    app.run(debug=True)