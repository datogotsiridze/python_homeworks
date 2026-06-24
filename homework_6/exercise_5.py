n = int(input("how many students are in group? "))


scores = {}

for _ in range (n):

    name = input(" what is your name? :")

    score = int(input("what is your score? : "))

    scores[name] = score

print(scores)
print(f"we have {len(scores)} students in group")
