from random import randint
secret_number = randint(1,5)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won!")
        break
    else:
        print("you lost")

print("secret number was :", secret_number)