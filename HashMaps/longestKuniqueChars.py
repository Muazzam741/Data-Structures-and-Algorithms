answer = 0
    distinct = 0
    memo = {}

    release = 0

    for acquire in range(len(s)):
        currentChar = s[acquire]

        if currentChar in memo:
            memo[currentChar] += 1

        else:
            memo[currentChar] = 1
            distinct += 1

        while(release <= acquire and distinct > k):
            discardChar = s[release]
            release += 1

            memo[discardChar] -= 1

            if memo[discardChar] == 0:
                memo.pop(discardChar)
                distinct -= 1

        answer = max(answer, acquire - release + 1)

    return answer