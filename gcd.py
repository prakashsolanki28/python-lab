def compute_hcf(x, y):
# find the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)

