import random
a = int(input("Upper limit of range : "))
b = int(input("Lower limit of range : "))
random_number = random.randrange(a, b)
guesses = 1
user_input = 0
while user_input != random_number:
    if guesses <= 3:
        user_input = int(input("Guess a number between given range : "))

        if user_input > random_number:
            if guesses == 3:
                print("Your guess number is little higher . ")
            else:
                print("Your guess number is little higher . Try one more time .")
        elif user_input < random_number:
            if guesses == 3:
                print("Your guess number is little low . ")
            else:
                print("Your guess number is little low . Try one more time .")
        else:
            print("Congratulations! Your guess was correct . ")
            break
    elif guesses > 3:
      print("Better luck next time .")
      break
    guesses += 1