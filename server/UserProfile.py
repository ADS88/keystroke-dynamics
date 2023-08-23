import statistics

# Dwell time multiplier that performed best during accuracy testing
DWELL_TIME_WEIGHT = 6


class UserProfile:
    """Holds all calculated information about how a user types"""
    def __init__(self, username: str, milliseconds_per_character: float, dwell_time):
        self.username = username
        self.median_milliseconds_per_character = milliseconds_per_character
        self.milliseconds_per_character_previous_tests = [milliseconds_per_character]
        self.median_dwell_time = dwell_time
        self.dwell_times_previous_tests = [dwell_time]

    def update_with_new_test(self, new_profile: 'UserProfile'):
        """Computes new values for profile data based on the most recent submission a user makes"""
        self.milliseconds_per_character_previous_tests.append(new_profile.median_milliseconds_per_character)
        self.median_milliseconds_per_character = statistics.median(self.milliseconds_per_character_previous_tests)

        self.dwell_times_previous_tests.append(new_profile.median_dwell_time)
        self.median_dwell_time = statistics.median(self.dwell_times_previous_tests)

    def similarity_with(self, other_profile: 'UserProfile'):
        """Returns a float showing how similar a user types to another. The lower the number, the more similar"""
        return abs(self.median_milliseconds_per_character - other_profile.median_milliseconds_per_character) + abs(
            self.median_dwell_time - other_profile.median_dwell_time) * DWELL_TIME_WEIGHT
