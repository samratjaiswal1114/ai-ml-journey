weight = int(input(" enter your weight: "))
unit = input ("(g) or (K) : ")
if unit == "g":
    weight = weight / 1000
    print(weight)
else:
    weight = weight * 1000
    print(weight)
