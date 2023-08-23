import statistics
from input_models import KeyEvent, KeyEventType


def calculate_milliseconds_per_character(results: list[KeyEvent]) -> float:
    """Returns the total time taken divided by the total characters typed. Total characters typed is arbitrarily defined
    as the number of keydown events"""
    if len(results) == 0:
        raise ValueError("Can't calculate milliseconds per character from empty result list")
    start_time = results[0]["timestampMillis"]
    end_time = results[-1]["timestampMillis"]
    total_time = end_time - start_time
    characters_pressed = len([result for result in results if result["type"] == KeyEventType.KEYDOWN])
    return total_time / characters_pressed if characters_pressed > 0 else total_time


def calculate_median_dwell_time(results: list[KeyEvent]) -> float:
    """Calculates median dwell time using the time between key down and key up events for each key.
    Dwell is time the time between a key being pressed down, and released."""
    dwell_times = []
    key_to_keydown_timestamp: dict[str, float] = {}

    for key_event in results:
        key = key_event["key"]
        key_type = key_event["type"]
        timestamp = key_event["timestampMillis"]

        if key_type == KeyEventType.KEYDOWN:
            key_to_keydown_timestamp[key] = timestamp

        elif key_type == KeyEventType.KEYUP and key in key_to_keydown_timestamp:
            keydown_timestamp = key_to_keydown_timestamp.pop(key)
            dwell_time = timestamp - keydown_timestamp
            dwell_times.append(dwell_time)

    median_dwell_time = statistics.median(dwell_times)
    return median_dwell_time
