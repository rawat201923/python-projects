password = "Secure3"

if len(password)<6:
    strength = "weak"
elif len(password)<= 10:
    strength= "medium"
else:
    strength = "strong"

print("password strength is : ", strength)