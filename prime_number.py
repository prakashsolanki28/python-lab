a = 120
count = 0
for i in range(2,(a//2)):
    if(a % i == 0):
        count = 1

if count == 0:
    print("prime")
else:
    print("not prime")  