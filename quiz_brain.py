from pickle import TRUE


class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.current_ques = self.question_list[self.question_num]
        self.question_num += 1
        print(f"Q.{self.question_num}: {self.current_ques.text}")

    def still_has_questions(self):
        if len(self.question_list) > (self.question_num):
            return True
        else: 
            return False

    def is_true(self, answer):
        if self.current_ques.answer == answer:
            self.score += 1
            return True
        else:
            return False

