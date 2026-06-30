def minimum_and_maximum(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for i in numbers:
        if i < minimum:
         minimum = i
        elif i> maximum:
         maximum = i

    return minimum, maximum


numms = [10, 100, 1000, 24, 99,  888777, 765, 5]


minimum, maximum = minimum_and_maximum(numms)
print(minimum)
print(maximum)