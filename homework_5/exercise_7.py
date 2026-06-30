def average(nums):
    total  = 0
    for x in nums:
        total = total + x

    return total / len(nums)

list1 = [5, 9, 18, 22, 65, 12, 18, 20, 37]
list2 = [0, 2, 4, 5, 66, 128, 11, 10]

print(round(average(list1)))
print(round(average(list2)))
