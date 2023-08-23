"""Script that checks how accurate the typing similarities provided by the app are"""
from test_data import test_data
from training_data import training_data
from src.UserProfileRepository import UserProfileRepository
from src.similarity_finder import profile_user, find_three_users_most_similar_to_current

user_profile_repository = UserProfileRepository()
for submission in training_data:
    test_result = profile_user(submission)
    user_profile_repository.add_submission(test_result)

times_first_result = 0
times_second_result = 0
times_third_result = 0
times_not_present = 0

for test in test_data:
    test_result = profile_user(test)
    most_similar_users = find_three_users_most_similar_to_current(test_result, user_profile_repository.all_profiles())
    user_under_test = test["username"]
    if user_under_test in most_similar_users:
        if user_under_test == most_similar_users[0]:
            times_first_result += 1
        elif user_under_test == most_similar_users[1]:
            times_second_result += 1
        else:
            times_third_result += 1
    else:
        times_not_present += 1


print(f"First: {times_first_result}")
print(f"Second: {times_second_result}")
print(f"Third: {times_third_result}")
print(f"Not present: {times_not_present}")

times_in_top_3 = times_first_result + times_second_result + times_third_result
print(f"In top 3: {times_in_top_3} times. Missing {times_not_present} times")

