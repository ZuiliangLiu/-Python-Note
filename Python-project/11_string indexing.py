credit_number = "123-456-789-0123"#num[x:y:z] x为起始点（包含），y为终点（不含），z为步长（默认为1）
# print(credit_number[5])#从0位开始算
# print(credit_number[0:3]) #包含起点，不包含终点
last_digits = credit_number[-4:]
print(last_digits)
credit_number = credit_number[::-1]#反转
print(credit_number)