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
        # if currentChar in memo and memo[currentChar] >= release:
        #     release = memo[currentChar] + 1

        answer = max(answer,i - release + 1)

    return answer
