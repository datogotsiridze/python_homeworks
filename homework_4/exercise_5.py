def count_vowels(word):

    count = 0

    for char in word.lower():

        if char == "a":

            count+=1

        if char == "e":

            count+=1

        if char == "i":

            count+=1

        if char == "o":

            count+=1 

        if char == "u":

            count+=1

    return count

new_movie = input ( " your favourite movie is...? ")

answer = count_vowels(new_movie)

print ( f" თქვენ მიერ არჩეული ფილმის სახელწოდებაში {answer} ხმოვანია ")

 