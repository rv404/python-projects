def linearSearch(iterable, find):
    for i in range(len(iterable)):
        if find == iterable[i]:
            return True
    else:
        return False
            
def binarySearch(iterable, find, min_index, max_index):
    if max_index >= min_index:
        mid = (max_index + min_index)//2
        if find == iterable[mid]:
            return True
        elif find > iterable[mid]:
            return binarySearch(iterable, find, (mid+1), max_index)
        else:
            return binarySearch(iterable, find, min_index, (mid-1))
    else:
        return False