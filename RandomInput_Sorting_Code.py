import random
import time
from sys import setrecursionlimit
setrecursionlimit(100000)

### INSERTION SORT FUNCTION ###
def InsertionSort(array):
    for index in range(1, len(array)):
        key = array[index]
        j = index - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j=j-1
        array[j + 1] = key

### INSERTION SORT FOR MODIFIED QUICK SORT ###
def InsertionSort_10subarrays(alist,left,right):
    for k in range(left,right+1):
        key1=alist[k]
        l=k-1
        while l>=0 and key1 < alist[l]:
            alist[l+1]=alist[l]
            l=l-1
        alist[l+1]=key1

### MERGE SORT FUNCTION ###
def MergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2
        Left = array[:middle]
        Right = array[middle:]
        MergeSort(Left)
        MergeSort(Right)
        i=0
        j=0
        k=0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k +=1

### HEAP SORT FUNCTION(BUILD AND REMOVE) ###
class HEAP:
    def __init__(self):
        self.heaplist = [0]
        self.length = 0

    def buildheap(self, item):
        self.heaplist.append(item)
        self.length = self.length + 1
        self.UpHeap(self.length)

    def UpHeap(self, j):
        while j // 2 > 0:
            if self.heaplist[j] < self.heaplist[j // 2]:
                self.heaplist[j // 2], self.heaplist[j] = self.heaplist[j], self.heaplist[j // 2]
            j= j // 2

    def removemin(self):
        root = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.length]
        self.length = self.length - 1
        self.heaplist.pop()
        self.Downheap(1)
        return root

    def Downheap(self, i):
        while (2*i) <= self.length:
            m = self.minimum(i)
            if self.heaplist[i] > self.heaplist[m]:
                self.heaplist[i], self.heaplist[m] = self.heaplist[m], self.heaplist[i]
            i = m

    def minimum(self, l):
        if 2*l+1 > self.length:
            return 2*l
        else:
            if self.heaplist[2*l] < self.heaplist[2*l+1]:
                return 2*l
            else:
                return 2*l+1

def heapSort(input):
    hlist = HEAP()
    o = []
    i = 0
    for item in input:
        hlist.buildheap(item)
    while i < len(input):
        min = hlist.removemin()
        o.append(min)
        i += 1
    return o

### INPLACE QUICK SORT FUNCTION ###
def InplaceQuickSort(array):
    def sorting(input, left, right):
        if right <= left:
            return
        pivot_index = random.randint(left, right)
        input[left], input[pivot_index] = input[pivot_index], input[left]
        i = left
        for j in range(left + 1, right + 1):
            if input[j] < input[left]:
                i += 1
                input[i], input[j] = input[j], input[i]
        input[i], input[left] = input[left], input[i]
        sorting(input, left, i - 1)
        sorting(input, i + 1, right)
    sorting(array, 0, len(array) - 1)

### MODIFIED QUICK SORT FUNCTION ###
def ModifiedQuickSort(input,left,right):
    if(left+10<=right):
        pivot=median(input,left,right)
        i=left
        j=right-2
        done=True
        while done:
            while(input[i]<pivot):
                i=i+1
            while(pivot<input[j]):
                j=j-1
            if(i<j):
                input[i],input[j]=input[j],input[i]
            else:
                done=False
        input[i],input[right-1]=input[right-1],input[i]
        ModifiedQuickSort(input,left,i-1)
        ModifiedQuickSort(input,i+1,right)
    else:
        InsertionSort_10subarrays(input,left,right)

def median(input,left,right):
    center=(left+right)//2
    if(input[center]<input[left]):
        input[left],input[center]=input[center],input[left]
    if (input[right] < input[left]):
        input[left], input[right] = input[right], input[left]
    if (input[right] < input[center]):
        input[right], input[center] = input[center], input[right]
    input[center],input[right-1]=input[right-1],input[center]
    return input[right-1]

### DRIVER AND MAIN CODE ###
def callingsorts(randominput,Start,n):
    InsertionInput=list(randominput)
    InplaceQuickInput = list(randominput)
    MergeInput=list(randominput)
    ModifiedQuickInput = list(randominput)
    l = len(ModifiedQuickInput)

    ### CALLING INSERTION SORT ###
    print("\n\n FOR " + str(Start) + " INPUT SIZE : \n")
    print(" Random Input : " + str(InsertionInput))
    InsertStart = time.time()
    InsertionSort(InsertionInput)
    InsertEnd = time.time()
    print(" Insertion Sort : " + str(InsertionInput))
    print(" Execution Time : " + str((InsertEnd - InsertStart) * 1000) + " ms ")
    print("***********************************************************************")

    ### CALLING MERGE SORT ###
    print(" Random Input : " + str(MergeInput))
    MergeStart = time.time()
    MergeSort(MergeInput)
    MergeEnd = time.time()
    print(" Merge Sort : " + str(MergeInput))
    print(" Execution Time : " + str((MergeEnd - MergeStart) * 1000) + " ms ")
    print("***********************************************************************")

    ### CALLING HEAP SORT ###
    global output
    output = []
    HeapStart = time.time()
    output = heapSort(randominput)
    HeapEnd= time.time()
    print(" Random Input : " + str(randominput))
    print(" Heap Sort : " + str(output))
    print(" Execution Time : " + str((HeapEnd - HeapStart) * 1000) + " ms ")
    print("***********************************************************************")

    ### CALLING INPLACE QUICK SORT ###
    print(" Random Input : " + str(InplaceQuickInput))
    InplaceQuickStart = time.time()
    InplaceQuickSort(InplaceQuickInput)
    InplaceQuickEnd = time.time()
    print(" Inplace Quick Sort : " + str(InplaceQuickInput))
    print(" Execution Time : " + str((InplaceQuickEnd - InplaceQuickStart) * 1000) + "ms")
    print("***********************************************************************")

    ### CALLING MODIFIED QUICK SORT ###
    print(" Random Input : " + str(ModifiedQuickInput))
    ModifiedQuickStart = time.time()
    ModifiedQuickSort(ModifiedQuickInput, 0, l - 1)
    ModifiedQuickEnd = time.time()
    print(" Modified Quick Sort : " + str(ModifiedQuickInput))
    print(" Execution Time : " + str((ModifiedQuickEnd - ModifiedQuickStart) * 1000) + "ms")

def main(input_sizes_range,startrange,endrange):
    for i in range(startrange,endrange):
        INPUT = random.sample(range(1, 60000), input_sizes_range[i])
        #INPUT=sorted(INPUT)
        n=len(INPUT)
        global heaplist
        heaplist = []
        callingsorts(INPUT,input_sizes_range[i],n)

randominput=[]
input_sizes_range=[1000,2000,4000,5000,10000,20000,30000,40000,50000]
main(input_sizes_range,0,len(input_sizes_range))

