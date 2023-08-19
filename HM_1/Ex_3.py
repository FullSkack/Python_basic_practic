n = 385916

n_1 = n//1000
sum_n1 = 0
while n_1 > 0:
    digit = n_1 % 10
    sum_n1 = sum_n1 + digit
    n_1 = n_1 // 10

# print(sum_n1)

n_2 = n%1000
sum_n2 = 0
while n_2 > 0:
    digit = n_2 % 10
    sum_n2 = sum_n2 + digit
    n_2 = n_2 // 10

# print(sum_n2)

if sum_n1 == sum_n2:
    print('yes')
else:
    print('no')