score = int(input("Enter a  score of student: "))

if score >= 101:
    print("please verify your grade again")
    exit()
    
if 90 <= score :
    print("Grade is A")
elif 80 <= score :
    print("Grade is B")
elif 70 <= score :
    print("Grade is C")
elif 80 <= score:
    print("Grade is D")
else:
    print("Grade is E")