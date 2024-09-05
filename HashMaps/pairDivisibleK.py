def checkPair(k, arr):
    memo = [0] * k

    for num in arr:
        currentRem = ((num % k) + k) % k
        memo[currentRem] += 1

    for i in range(int(k/2) + 1):
        if i == 0:
            if memo[i] % 2 != 0:
                return False
        else:
            y = k - i
            if memo[i] != memo[y]:
                return False

    return True

    return memo

print(checkPair(7, [1,2,3,4,5,6]))