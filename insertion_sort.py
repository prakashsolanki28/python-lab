def ins_sort(k):
    for i in range(1,len(k)):
        j = i
        temp = k[j]
        while j > 0 and temp < k[j-1]:
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp
    return k

elements = [4,2,1,10,5,3,100]

ins_sort(elements)
print(elements)
