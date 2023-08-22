from UserProfile import UserProfile
from input_models import KeyEvent, TestData


def profile_user(test: TestData) -> UserProfile:
    username = test["username"]
    milliseconds_per_character = calculate_milliseconds_per_character(test["results"])
    return UserProfile(username, milliseconds_per_character)


def find_three_most_similar_to_current_user(
        current_user: UserProfile,
        all_profiles: list[UserProfile]) -> list[str]:
    differences = [
        (abs(current_user.milliseconds_per_character - other_profile.milliseconds_per_character),
         other_profile.username
         ) for other_profile in all_profiles]
    differences.sort(key=lambda x: (x[0], x[1]))
    return [difference[1] for difference in differences[0:3]]


def calculate_milliseconds_per_character(results: list[KeyEvent]):
    if len(results) == 0:
        raise ValueError("Can't calculate milliseconds per character from empty result list")
    start_time = results[0]["timestampMillis"]
    end_time = results[-1]["timestampMillis"]
    total_time = end_time - start_time
    characters_pressed = len([result for result in results if result["type"] == "keydown"])
    return total_time / characters_pressed if characters_pressed > 0 else total_time
