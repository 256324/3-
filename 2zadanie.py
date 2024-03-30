def binar_serch(list, nom):
    first = 0
    last = len(list)
    mid  = (first + last)//2
    while list[mid] != nom:
        if mid == last or mid == first:
            return "этого числа нет в массиве"
        if list[mid] > nom:
            last = mid
            mid = (first + last) // 2
        if list[mid] < nom:
            first = mid
            mid = (first + last) // 2
    return mid

list = [1, 5, 14, 27, 34, 56, 96]
a = binar_serch(list, 14)
print(a)