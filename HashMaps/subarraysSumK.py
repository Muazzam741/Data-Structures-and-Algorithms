def subarrays(arr, k):
    answer = 0
    prefixSum = 0
    memo = {}
    memo[prefixSum] = 1
    for num in nums:
        prefixSum += num

        if (prefixSum - k) in memo:
            answer += memo[prefixSum - k]

        if prefixSum in memo:
            memo[prefixSum] += 1
        else:
            memo[prefixSum] = 1

    return answer