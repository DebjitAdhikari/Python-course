class Quizbrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def still_has_question(self):
        if len(self.question_list)==self.question_number:
            return False
        return True
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.checkAnswer(user_ans,current_question.answer)

    def checkAnswer(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            print("right")
            self.score+=1
        else:
            print("wrong")
        print(f"correct ans {correct_ans}")
        print(f"your current score: {self.score}/{self.question_number}\n")
        
