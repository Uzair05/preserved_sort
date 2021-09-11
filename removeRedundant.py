from typing import List, Tuple
from math import floor
import io


class node:
    def __init__(self, loc: int, val: str) -> None:
        self.loc = loc
        self.val = val


def mergeSortLoc(arr: List[node]) -> None:
    if len(arr) > 1:
        mid: int = len(arr) // 2  # Finding the mid of the array
        L: List[node] = arr[:mid]  # Dividing the array elements
        R: List[node] = arr[mid:]  # into 2 halves

        mergeSortLoc(L)  # Sorting the first half
        mergeSortLoc(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].loc < R[j].loc:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def mergeSortVal(arr: List[node]) -> None:
    if len(arr) > 1:
        mid: int = len(arr) // 2  # Finding the mid of the array
        L: List[node] = arr[:mid]  # Dividing the array elements
        R: List[node] = arr[mid:]  # into 2 halves

        mergeSortVal(L)  # Sorting the first half
        mergeSortVal(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].val < R[j].val:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def binarySearch(src, arr: List[int], st: int = 0, en: int = None) -> int:

    if en == None:
        en = len(arr)

    while (en > st):
        mid: int = floor((en + st) / 2)
        if (arr[mid].val == src):
            return mid
        elif (arr[mid].val > src):
            en = mid
        else:
            st = mid
    return -1


def readFile(filepath: str) -> List[Tuple[int, str]]:
    tupled_entries: List[Tuple[int, str]] = []
    with io.open(filepath, 'r', encoding='UTF-8', errors='replace') as file:
        con = file.read()
        con = con.split('\n')
        tupled_entries = list(enumerate(con))
        file.close()
    return tupled_entries


def writeResultsToFile(arr: List[node], path_to_file: str) -> None:
    #writes in file of same extension
    splited_filename: List[str] = path_to_file.split('.')
    temp_filename: str = "./output_resolution." + splited_filename[-1]

    with io.open(temp_filename, 'w', encoding='UTF-8',
                 errors='replace') as outfile:
        for i in arr:
            outfile.write(i.val)
            outfile.write('\n')
        outfile.close()


def processBaseEntries(arr: List[Tuple[int, str]]) -> List[node]:
    processedEntries: List[node] = []
    for i in arr:
        processedEntries.append(node(loc=i[0], val=i[1]))
    return processedEntries


def reduceArray(arr: List[node], st: int, pt: int) -> node:
    min_location_value = arr[st].loc
    for i in range(st, pt, +1):
        if arr[i].loc < min_location_value:
            min_location_value = arr[i].loc
    return node(val=arr[st].val, loc=min_location_value)


def listDuplicates(arr: List[node], st: int = 0) -> int:
    pt = st
    array_len = len(arr)
    while ((pt < array_len) and (arr[pt].val == arr[st].val)):
        pt += 1
    return pt


def elimenateDuplicates(arr: List[node]) -> List[node]:
    res: List[node] = []  # will hold result
    st = 0
    while (st < len(arr)):
        pt = listDuplicates(arr, st)
        if (pt - st > 1):
            # we dont want to remove whitespace and hurt readability
            if arr[st].val == '':
                res.extend(arr[st:pt])
            else:
                res.append(reduceArray(arr, st, pt))
        else:
            res.append(arr[st])
        st = pt
    return res


def main():
    path_to_file = str(input("Get File Name:\t"))
    unprocessed_reads = readFile(path_to_file)
    reads = processBaseEntries(unprocessed_reads)
    mergeSortVal(reads)
    reads = elimenateDuplicates(reads)
    mergeSortLoc(reads)
    writeResultsToFile(reads, path_to_file)


if __name__ == "__main__":
    main()