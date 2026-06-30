breakfast_list = ["potato", "cheese", "egg"]

with open("breakfast.txt" , "w") as f:
    for x in breakfast_list:
        f.write(x + "\n")

with open("breakfast.txt", "r") as f:
    sauzme = f.read()

print(sauzme)