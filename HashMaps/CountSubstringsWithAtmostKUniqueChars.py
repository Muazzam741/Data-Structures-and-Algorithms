def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    memo = {}
    distinct = 0
    release = 0
    answer = 0

    for acquire in range(len(s)):
        element = s[acquire]
        if element in memo:
            memo[element] = memo[element] + 1
        else:
            memo[element] = 1
            distinct += 1
        
        while(release < acquire and distinct > k):
            discardChar = s[release]
            release += 1
            memo[discardChar] -= 1
            if memo[discardChar] == 0:
                memo.pop(discardChar)
                distinct -= 1
        answer += acquire - release + 1
    return answer