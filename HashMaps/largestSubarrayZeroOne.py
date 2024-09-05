def largestArray(arr):
    memo = {}
    prefixSum = 0
    answer = 0
    memo[prefixSum] = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            prefixSum += -1

        else:
            prefixSum += 1
        if prefixSum in memo:
            answer = max(answer, i - memo[prefixSum])

        else:
            memo[prefixSum] = i

    return answer
print(largestArray([0,1,0,1]))

