from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank=[]
for i in question_data:
    #question_bank.append(Question(i["text"],i["answer"]))
    # question_text=i["text"]
    # question_ans=i["answer"]
    question_text=i["question"]
    question_ans=i["correct_answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)

quiz=Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score {quiz.score}/{len(question_bank)}")