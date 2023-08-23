from src.input_models import KeyEvent
from pytest import raises
from src.typing_characteristics_calculations import calculate_milliseconds_per_character


def test_milliseconds_per_character_calculates_correctly():
    events: list[KeyEvent] = [
        {'key': 't', 'type': 'keydown', 'timestampMillis': 100},
        {'key': 'e', 'type': 'keydown', 'timestampMillis': 200},
        {'key': 't', 'type': 'keyup', 'timestampMillis': 300},
        {'key': 'e', 'type': 'keyup', 'timestampMillis': 350},
        {'key': 's', 'type': 'keydown', 'timestampMillis': 400},
        {'key': 's', 'type': 'keyup', 'timestampMillis': 500},
        {'key': 't', 'type': 'keydown', 'timestampMillis': 700},
        {'key': 't', 'type': 'keyup', 'timestampMillis': 900}
    ]
    milliseconds_per_character = calculate_milliseconds_per_character(events)
    assert milliseconds_per_character == 200


def test_milliseconds_per_character_throws_value_error_with_empty_input():
    events = []
    with raises(ValueError):
        calculate_milliseconds_per_character(events)
