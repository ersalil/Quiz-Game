from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    qtext = question["text"]
    qanswer = question["answer"]

    new_q = Question(qtext,qanswer)

    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    res = input("Answer (True/False): ")
    if quiz.is_true(res):
        print("Your Answer is Correct!")
    else:
        print("Your answer is wrong! Try again later!\n","Your Current Score: ", quiz.score)
        break
