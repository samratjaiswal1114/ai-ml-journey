def find_max(number):
    maximum = number[0]
    for i in number:
        if i > maximum:
            maximum = i
    print(maximum)
