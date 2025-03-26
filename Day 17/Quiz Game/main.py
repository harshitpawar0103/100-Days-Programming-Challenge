from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["question"],question_data[i]["correct_answer"]))

# print(question_bank[0].answer)
q1 = QuizBrain(question_bank)
# print(q1.question_list[0].answer)
while q1.still_has_questions():
    ui = q1.next_question()
    q1.check_answer(ui)

print(f"You've completed the quiz. \nYour final score is : {q1.score}/{q1.question_number} ")
