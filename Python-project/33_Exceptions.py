try:
   age =  int(input("Enter your age: "))
   income = 20000
   max = income/age
except ValueError:
    print("Please enter an integer")
except ZeroDivisionError:
    print("You cannot divide by zero")
print(f"You age is {age},and your max is {max:.2f}")