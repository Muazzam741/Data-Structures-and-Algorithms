class Solution:

    # Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self, arr, n):
        # Your code here
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1

        return self.findAnswer(arr, {})

    def findAnswer(self, arr, memo):
        prefixSum = 0
        answer = 0
        memo[prefixSum] = 1

        for i in range(len(arr)):
            prefixSum += arr[i]

            if prefixSum in memo:
                answer += memo[prefixSum]
                memo[prefixSum] += 1
            else:
                memo[prefixSum] = 1

        return answer