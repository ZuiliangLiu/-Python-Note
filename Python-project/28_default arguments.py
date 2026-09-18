# def net_price(list_price,discount,max):
#
#     return list_price*(1-discount)*(1+max)
# print(net_price(1000,0.05,0.01))
#
#
# def net_price(list_price,discount=0.05,max=0):
#     return list_price*(1-discount)+max
# print(net_price(1000))

# import time
# def count(start, end):
#
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Time Up!")
#
# count(0,10)

import time
def count(start, end=5):#默认值在后，不然报错

    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Time Up!")

count(0)

