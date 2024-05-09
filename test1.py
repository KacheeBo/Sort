import random
import time
a = list(random.randint(1,100000) for _ in range(10001))
time_start = time.time()
# 冒泡排序
'''for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
'''

# 选择排序
'''for i in range(0,len(a)):
    m = i
    for j in range(i + 1, len(a)):
        if (a[j] < a[m]):
            m = j
    a[m],a[i] = a[i],a[m]
'''

# 快速排序
'''def parttion(a, low, high):
        pivotkey = a[low]
        while (low < high):
            while (low < high and a[high] >= pivotkey):
                high -= 1
            a[low] = a[high]
            while (low < high and a[low] <= pivotkey):
                low += 1
            a[high] = a[low]
        a[low] = pivotkey
        return low
 
def quick_sort(a, low, high):
    if (low < high):
        pivotloc = parttion(a, low, high)
        quick_sort(a, low, pivotloc - 1)
        quick_sort(a, pivotloc + 1, high)
    return
quick_sort(a,0,len(a)-1)
'''

# 归并排序
def merge_sort(ary):
    if len(ary) <= 1:
        return ary
    median = int(len(ary)/2) 
    left = merge_sort(ary[:median])
    right = merge_sort(ary[median:])
    return merge(left, right) 
    
def merge(left, right):
    res = []
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1        
        res = res + left[i:] + right[j:]
        return res

merge_sort(a)
time_end = time.time()
time_c = time_end - time_start
print(a)
print(time_c)
 
