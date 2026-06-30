# car_info = ("subaru", "forester", "red", 2017)
# brand, model, colour, year = car_info

# print(colour)


def min_max(numbers):
    return min(numbers), max(numbers)


nums = (55, 25, 150,  2, -99,  52)

print(min_max(nums))


lowest, highest = min_max(nums)

print(lowest)

print(highest)