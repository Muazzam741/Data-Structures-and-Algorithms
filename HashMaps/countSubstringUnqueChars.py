def unqueChars(s:str):
    memo = {}
    answer = 0
    release = 0
    for i in range(len(s)):
        currentChar = s[i]

        while release < acquire and currentChar in memo:
            discardChar = s[release]
            memo.pop(discardChar)
            release += 1

        memo[currentChar] = 1

        answer += acquire - release + 1

    return answer
