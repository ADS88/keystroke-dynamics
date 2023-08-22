class UserProfile:
    def __init__(self, username: str, milliseconds_per_character: float):
        self.username = username
        self.milliseconds_per_character = milliseconds_per_character

    def update_with_new_test(self, new_profile: 'UserProfile'):
        self.milliseconds_per_character = (self.milliseconds_per_character + new_profile.milliseconds_per_character) / 2

