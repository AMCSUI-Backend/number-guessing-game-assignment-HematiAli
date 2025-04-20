from random import randint

attemp = 0
gold_number = randint(1, 100)

while 1:
    guess_number = int(input("geuss the number : "))
    attemp += 1
    if guess_number < gold_number :
        print("Too low!")

    elif guess_number > gold_number :
        print("Too high!")
    else :
        print("Congratulations! You guessed it!")
        break

print(f"your attempt is {attemp}")
