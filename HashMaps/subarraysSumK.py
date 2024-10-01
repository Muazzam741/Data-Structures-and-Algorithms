def subarrays(arr, k):
    answer = 0
    prefixSum = 0
    memo = {}
    memo[prefixSum] = 0
    for num in nums:
        prefixSum += num

        if