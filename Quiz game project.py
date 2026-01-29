#Quiz game project
file_name = "high_score.txt"
score = 0
high_score = 0
#Load high score
def load_high_score():
    global high_score
    try:
        #open file in read mode
        file = open(file_name,"r")
        high_score = int(file.read())
        file.close()
    except:
        pass
#Save high score
def save_high_score():
    #open the file in write mode
    file = open(file_name,"w")
    file.write(str(high_score))
    file.close()
#Play Quiz
def play_quiz():
    global score
    questions = ["what is the output of print(2+3)?", "which datatype stores True/False", "which keyword is used to fetch global variable in the function?"]
    answers = ["5","bool","global"]
    for i in range(len(questions)):
        print("\nQ.",questions[i])
        user_answer = input("your_answer:")
        if user_answer == answers[i]:
            score = score+1
            print("Correct")
        else:
            print("Wrong!")
#Main Program
def main():
    #global allows upadating same high score
    global high_score
    #load previous high score
    load_high_score()
    #ask the player name
    name = input("enter your name:")
    #start quiz
    play_quiz()
    #print final score
    print("\nQuiz over")
    print(name,"your score is:", score)
    #compare scorewith high score
    if score>high_score:
        high_score = score
        save_high_score ()
    else:
        print("high score is:",high_score)
main()