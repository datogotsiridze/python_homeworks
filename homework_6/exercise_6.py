nature = "river tree forrest tree field tree river hill"
place_list = nature.split()


counts = {}

for place in place_list:
        
        counts[place] = counts.get(place, 0) + 1

print(counts)