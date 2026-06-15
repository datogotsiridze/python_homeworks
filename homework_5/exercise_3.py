tbilisi_week_grades = [20, 25, 27, 29, 19, 24, 32]
total = 0

for gradus in tbilisi_week_grades:
    total += gradus

print(f"თბილისის საშუალო ტემპერატურა {round(total/len(tbilisi_week_grades),1)} გრადუსია ")