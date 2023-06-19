score = input("Enter Score: ")

score_number = float(score)

if (score_number < 0 or score_number > 1):
    print("Choose a number between 0.0 and 1.0")
else:
    grade = "undefined"
    if(score_number >= 0.9):
        grade = "A"
    elif(score_number >= 0.8):
        grade = "B"
    elif(score_number >= 0.7):
        grade = "C"
    elif(score_number >= 0.6):
        grade = "D"
    else:
        grade = "F"
    print(grade)