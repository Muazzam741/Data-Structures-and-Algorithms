def countDistinct(arr, k):
    memo = {}
    distinct = 0
    answer = []

    for i in range(k):
        currentVal = arr[i]
        if currentVal in memo:
            memo[currentVal] += 1

        else:
            memo[currentVal] = 1
            distinct += 1


    answer.append(distinct)
    release = 0

    for acquire in range(k, len(arr)):
        discardElement = arr[release]
        memo[discardElement] -= 1
        release += 1

        if memo[discardElement] == 0:
            memo.pop(discardElement)
            distinct -= 1

        currentVal = arr[acquire]
        if currentVal in memo:
            memo[currentVal] += 1

        else:
            memo[currentVal] = 1
            distinct += 1

        answer.append(distinct)

    return answer