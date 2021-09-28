class Questions:
    def __init__(self, q_text, q_answer):
        self.text=q_text
        self.answer=q_answer

new_ques=Questions("2+3=5", "true")
print(new_ques.answer)