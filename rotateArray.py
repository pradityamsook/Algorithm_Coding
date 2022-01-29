# rotate from back to front.
# e.g. rotate 2 elements [1, 2, 3, 78, 66] -> [78, 66, 1, 2, 3] .
# "arr[:] = arr[n:lenArr] + arr[0:n]" this line will slice array follow start index to index was indentified
# and then it'l be restore in array was exist

# n is number of elements to rotate back to front.
def rotateArr(arr, n):
    lenArr = len(arr)
    n = lenArr - n
    arr[:] = arr[n:lenArr] + arr[0:n]
    return arr


if __name__ == '__main__':
    arr = [1, 569, 934, 5]
    arr = rotateArr(arr, 3)
    print(arr)
