#Code:
number = 153
temp = number
add_sum = 0
while temp != 0:
    k = temp % 10
    add_sum += k*k*k
    temp = temp//10
if add_sum == number:
    print('Given number is a three-digit Armstrong Number')
else:
    print('Given number is not an Armstrong Number')

#Code:
number = 1634
digits = len(str(number))
temp = number
add_sum = 0
while temp != 0:
    # get the last digit in the number
    k = temp % 10
    add_sum += k**digits
    temp = temp//10
if add_sum == number:
    print('Given number is an Armstrong Number')
else:
    print('Given number is not a Armstrong Number')

