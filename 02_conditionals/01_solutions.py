age = input("Provide me an age: ")

age = int(age)

if age < 13:
    print("User is child")
elif age < 20:
    print("User is teenager")
elif age < 60:
    print("User is Adult")
else:
    print("User is senior")