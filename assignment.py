# Programmer: Henderson Fryer
# Course: CS701/GB-731, Dr. Yalew
# Date: 8/12/2024
# Programming Assignment: 3
# Program Inputs: A string containing answer
# Program Outputs: Very good(If 100% correct) or Missed number and Score Presentage
def main():
    # Define a string containing the correct answers.
    CORRECT_ANSWERS = "adbdcacbdac"

    #get input from student
    studentAnswer = input("Enter your multiple choice answers: ")

    #validate input
    while len(studentAnswer) != len(CORRECT_ANSWERS):
        print("Error: an incorrect number of answers given.")
        studentAnswer = input("Enter your multiple choice answers: ")
    
    #create a new string of correct answers and 'X' for incorrect answers
    checkedAnswers = ''
    wrongAnswers = 0
    for i in range(0,len(studentAnswer)):
        if studentAnswer[i] == CORRECT_ANSWERS[i]:
            checkedAnswers += studentAnswer[i]
        else:
            checkedAnswers += 'X'
            wrongAnswers += 1
    
    #print results
    if wrongAnswers == 0:
        print("Very Good!")
    else:
        print("You missed ", wrongAnswers, " questions: ", checkedAnswers, sep = '')
    print("Your score is: ", int(round(((len(CORRECT_ANSWERS) - wrongAnswers)/len(CORRECT_ANSWERS)) * 100)), " percent", sep='')
    

if __name__ == "__main__":
    main()