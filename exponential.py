num = int(input("Enter a number -: "))
expo = int(input("Enter a exponent -: "))
result = 1
for i in range(0,expo):
    result = result * num
    print(result)

print("Exponential is -: ",result)
