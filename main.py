from question_model import Questions
from data import question_data

question_bank=[]

# this will loop through the list containing dictionary
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    # creating a new object
    new_ques=Questions(q_text, q_ans)
    question_bank.append(new_ques)

print(question_bank)