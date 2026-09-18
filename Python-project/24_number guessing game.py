import random

low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True
while is_running:
    guess =(input("Guess a number:"))
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess<answer:
            print("Your guess is too Low")
        elif guess>answer:
            print("Your guess is too High")
        elif guess==answer:
            print(f"You guessed my number is {answer}You are right")
            is_running = False

    else:
        print("It is a invalid value")
print(f"Your total guesses_number is {guesses}")


