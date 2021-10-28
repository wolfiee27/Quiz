import os
import ast
from environs import Env
from replit import db
env = Env()
env.read_env() 
system =ast.literal_eval(os.environ['FILE'])


#main Program
from Quiz import GambelQuiz
name = input("HI welcome to GAMBLE-Quiz \n  Enter Your Name to proceed : ")
Obj = GambelQuiz(name,system)
Obj.questions()



# to find the answers once everyome completes
# arr = list(db.keys())
# for i in arr:
#   print(f"{i}:{db[i]}") 



  



