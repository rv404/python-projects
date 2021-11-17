def mySort(x):
    for i in range(len(x)):
        min_num = x[i]
        idx = i
        count = i
        for j in range(i, len(x)):
            if x[j] < min_num:
                min_num = x[j]
                idx = count
            count += 1
        temp = x[i]
        x[i] = min_num
        x[idx] = temp
    print(x)
    return x