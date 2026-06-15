def facecontrol (name, age):

   

    if age < 18:

        return " Sorry, no entry. "

    if age >= 21 and name == "nino":

        return " Welcome, VIP! "

    if age % 2 == 0 or  name =="giorgi":

        return " Welcome! Free drink for you! "

    else:

        return " Welcome! "

 

door_question1 = input(f"what's your name ? ").strip().lower()

door_question2 = int(input(f"what is your age ? "))   

print(f" {facecontrol(door_question1, door_question2)} ")  

 