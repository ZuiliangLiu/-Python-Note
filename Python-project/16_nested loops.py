# for x in range(1,4):
#     for y in range(1,10):
#         print(y,end="")
#     print("-")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")
for x in range(cols):
    for y in range(rows):
        print(symbol,end="")
    print()