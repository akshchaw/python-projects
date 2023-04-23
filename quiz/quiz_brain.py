class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = q_list

    def still_has_questions(self):
        total_questions = len(self.question_list)
        return self.question_number <= total_questions-1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q{self.question_number}. {current_question.question} enter True or False: ")
        self.check_answer(user_choice,current_question.answer)

    def check_answer(self,user_choice,correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("You got it right")
            self.correct_answers += 1
        else:
            print('You got it wrong')
        print(f"Correct answer is {correct_answer}")
        print(f"Your score is {self.correct_answers}/{self.question_number}.")
        print('\n')


