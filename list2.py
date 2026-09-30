num = [1,2,2,4,5,4,5,6,7,6,5,7,6,5]
uniques = []
for number in num:
    if number not in uniques:
        uniques.append(number)
print(uniques)
