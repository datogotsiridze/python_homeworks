your_answer = input(" which number do you want? ")
try:

    numbers = int(your_answer)
except ValueError:
    print(f"{your_answer} is not a number ")

else:
    print(f"double is {numbers*2} ")