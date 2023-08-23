from UserProfile import UserProfile
from similarity_finder import find_three_users_most_similar_to_current


def test_most_similar_users_returns_empty_list_if_no_users_stored():
    current_user = UserProfile("test", 100, 0)
    all_profiles = []
    most_similar_users = find_three_users_most_similar_to_current(current_user, all_profiles)
    assert len(most_similar_users) == 0


def test_most_similar_users_returns_the_most_similar_users():
    current_user = UserProfile("test", 100, 0)
    all_profiles = [UserProfile("andrew", 150, 0), UserProfile("frankie", 30, 0)]
    most_similar_users = find_three_users_most_similar_to_current(current_user, all_profiles)
    assert len(most_similar_users) == 2
    assert most_similar_users[0] == "andrew"
    assert most_similar_users[1] == "frankie"


def test_most_similar_users_returns_at_maximum_the_three_most_similar_users():
    current_user = UserProfile("test", 100, 0)
    all_profiles = [UserProfile("fletcher", 80, 0),
                    UserProfile("arya", 30, 0),
                    UserProfile("test", 97, 0),
                    UserProfile("frankie", 30, 0),
                    UserProfile("steve", 105, 0)]
    most_similar_users = find_three_users_most_similar_to_current(current_user, all_profiles)
    assert len(most_similar_users) == 3
    assert most_similar_users[0] == "test"
    assert most_similar_users[1] == "steve"
    assert most_similar_users[2] == "fletcher"


def test_most_similar_users_sorts_by_name_if_two_users_have_some_milliseconds_per_character():
    current_user = UserProfile("test", 100, 0)
    all_profiles = [UserProfile("a", 80, 0), UserProfile("z", 80, 0)]

    most_similar_users = find_three_users_most_similar_to_current(current_user, all_profiles)
    assert len(most_similar_users) == 2
    assert most_similar_users[0] == "a"
