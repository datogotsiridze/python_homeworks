try:
    with open("notes.txt" , "r") as f:
        notess = f.readlines()
except FileNotFoundError:
    notess = []

new_note = input("what do you want to add? ")

notess.append(new_note)

with open("notes.txt", "a") as f:
    f.write(new_note + "\n")

print(notess)