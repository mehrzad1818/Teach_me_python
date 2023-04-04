class User:
    """ Manages the user. """

    def __init__(self, user_id, username) -> None:
        self.identity = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user is being created ... ")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jimmy")
user_2 = User("002", "Jones")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# This part deals with the new challenge

from data import question_data
from question_model import Question

question_banka = []

for question in question_data:
    Q_TEXT = (question["text"])
    Q_ANSWER = (question["answer"])
    NEW_QUESTION = Question(q_text=Q_TEXT, q_answer=Q_ANSWER)
    question_banka.append(NEW_QUESTION)

print(question_banka)


