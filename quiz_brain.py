class QuizBrain:
    def __init__(self, q_list):
        self.question_number=0
        self.questionlist=q_list
        self.score=0

    def still_has_ques(self):
        return self.question_number<len(self.questionlist)

    def check_answer(self, user_input, current_ques):
        # using input from the user to check if the answer is correct and keep a score
        if user_input.lower()==current_ques.answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print(f"That's wrong. The correct answer is {current_ques.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        # we get hold of the Question object
        current_ques=self.questionlist[self.question_number]
        self.question_number+=1
        user_input=input(f"Q.{self.question_number}: {current_ques.text} (True/False)?: ")
        self.check_answer(user_input, current_ques)

