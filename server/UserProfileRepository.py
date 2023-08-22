from UserProfile import UserProfile


class UserProfileRepository:
    def __init__(self):
        self.user_profiles: dict[str, UserProfile] = {}

    def add_test(self, test_result: UserProfile):
        username = test_result.username
        if username in self.user_profiles:
            self.user_profiles[username].update_with_new_test(test_result)
        else:
            self.user_profiles[username] = test_result

    def all_profiles(self):
        return self.user_profiles.values()
