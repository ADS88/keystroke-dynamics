"""Script that checks how accurate the typing similarities provided by the app are against a set of data from kaggle"""
import json
from UserProfileRepository import UserProfileRepository
from similarity_finder import profile_user, find_three_users_most_similar_to_current

with open("../data/training_data.json") as training_json_file:
    training_data = json.load(training_json_file)

with open("../data/test_data.json") as test_json_file:
    test_data = json.load(test_json_file)

user_profile_repository = UserProfileRepository()
for submission in training_data:
    user_profile_repository.add_submission(profile_user(submission))

top_three_counts = [0, 0, 0]
times_not_present = 0

for test in test_data:
    test_result = profile_user(test)
    most_similar_users = find_three_users_most_similar_to_current(test_result, user_profile_repository.all_profiles())
    user_under_test = test["username"]
    if user_under_test in most_similar_users:
        position = most_similar_users.index(user_under_test)
        top_three_counts[position] += 1
    else:
        times_not_present += 1

times_in_top_3 = sum(top_three_counts)

print(f"First: {top_three_counts[0]}")
print(f"Second: {top_three_counts[1]}")
print(f"Third: {top_three_counts[2]}")
print(f"Not present: {times_not_present}")
print(f"In top 3: {times_in_top_3} times. Missing {times_not_present} times")
