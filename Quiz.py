# import os
from replit import db
import  random
import time
class GambelQuiz:
    def __init__(self, name,questionData):
        self.name = name
        self.Data = questionData
        self.attended = []
        self.Score = 0
        self.questionNo = 0

    def scoreBoard(self,answer,recived_answer,Question):
        if recived_answer == answer:
            self.Score +=100
            print( f"\n WOW !! you got that right \n +100 point !!! \n  current score : {self.Score} \n\n")
        elif recived_answer == "z":
            self.Score += 50
            print(f"\n Well thats a Smart Move \n +50 point !!! \n current score : {self.Score} \n\n")
        elif recived_answer != ( answer or "z"):
            print(f" \n OOps !!! Wrong Answer \n correct answer is {answer}){Question[answer]}  \n current score : {self.Score} \n\n")

    def questions(self):
        self.answer_entered = ""
        self.current_question = self.Data[1]
        self.Flag = True

        while self.Flag == True:

            # to make sure no repeated question is asked and to generate randomness
            if self.current_question not in self.attended:
                time.sleep(2)
                self.attended.append(self.current_question)
                self.questionNo += 1

                # print the questions and answers
                print(f"{self.questionNo}) { self.current_question['q'] }")
                print(f" a){ self.current_question['a'] } \n b){ self.current_question['b'] } \n"
                      f" c){ self.current_question['c'] } \n d){ self.current_question['d'] } \n z){ self.current_question['z'] } ")

                #get the input from the user
                self.answer_entered = input("enter your response : ").lower()

                #check if the answer is correct and update the scoreboard
                self.scoreBoard( self.current_question["ans"] ,self.answer_entered,self.current_question )

            #check to see if the Questions are complete
            elif self.questionNo == 4:
                print(f"the Quiz has ended you have scored {self.Score} and overall { round( (self.Score / 400 ) *100 , 2)} %")
                # os.environ[f'{self.name}'] = f'{self.Score}'
                db[f"{self.name}"] = f"{self.Score}"
                self.Flag = False
                break

            #get a new Question
            self.current_question = self.Data[random.randint(1,4)]



