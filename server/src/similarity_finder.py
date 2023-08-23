from UserProfile import UserProfile
from input_models import Submission
from typing_characteristics_calculations import calculate_milliseconds_per_character, calculate_median_dwell_time


def profile_user(submission: Submission) -> UserProfile:
    """Creates a profile with calculated characteristics calculated for the user who made the submission"""
    username = submission["username"]
    results = submission["results"]
    milliseconds_per_character = calculate_milliseconds_per_character(results)
    median_dwell_time = calculate_median_dwell_time(results)
    return UserProfile(username, milliseconds_per_character, median_dwell_time)


def find_three_users_most_similar_to_current(
        current_user_profile: UserProfile,
        all_profiles: list[UserProfile]) -> list[str]:
    """Returns the names of the three users found to be most similar to the user who made the submission"""
    similarities_to_other_profiles = [(current_user_profile.similarity_with(other_profile), other_profile.username) for
                                      other_profile in
                                      all_profiles]
    similarities_to_other_profiles.sort(key=sort_by_minimum_difference_score_then_name)
    three_most_similar_profiles = similarities_to_other_profiles[0:3]
    three_most_similar_names = [profile[1] for profile in three_most_similar_profiles]
    return three_most_similar_names


def sort_by_minimum_difference_score_then_name(difference_result: tuple[float, str]):
    return difference_result[0], difference_result[1]
