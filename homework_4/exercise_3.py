def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    else:
        return "F"

score = int(input(" რა ქულა მიიღე გამოცდაზე? "))
print(f" მეგობარო შენ აიღე {score} ქულა რაც არის {letter_grade(score)} ნიშანი ")