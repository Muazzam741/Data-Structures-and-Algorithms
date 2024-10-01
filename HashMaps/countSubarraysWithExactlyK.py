class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 1:
            atmostK = 0
            release = 0
            distinct = 0
            memo = {}
            for acquire in range(len(nums)):
                element = nums[acquire]
                if element in memo:
                    memo[element] = memo[element] + 1
                else:
                    memo[element] = 1
                    distinct += 1

                while (release < acquire and distinct > k):
                    discardChar = nums[release]
                    release += 1
                    memo[discardChar] -= 1
                    if memo[discardChar] == 0:
                        memo.pop(discardChar)
                        distinct -= 1
                atmostK += acquire - release + 1
            return atmostK
        else:
            memo = {}
            distinct = 0
            release = 0
            atmostK = 0
            atmostK1 = 0
            newK = k - 1
            # Substrings with atmost k unique characters
            for acquire in range(len(nums)):
                element = nums[acquire]
                if element in memo:
                    memo[element] = memo[element] + 1
                else:
                    memo[element] = 1
                    distinct += 1

                while (release < acquire and distinct > k):
                    discardChar = nums[release]
                    release += 1
                    memo[discardChar] -= 1
                    if memo[discardChar] == 0:
                        memo.pop(discardChar)
                        distinct -= 1
                atmostK += acquire - release + 1
            distinct = 0
            release = 0
            memo1 = {}
            # Substrings with atmost k-1 unique characters
            for i in range(len(nums)):
                element = nums[i]
                if element in memo1:
                    memo1[element] = memo1[element] + 1
                else:
                    memo1[element] = 1
                    distinct += 1

                while (release < acquire and distinct > newK):
                    discardChar = nums[release]
                    release += 1
                    memo1[discardChar] -= 1
                    if memo1[discardChar] == 0:
                        memo1.pop(discardChar)
                        distinct -= 1
                atmostK1 += i - release + 1

            return (atmostK - atmostK1)
