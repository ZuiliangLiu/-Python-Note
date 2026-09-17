questions = ["1",
             "2",
             "3",
             "4",
             "5"]
options =[["A:GPT","B:TESLA","C:GORK","D:SPACEX"],
          ["A:GOOGLE","B:APPLE","C:SAM","D:ARMS"],
          ["A","B","C","D"],
          ["A","B","C","D"],
          ["A","B","C","D"]]
answers = ["C","D","A","A","B"]
guess = []
total_score = 0
num = 0


for question in questions:
    print(question)

    if num < 5:
       for option in options[num]:
           print(option)
    else:
        break

    answer = input("What would you like to guess?").upper()
    if answer == answers[num]:
        print("Correct!")
        total_score += 1
    else:
        print("Wrong!")

    num = num + 1
    print("--------------------------")


print(f"Total score: {total_score}")
