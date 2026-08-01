list = [12,15,3,45,21,7,17,9,10,38]

for i in range(len(list)-1):
    if list[i] < list[i+1]:
        continue
    else:
        print("The list is not sorted in ascending order.")
        break
else:
    print("The list is sorted in ascending order.")

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(f"The sorted list is: {list}")