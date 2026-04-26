from flask import Blueprint, jsonify, request
from services.github_service import get_user_profile, get_user_top_repos

github_bp = Blueprint("github", __name__)


@github_bp.route("/user/<username>", methods=["GET"])
def user_profile(username):
    data = get_user_profile(username)

    if not data:
        return jsonify({"error": "User not found"}), 404

    return jsonify(data)


@github_bp.route("/user/<username>/repos", methods=["GET"])
def user_repos(username):
    limit = request.args.get("limit", default=5, type=int)

    repos = get_user_top_repos(username, limit)

    if repos is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "username": username,
        "top_repositories": repos
    })