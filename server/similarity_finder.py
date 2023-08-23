from UserProfile import UserProfile
from input_models import KeyEvent, TestData
import statistics


def profile_user(test: TestData, weights) -> UserProfile:
    username = test["username"]
    results = test["results"]
    milliseconds_per_character = calculate_milliseconds_per_character(test["results"]) * weights[0]
    median_dwell_time = calculate_median_dwell_time(results) * weights[1]
    median_interval_time = calculate_median_interval_time(results) * weights[2]
    return UserProfile(username, milliseconds_per_character, median_dwell_time, median_interval_time)


def find_three_most_similar_to_current_user(
        current_user: UserProfile,
        all_profiles: list[UserProfile]) -> list[str]:
    differences = [(current_user.similarity_to(other_profile), other_profile.username) for other_profile in
                   all_profiles]
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


def calculate_median_dwell_time(results: list[KeyEvent]) -> float:
    dwell_times = []
    key_to_keydown_timestamp: dict[str, float] = {}

    for key_event in results:
        key = key_event["key"]
        key_type = key_event["type"]
        timestamp = key_event["timestampMillis"]

        if key_type == "keydown":
            key_to_keydown_timestamp[key] = timestamp

        # elif key_type == KEY_UP:
        elif key_type == "keyup" and key in key_to_keydown_timestamp:
            keydown_timestamp = key_to_keydown_timestamp.pop(key)
            dwell_time = timestamp - keydown_timestamp
            dwell_times.append(dwell_time)

    median_dwell_time = statistics.median(dwell_times)
    return median_dwell_time


def calculate_median_interval_time(result: list[KeyEvent]) -> float:
    most_recent_keyup_timestamp = None
    interval_times = []
    for key_event in result:
        key_type = key_event["type"]
        timestamp = key_event["timestampMillis"]
        if key_type == "keydown" and most_recent_keyup_timestamp is not None:
            interval_time = timestamp - most_recent_keyup_timestamp
            interval_times.append(interval_time)
            most_recent_keyup_timestamp = None
        elif key_type == "keyup":
            most_recent_keyup_timestamp = timestamp
    median_interval_time = statistics.median(interval_times)
    return median_interval_time
