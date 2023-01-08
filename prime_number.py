a=2
num=13
if num%a==0 & a!=num:
    print('not prime')
else: # loop not exited via break
  print('prime')


for a in range(a, num):
    if a % num == 0:
        print('not prime')
        break
else: # loop not exited via break
    print('prime')


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
