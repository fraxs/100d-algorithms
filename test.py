a= 2
b = 5
list1 = []
list1.append(a)
list1.append(b)
for i in range(len(list1)):
    list1[i] = str(list1[i])
x = ''.join(list1)
print(x)