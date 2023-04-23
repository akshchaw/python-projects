from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    question_obj = Question(q_text=q_text, q_answer=q_answer)
    question_bank.append(question_obj)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz_brain.correct_answers}/{quiz_brain.question_number}")
