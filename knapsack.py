t = [[-1] * 500] * 500
def knapsack(wt, vl, w, n):
#     print(t)
    if n == 0 or w == 0:
        return 0
    if t[w][n] != -1:
        return t[w][n]
    if wt[n-1] <= w:
        t[w][n] = max(vl[n-1] + knapsack(wt, vl, w - wt[n-1], n - 1), knapsack(wt, vl, w, n - 1))
        return t[w][n]
    elif wt[n-1] > w:
        t[w][n] = knapsack(wt, vl, w, n - 1)
        return t[w][n]
if __name__ == "__main__":
    print(knapsack([10, 20, 30], [60, 100, 120], 50, 3))
