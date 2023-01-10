elements = [4,2,1,10,5,3,100]

for i in range(len(elements)):
    mini = min(elements[i:])
    min_index = elements[i:].index(mini) #find index of minimum element
    elements[i + min_index] = elements[i] #replace element at min_index with first element
    elements[i] = mini                  #replace first element with min element

print(elements)