from similarity_finder import calculate_milliseconds_per_character, find_three_most_similar_to_current_user
from UserProfile import UserProfile
from input_models import KeyEvent
from pytest import raises


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


def test_most_similar_users_returns_empty_list_if_no_users_stored():
    current_user = UserProfile("test", 100)
    all_profiles = []
    most_similar_users = find_three_most_similar_to_current_user(current_user, all_profiles)
    assert len(most_similar_users) == 0


def test_most_similar_users_returns_the_most_similar_users():
    current_user = UserProfile("test", 100)
    all_profiles = [UserProfile("andrew", 150), UserProfile("frankie", 30)]
    most_similar_users = find_three_most_similar_to_current_user(current_user, all_profiles)
    assert len(most_similar_users) == 2
    assert most_similar_users[0] == "andrew"
    assert most_similar_users[1] == "frankie"


def test_most_similar_users_returns_at_maximum_the_three_most_similar_users():
    current_user = UserProfile("test", 100)
    all_profiles = [UserProfile("fletcher", 80),
                    UserProfile("arya", 30),
                    UserProfile("test", 97),
                    UserProfile("frankie", 30),
                    UserProfile("steve", 105)]
    most_similar_users = find_three_most_similar_to_current_user(current_user, all_profiles)
    assert len(most_similar_users) == 3
    assert most_similar_users[0] == "test"
    assert most_similar_users[1] == "steve"
    assert most_similar_users[2] == "fletcher"


def test_most_similar_users_sorts_by_name_if_two_users_have_some_milliseconds_per_character():
    current_user = UserProfile("test", 100)
    all_profiles = [UserProfile("a", 80), UserProfile("z", 80)]

    most_similar_users = find_three_most_similar_to_current_user(current_user, all_profiles)
    assert len(most_similar_users) == 2
    assert most_similar_users[0] == "a"
