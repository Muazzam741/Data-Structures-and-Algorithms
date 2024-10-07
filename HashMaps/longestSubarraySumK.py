class Solution:
    def lenOfLongSubarr (self, arr, n, k) :
        #Complete the function
        memo = {}
        answer = 0
        prefixSum = 0
        memo[prefixSum] = -1
        for i in range(len(arr)):
            prefixSum += arr[i]
            if (prefixSum - k) in memo:
                answer = max(answer, i - memo[prefixSum - k])

            if prefixSum not in memo:
                memo[prefixSum] = i

        return answer