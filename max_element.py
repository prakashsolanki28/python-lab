item_no = [5, 6, 7, 8, 8]

max_no = max(item_no)
highest = [max_no for _ in range(item_no.count(max_no))]
print(highest)  # -> [8, 8]


item_no = [5, 6, 7, 8, 8]
max_no = 0  # Note 1 
for i in item_no:
    if i > max_no:
        max_no = i
        high = [i]
    elif i == max_no:
        high.append(i)

print(max_no)


