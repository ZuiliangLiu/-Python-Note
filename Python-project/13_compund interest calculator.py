# P = 0
# r = 0
# t = 0
#
#
# while P<= 0:
#     print("The P could not be less than 0")
#     if P <= 0:
#         P = float(input("Please enter a true number: "))
#
#
# while r<= 0:
#     print("The r could not be less than 0")
#     if r <= 0:
#         r = float(input("Please enter a true number: "))
#
# while t<= 0:
#     print("The t could not be less than 0")
#     if t <= 0:
#         t = int(input("Please enter a true number: "))
#
#
# A = P*pow((1+r/100),t)
#
# print(f"The total A is ${A:.3f}")
#注意while与if的先后顺序

P = 0
r = -1
t = 0

while P <= 0:
    P = float(input("Please enter the principal: "))

    if P <= 0:
        print("The principal must be greater than 0.")

while r < 0:
    r = float(input("Please enter the annual interest rate: "))

    if r < 0:
        print("The interest rate cannot be less than 0.")

while t <= 0:
    t = int(input("Please enter the number of years: "))

    if t <= 0:
        print("The number of years must be greater than 0.")

A = P * pow(1 + r / 100, t)

print(f"The total amount is ${A:.2f}")