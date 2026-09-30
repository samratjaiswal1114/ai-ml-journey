phone_numbers = input("Enter phone numbers: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone_numbers:
    output += digits_mapping.get(ch,"!") + " "
print(output)
