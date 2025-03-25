


class QuizBrain :
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        ui = input(f"Q. {self.question_number+1} : {self.question_list[self.question_number].text} (True/False) : " )
        self.question_number += 1
        return ui

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,ui):
        correct_answer = self.question_list[self.question_number-1].answer
        if ui.lower() == correct_answer.lower():
            self.score+=1 
            print(f"You got it right.")
        else :
            print("Wrong answer")
        print(f"The correct answer was : {correct_answer}")
        print(f"your current score is : {self.score}/{self.question_number}")
        print("\n\n")




