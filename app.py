from flask import Flask, jsonify
from utils import fetch_user_repos, fetch_user, calculate_account_age

app = Flask(__name__)

@app.route("/user/<username>", methods=["GET"])
def get_user(username):
    user_data = fetch_user(username)

    if not user_data:
        return jsonify({"error": "User not found"}), 404
    
    created_at = user_data.get("created_at")
    account_age = calculate_account_age(user_data.get("created_at")) if created_at else "Unknown"

    response = {
        "username": user_data["login"],
        "public_repos": user_data["public_repos"],
        "followers": user_data["followers"],
        "account_age": account_age,
        "created_at": created_at,
        "last_update": user_data["updated_at"]
    }

    return jsonify(response)

@app.route("/user/<username>/repos", methods=["GET"])
def get_user_repos(username):
    repos = fetch_user_repos(username)

    if repos is None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "username": username,
        "top_repositories": repos
    })

# print("\nTop 5 Repositories:")
# for i, repo in enumerate(top_repos, start=1):
#     print(f"{i}. {repo['name']} ⭐ {repo['stars']}")

if __name__ == "__main__":
    app.run(debug=True)