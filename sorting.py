print("Sorting in Descending order")
list = []
n=int(input("How many number you want to sort"))
for k in range(n):
    input2 = int(input("Enter the values"))
    list.append(input2)

print(list)
for i in range(len(list)):
    j = i + 1
    while (j < len(list)):
        if list[i] < list[j]:
            temp = list[j]
            list[j] = list[i]
            list[i] = temp
        j += 1
print("Descending order ", list)