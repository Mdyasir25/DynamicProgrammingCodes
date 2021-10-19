def nWaysSum(num, target, numlen):
    count = [0 for i in range(target+1)]

    #base case
    count[0] = 1

    for i in range(1, target+1):
        for j in range(numlen):
            if num[j] <= i:
                count += count[i - num[j]]
    return count[-1]

arr = [1, 5, 6]
m = len(arr)
N = 7
print("Total number of ways = ", nWaysSum(arr, N, m))
