import statistics


class UserProfile:
    def __init__(self, username: str, milliseconds_per_character: float):
        self.username = username
        self.median_milliseconds_per_character = milliseconds_per_character
        self.milliseconds_per_character_previous_tests = [milliseconds_per_character]

    def update_with_new_test(self, new_profile: 'UserProfile'):
        self.milliseconds_per_character_previous_tests.append(new_profile.median_milliseconds_per_character)
        self.median_milliseconds_per_character = statistics.median(self.milliseconds_per_character_previous_tests)
