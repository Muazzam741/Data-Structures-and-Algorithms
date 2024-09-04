class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        return self.findAnswer({}, arr, n)
    
    def findAnswer(self, memo, arr, n):
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
