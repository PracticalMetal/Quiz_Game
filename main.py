from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

# this will loop through the list containing dictionary
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    # creating a new object
    new_ques=Questions(q_text, q_ans)
    question_bank.append(new_ques)

quiz=QuizBrain(question_bank)
while quiz.still_has_ques:
    quiz.next_question()

print(f'''You have completed the quiz!
Your final score was: {quiz.score}''')