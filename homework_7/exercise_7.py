numbers = [1, 2, 3, 4, 5, 6]
doubledd = [n * 2 for n in numbers]
evenss = [n for n in numbers if n % 2 == 0 ]

squaree = {n: n * n  for n in numbers}

print(doubledd)
print(evenss)
print(squaree)
