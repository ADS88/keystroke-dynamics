import random

from flask import Flask, request, jsonify
from flask_cors import CORS

from similarity_finder import find_three_users_most_similar_to_current, profile_user
from UserProfileRepository import UserProfileRepository
from sentences import sentences

app = Flask(__name__)
CORS(app)

user_profile_repository = UserProfileRepository()


@app.route("/api/v1/sentence", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        sentence_id, text = random.choice(list(sentences.items()))
        return jsonify(id=sentence_id, text=text)
    elif request.method == 'POST':
        current_user_profile = profile_user(request.json)
        people_who_type_most_similar_to_current_user = find_three_users_most_similar_to_current(
            current_user_profile,
            user_profile_repository.all_profiles()
        )
        user_profile_repository.add_test(current_user_profile)
        return people_who_type_most_similar_to_current_user


if __name__ == "__main__":
    app.run()
