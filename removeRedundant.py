import sys

def mergeSort(arr, fn=None):
    if len(arr) <= 1:
        return arr
    else:
        p = len(arr)//2
        larr = mergeSort(arr[:p], fn)
        rarr = mergeSort(arr[p:], fn)
        n_arr = []
        while ((len(larr) > 0) and (len(rarr) > 0)):
            if fn is None:
                if larr[0] < rarr[0]:
                    n_arr.append(larr.pop(0))
                else:
                    n_arr.append(rarr.pop(0))
            else:
                if fn(larr[0]) < fn(rarr[0]):
                    n_arr.append(larr.pop(0))
                else:
                    n_arr.append(rarr.pop(0))
        if len(larr) > 0:
            n_arr.extend(larr)
        if len(rarr) > 0:
            n_arr.extend(rarr)
        return n_arr

def binarySearch(item, arr, fn = lambda x: x):

    if (len(arr) == 0):
        return -1
    if (len(arr) == 1):
        if item == fn(arr[0]):
            return 0
        else:
            return -1

    if len(arr)>1:
        start, end = 0, len(arr)
        while not(end <= start):
            mid = (start+end)//2
            
            if item == fn(arr[mid]):
                return mid
            elif item > fn(arr[mid]):
                start = mid + 1
            else:
                end = mid

        return -1    

def main():
    with open(sys.argv[1], 'r') as file:
        
        l_ = mergeSort([(i, l[:-1]) for i, l in enumerate(file.readlines())], lambda x:x[1])

        l__ = []
        for li in l_:
            if li[1] == "":
                l__.append(li)
                continue

            idx = binarySearch(li[1], l__, lambda x: x[1])
            if idx == -1:
                l__.append(li)
            else:
                if l__[idx][0] > li[0]:
                    l__[idx] = li
                    
        del(l_)
        l__ = mergeSort(l__, lambda x:x[0])

        name = ".".join(sys.argv[1].split(".")[:-1]), sys.argv[1].split(".")[-1]

        with open(f"{name[0]}_.{name[1]}", 'w') as out_file:
            out_file.writelines([f"{i[1]}\n" for i in l__])
            
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()