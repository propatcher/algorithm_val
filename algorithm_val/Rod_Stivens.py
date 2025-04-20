def FindLargest(array1):
    largest = array1[0] # O(1)
    for i in range(len(array1)): #O(n)
        if array1[i] > largest:
            largest = array1[i]
    return largest #O(1)
    # in sum O(1 + n + 1) = O(2+n)
def ContainsDuplicates(array2):
    for i in range(len(array2)):
        for j in range(i + 1, len(array2)):
            if array2[i] == array2[j]:
                return True
    return False # O(n^2)
def DividingPoint(array3):
    number1 = array3[0]
    number2 = array3[-1]
    number3 = array3[5]
    
    if number1 > number2 and number1 < number3:
        return number1
    elif number2 > number1 and number2 < number3:
        return number2
    else:
        return number3
print(DividingPoint([1,2,65,435,4,2,1,4,35,4,5,6,6,4]))
    
