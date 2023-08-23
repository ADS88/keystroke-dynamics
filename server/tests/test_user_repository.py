from src.UserProfileRepository import UserProfileRepository
from src.UserProfile import UserProfile


def test_updates_existing_results_using_median():
    user_profile_repository = UserProfileRepository()

    test_results = [
        UserProfile("test user", 2000, 100),
        UserProfile("other user", 2000, 200),
        UserProfile("test user", 2130, 300),
        UserProfile("test user", 1843, 400)
    ]

    for result in test_results:
        user_profile_repository.add_submission(result)

    assert len(user_profile_repository.all_profiles()) == 2
    assert user_profile_repository.user_profiles['test user'].median_milliseconds_per_character == 2000
    assert user_profile_repository.user_profiles['test user'].median_dwell_time == 300


def test_adds_new_result_when_no_previous_results_for_user():
    user_profile_repository = UserProfileRepository()
    test_result = UserProfile("test user", 1000, 100)
    user_profile_repository.add_submission(test_result)
    assert len(user_profile_repository.all_profiles()) == 1
    assert list(user_profile_repository.all_profiles())[0] == test_result
