import subsetsum


def equalSumPartition(arr):
    lenarr = len(arr)
    arrsum = sum(arr)

    if arrsum % 2 != 0:
        return False
    else:
        return subsetsum.SubsetSum(arr, lenarr, arrsum // 2)


# print(equalSumPartition([1, 3, 2, 3, 6, 1, 8]))

def minSubsetDifference(arr):
    arrsum = sum(arr)
    arrlen = len(arr)

    i = arrsum//2
    while i >= 0:
        if subsetsum.SubsetSum(arr, arrlen, i):
            return arrsum - 2*i
        i -= 1

print(minSubsetDifference([1 ,2, 7]))
