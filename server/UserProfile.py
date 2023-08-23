import statistics


class UserProfile:
    def __init__(self, username: str, milliseconds_per_character: float, dwell_time):
        self.username = username
        self.median_milliseconds_per_character = milliseconds_per_character
        self.milliseconds_per_character_previous_tests = [milliseconds_per_character]
        self.median_dwell_time = dwell_time
        self.dwell_times_previous_tests = [dwell_time]

    def update_with_new_test(self, new_profile: 'UserProfile'):
        self.milliseconds_per_character_previous_tests.append(new_profile.median_milliseconds_per_character)
        self.median_milliseconds_per_character = statistics.median(self.milliseconds_per_character_previous_tests)

        self.dwell_times_previous_tests.append(new_profile.median_dwell_time)
        self.median_dwell_time = statistics.median(self.dwell_times_previous_tests)

    def similarity_with(self, other_profile: 'UserProfile'):
        return abs(self.median_milliseconds_per_character - other_profile.median_milliseconds_per_character) + abs(
            self.median_dwell_time - other_profile.median_dwell_time) * 6
