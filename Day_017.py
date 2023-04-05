# This is the start of the Day 17. 


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

# New challenges main.py file:

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_banka = []

for question in question_data:
    Q_TEXT = (question["text"])
    Q_ANSWER = (question["answer"])
    NEW_QUESTION = Question(q_text=Q_TEXT, q_answer=Q_ANSWER)
    question_banka.append(NEW_QUESTION)

quiz = QuizBrain(question_banka)

while quiz.has_new_questions:
    quiz.next_question()

if quiz.has_new_questions is False:
    print("You've completed the quiz.")
    print(
        f"Your final score is: {quiz.score}/{quiz.question_number}")


    
# question_model.py file:

class Question:
    """ Manages the questions. """

    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer

        
# data.py file:

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.",
     "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
     "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# quiz_brain.py file:

class QuizBrain:
    "Manges the game."

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def has_new_questions(self):
        """ Manages the remaining questions. """
        return self.question_list[self.question_number + 1]
        # return self.question_number < len(self.question_list)

    def next_question(self):
        """ Manages the next question. """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{(self.question_number)}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """ Manages the answers. """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

