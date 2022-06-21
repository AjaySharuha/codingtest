list = [4, 1, 9, 10, 15, 22, 5, 14, 1, 2 , 4 , 5 , 6 ,1 , 3 , 7 , 9 ,10]
for i in list:
    dividee = i % 2
    if dividee == 0:
        list.remove(i)
print(list)
arr = list 
print("Repeated elements: ")
#Searches for duplicate element.
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] == arr[j]):
            print(arr[j])