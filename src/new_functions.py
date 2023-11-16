class User:

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email


class UserDatabase:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, username, email):
        new_user = User(self.next_id, username, email)
        self.users[self.next_id] = new_user
        self.next_id += 1
        return new_user

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, new_username=None, new_email=None):
        user = self.users.get(user_id)
        if user:
            if new_username:
                user.username = new_username
            if new_email:
                user.email = new_email
            return True
       
