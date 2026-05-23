import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

password = input("Enter password: ")
print("Strength:", check_password(password))