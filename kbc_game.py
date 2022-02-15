question_list=["Which out the following is a scripting language??","What is the capital of India ?",
"Which of the following is the first calculating device? ? ","Who invented mechanical calculator called Pascaline?"]

options_list=[["Java","Python","Lisp","All of the above","None of the above"],
["Chandigarh","Bhopal","Chennai","Delhi","Hint option"],
["Abacus","Calculator","Turing Machine"," Pascaline","Hint option"]
,["Charles Babbage"," Blaise Pascal"," Alan Turing","Lee De Forest"]]

Hint_option=[["None of the above","All of the above"],["Bhopal","Delhi"],["Abacus","Pascaline"],["Blaise Pascal","Charles Babbage"]]

Hint_solution=[2,2,1,1]
solution_list=[4,4,1,2]
count=0

def hint(i):
	global count
	if count==0:
		k=0
		while k<len(Hint_option[i]):
			print(k+1,Hint_option[i][k])
			k=k+1
		answer=int(input("enter any no. "))
		count=count+1
		if answer==Hint_solution[i]:
			return True
		else:
			return False
	else:
		print("you already used hint option")
		option(i)

def option(i):
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1 
	ans=int(input("enter your answer: "))
	if ans==solution_list[i]:
		return True
	if ans==5:
		return hint(i)
	else:
		return False
	
def  question():
	i=0
	while i<len(question_list):
		print("Q.",i+1,question_list[i])
		x=option(i) 
		if x==True:
			print("your ans is correct")
		elif x==False:
			print("you lose the game")
			break
		i=i+1
question()
