### -------------------[정렬] bubble sort------------------- ###
lst = list(range(12, 0, -1))
print(lst)

for i in range(len(lst)-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

### -------------------[부분집합] 반복문과 배열------------------- ###
arr = [1, 2, 3]
subsets = [[]]

for num in arr:
    size = len(subsets)
    for i in range(size):
        subsets.append(subsets[i]+[num])
print(subsets)

### -------------------[Recursive func. factorial]------------------- ###
def fact(n):
    if n == 1:
        return 1
    else:
        return n*(fact(n-1))

### -------------------[Recursive func. fibonacci]------------------- ###
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)