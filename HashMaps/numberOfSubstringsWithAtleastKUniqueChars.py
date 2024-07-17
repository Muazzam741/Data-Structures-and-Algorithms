def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    memo = {}
    distinct = 0
    release = 0
    answer = 0
    newK = k - 1
    n = len(s)

    for acquire in range(len(s)):
        element = s[acquire]
        if element in memo:
            memo[element] = memo[element] + 1
        else:
            memo[element] = 1
            distinct += 1
        
        while(release < acquire and distinct > newK):
            discardChar = s[release]
            release += 1
            memo[discardChar] -= 1
            if memo[discardChar] == 0:
                memo.pop(discardChar)
                distinct -= 1
        answer += acquire - release + 1
    return int((n*(n+1)/2) - answer)

print(countSubStrings('abcabcabcabc', 3))