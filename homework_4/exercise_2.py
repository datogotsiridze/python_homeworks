def is_even(number):

    return (number % 2 == 0)

   

number = int(input("შეიყვანეთ თქვენი ნომერი: "))

 

if is_even(number):

        print(" თქვენ აირჩიეთ ლუწი რიცხვი! ")

else:

        print(" თქვენი არჩეული რიცხვი კენტია. ")