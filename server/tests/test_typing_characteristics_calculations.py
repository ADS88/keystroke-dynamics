from src.input_models import KeyEvent, KeyEventType
from pytest import raises
from src.typing_characteristics_calculations import calculate_milliseconds_per_character, calculate_median_dwell_time


def test_milliseconds_per_character_calculates_correctly():
    events: list[KeyEvent] = [
        {'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 100},
        {'key': 'e', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 200},
        {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 300},
        {'key': 'e', 'type': KeyEventType.KEYUP, 'timestampMillis': 350},
        {'key': 's', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 400},
        {'key': 's', 'type': KeyEventType.KEYUP, 'timestampMillis': 500},
        {'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 700},
        {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 900}
    ]
    milliseconds_per_character = calculate_milliseconds_per_character(events)
    assert milliseconds_per_character == 200


def test_milliseconds_per_character_throws_value_error_with_empty_input():
    events = []
    with raises(ValueError):
        calculate_milliseconds_per_character(events)


def test_median_dwell_time_works_with_no_overlapping_key_presses():
    events: list[KeyEvent] = [{'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 100},
                              {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 200},
                              {'key': 'e', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 300},
                              {'key': 'e', 'type': KeyEventType.KEYUP, 'timestampMillis': 350},
                              {'key': 's', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 400},
                              {'key': 's', 'type': KeyEventType.KEYUP, 'timestampMillis': 600},
                              {'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 700},
                              {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 925}]
    median_dwell_time = calculate_median_dwell_time(events)
    assert median_dwell_time == 150


def test_median_dwell_time_works_with_some_overlapping_key_presses():
    events: list[KeyEvent] = [{'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 100},
                              {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 220},
                              {'key': 'e', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 300},
                              {'key': 'e', 'type': KeyEventType.KEYUP, 'timestampMillis': 350},
                              {'key': 's', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 400},
                              {'key': 's', 'type': KeyEventType.KEYUP, 'timestampMillis': 600},
                              {'key': 't', 'type': KeyEventType.KEYDOWN, 'timestampMillis': 700},
                              {'key': 't', 'type': KeyEventType.KEYUP, 'timestampMillis': 935}]
    median_dwell_time = calculate_median_dwell_time(events)
    assert median_dwell_time == 160
