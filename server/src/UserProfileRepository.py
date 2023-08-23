from UserProfile import UserProfile


class UserProfileRepository:
    """Stores a list of UserProfiles containing information about how users type. In future this should be replaced
    by a database, or more efficient data structure"""

    def __init__(self):
        self.user_profiles: dict[str, UserProfile] = {}

    def add_submission(self, test_result: UserProfile):
        """Either creates a new profile based on a new user submission, or updates the user's existing profile if it
        exists """
        username = test_result.username
        if username in self.user_profiles:
            self.user_profiles[username].update_with_new_test(test_result)
        else:
            self.user_profiles[username] = test_result

    def all_profiles(self):
        return self.user_profiles.values()
