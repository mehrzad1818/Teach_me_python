class User:
    """ Manages the user. """

    def __init__(self, user_id, username) -> None:
        self.identity = user_id
        self.username = username
        print("New user is being created ... ")


user_1 = User("001", "Jimmy")

print(user_1.username)


user_2 = User()
user_2.id = "002"
user_2.username = "Jones"
print(user_2.username)

def enter_racemode():
    seats = 2
