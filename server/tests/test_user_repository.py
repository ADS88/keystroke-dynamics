from UserProfileRepository import UserProfileRepository
from UserProfile import UserProfile


def test_updates_existing_results_using_average():
    user_profile_repository = UserProfileRepository()

    test_result = UserProfile("test user", 1000)
    test_result_two = UserProfile("test user", 2000)
    test_result_three = UserProfile("different user", 3000)

    user_profile_repository.add_test(test_result)
    user_profile_repository.add_test(test_result_two)
    user_profile_repository.add_test(test_result_three)

    assert len(user_profile_repository.all_profiles()) == 2
    assert user_profile_repository.user_profiles['test user'].milliseconds_per_character == 1500


def test_adds_new_result_when_no_previous_results_for_user():
    user_profile_repository = UserProfileRepository()
    test_result = UserProfile("test user", 1000)
    user_profile_repository.add_test(test_result)
    assert len(user_profile_repository.all_profiles()) == 1
    assert list(user_profile_repository.all_profiles())[0] == test_result
