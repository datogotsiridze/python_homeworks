n = int(input(" how many products we need?: "))

items = []

for _ in range(n):
    items.append(input("essential item is: "))
    
print(f" we need {n} items to have. they are: \n {items} ")