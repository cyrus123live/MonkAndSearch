def findNum(num, array):
    l = 0
    r = len(array) - 1
    while(l < r):
        mid = ( l + (r - 1) ) // 2
        ##print("l = " + str(l) + " and r = " + str(r))
        if(array[mid] == num):
            return mid
        elif(array[mid] < num):
            l = mid + 1
        elif(array[mid] > num):
            r = mid - 1
    return -1

size = int(input())

array = input().split(" ")
intArray = []

for i in range(size):
    intArray.append(int(array[i]))

numOfQueries = int(input())

for i in range(numOfQueries):
    array = input().split(" ")
    index = findNum(int(array[1]), intArray)
    if (index != -1):
        if (int(array[0]) == 0):
            print(len(intArray) - index)
        else:
            print(len(intArray) - index - 1)
    else:
        print(0)
