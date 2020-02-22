# -*- coding: utf-8 -*-
# @File   : sort_algorithm.py
# @Author : Runpeng Zhang
# @Date   : 2020/2/22
# @Desc   : 用Python 手写十大经典排序算法


def bubbleSort(arr: list):
    """
    冒泡排序：对第二个到最后一个数，逐次遍历前面的数字大小对换
    :rtype: 排序后的数组，list
    """
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSort(arr):
    """
    选择排序：对除了最后一个数的每个数，逐个遍历后面的数字找到最小的数字
    :rtype: 排序后的数组，list
    """
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


def insertionSort(arr):
    """
    插入排序：对数组中的每个数，逐个往前遍历，如果比其大，则后移，
    直到找到比其小，则有空位插入。
    :rtype: 排序后的数组，list
    """
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr


def shellSort(arr):
    """
    希尔排序：对待排序的数组分割成若干个子序直接进行直接插入排序，
    待整个数组的记录“基本有序”时，再对全体记录进行依次直接插入排序。
    :rtype: 排序后的数组，list
    """
    import math
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)  # floor() 返回数字的下舍整数
    return arr


def mergeSort(arr):
    """
    归并排序：对数据逐次递归拆成两份
    :rtype: 返回排序后的数组，这里递归左右两个数组
    """
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0: middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    """
    对左右两个序列进行排除合并
    :rtype: 排序后的数组
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def quickSort(arr, left=None, right=None):
    """
    快速排序：从数据中找到基准，比基准小的放在基准前面，比基准大的放在基准后面
    :rtype: 排序后的数组
    """
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    """
    快速排序，基准划分
    :rtype: int,基准序号
    """
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def Qsort_main(arr):
    return QSort(arr, 0, len(arr) - 1)


def QSort(arr, left, right):
    """
    快速排序：从数据中找到基准，比基准小的放在基准前面，比基准大的放基准后面
    :rtype: object
    """
    if left < right:
        privotloc = QSort_partitaion(arr, left, right)
        QSort(arr, left, privotloc - 1)
        QSort(arr, privotloc + 1, right)
    return arr


def QSort_partitaion(arr, low, high):
    """
    快速排序基准划分，返回基准
    :rtype: object
    """
    if low > high:
        return -1
    tmp = arr[low]
    while low < high:
        while low < high and arr[high] >= tmp:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= tmp:
            low += 1
        arr[high] = arr[low]
    arr[low] = tmp
    return low


def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def heapSort(arr):
    """
    堆排序：建立堆
    :rtype: object
    """
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


def countingSort(arr):
    """
    计数排序：将输入的数据值转化为健存储在额外开辟的数组空间
    :rtype: 排序后的数组
    """
    maxValue = max(arr)
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr


def bucketSort(arr):
    """
    桶排序
    :rtype: 排序好的数组，list
    """
    minNum = min(arr)
    maxNum = max(arr)
    # 桶的大小
    bucketRange = (maxNum - minNum) / len(arr)
    # 桶数组
    countList = [[] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        countList[int((i - minNum) // bucketRange)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in countList:
        for j in sorted(i):
            arr.append(j)
    return arr


def RadixSort(arr):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1（包含0）
    maxNum = max(arr)  # 得到带排序数组中最大数
    while maxNum > 10 ** n:  # 得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])  # 将每个桶置空
        for x in arr:  # 对每一位进行排序
            radix = int((x / (10 ** i)) % 10)  # 得到每位的基数
            bucket[radix].append(x)  # 将对应的数组元素加入到相应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:  # 若桶不为空
                for y in bucket[k]:  # 将该桶中每个元素
                    arr[j] = y  # 放回到数组中
                    j += 1
        i += 1
    return arr


def main():
    arr = [1, 3, 2, 0]
    print(RadixSort(arr))


if __name__ == '__main__':
    main()
