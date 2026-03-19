#======================Рекурсия=================
# Рекурсия - техника при которой функция вызывает сама себя для решения подзадачи
# Обязательные элементы рекурсии:
# 1 Базовая (условие остановки рекурсии)
# 2 Рекурсивный случай ( вызов функции с упращенным аргументом)


# Рекурсия  читаемость(часто лучше)| память берет больше| медленнее
# Цикл чистаемость(иногда хуже)| память берет меньше| быстрее

factorial = 5
result = 1
for i in range(1, factorial+1):
    result*=i
    #result = result * i
print(result)

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))
# = 4 * factorial(4-1) -> 3 * factorial(3-1)
# = 4 * 3 * factorial(3-1) -> 2 * factorial(2-1)
# = 4 * 3 * 2 * 1 * factorial(1-1) -> 1
# = 4 * 3 * 2 * 1 * 1 

#не правильно!!!! причина нету остановки рекурсии
# def a():
#     return a()
# a()

list1 = [1, 2, 3, 4]
result = 0
for i in list1:
    result+=i

print(result)

def sum_list(list1: list[int]) -> int:
    if not list1:
        return 0
    return list1[0] + sum_list(list1[1:])

print(sum_list(list1))


list_sort = [1, 2, 3, 4, 5]
target = 3
for index, value in enumerate(list_sort):
    if not target in list_sort:
        print(-1)
        break
    if value == target:
        print(index)

list_sort = [1, 2, 3, 4, 5]
def iterative_search(list_sort, target):
    for index, value in enumerate(list_sort):
        if value == target:
            return index
    return -1

print(iterative_search(list_sort, 2)) #1
print(iterative_search(list_sort, 10)) #-1

list_sort = [1, 2, 3, 4, 5]
def recursive_search(list_sort, target, index=0):
    if index >= len(list_sort):
        return -1
    if list_sort[index] == target:
        return index
    return recursive_search(list_sort, target, index+1)

print(recursive_search(list_sort, 5))
print(recursive_search(list_sort, 10))




list_sort = [1, 2, 3, 4, 5]
#============0==1==2==3==4
target = 2
# elif
left = 0
right = 4
mid = 2
right = 1

# else
target = 5

left = 0
right = 4
mid = 2
right = 4
left = +1

def binary_search(list_sort: list[int], target: int, left=0, right=None) -> int:
    if right is None:
        right = len(list_sort)-1
    
    if left > right:
        return -1
    mid = (left + right) // 2
    
    if list_sort[mid] == target:
        return mid
    elif target < list_sort[mid]:
        return binary_search(list_sort, target, left, mid - 1)
    else:
        return binary_search(list_sort, target, left+1, right)
list_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 4
print("binary search index", binary_search(list_sort, target))

"""
left  = 0
right = 14
mid = 7
list_sort[7] = 8
mid_element = 8
left = 0
right = 6
mid = 3 
list_sort[3] = 4 
"""


import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())