with open("breakfast.txt", "r") as f:
    
    lines = 0 

    for line in f:
        print(line.strip())


        lines +=1
print(f"there is {lines} lines")
