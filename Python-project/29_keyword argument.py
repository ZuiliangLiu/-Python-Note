# def get_phonenumbers(country,area,frist,last):
#     return f"{country}-{area}-{frist}-{last}"
# get_phonenumbers(country=1,area=2,frist=3456,last=7890)
# number = get_phonenumbers(country=1,area=2,frist=3456,last=7890)
# print(number)
def name(first,last):
    return f"{first}{last}"
print(f"Your full name is  {name(input("Enter your first name:"),input("Enter your last name:"))}")
print(name(first="zl",last="l"))
