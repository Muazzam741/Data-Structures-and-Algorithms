class Solution:
    def maxLen(self, n, arr):
        #Code here
        return self.maxLength({}, n, arr)
    
    def maxLength(self, memo, n, arr):
        prefixSum = 0
        answer = 0
        
        memo[prefixSum] = -1
        
        for i in range(len(arr)):
            prefixSum += arr[i]
            if prefixSum in memo:
                answer = max(answer, i - memo[prefixSum])
            else:
                memo[prefixSum] = 1
        
        return answer

new = Solution()
print(new.maxLen(8, [15,-2,2,-8,1,7,10,23]))