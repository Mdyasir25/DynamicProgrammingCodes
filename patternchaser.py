def patternchaser(s):
    counter = 1
    lo1 = 0
    hi1 = len(s) // 2 - 1
    while hi1 - lo1 > 0:
        n = s[lo1:hi1+1]
        lo2 = hi1 + 1
        hi2 = hi1 + (hi1+1 - lo1)
        while hi2 < len(s):
            t = s[lo2:hi2+1]
            if n == t:
                return "Yes", n
            lo2 += 1
            hi2 += 1
        hi1 += 1
        lo1 += 1
        if hi1 >= len(s) // 2:
            lo1 = 0
            hi1 = len(s)//2 - counter - 1
            counter += 1
    return "No", "Null"

if __name__ == "__main__":
    print(patternchaser("aa2bbbaacbbb"))