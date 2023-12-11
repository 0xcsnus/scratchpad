def solulu(s):

    start = end = maxLength = 0
    seen = {}

    while start <= end and end < len(s):

        ch  = s[end]

        if ch in seen and start <= seen[ch]:
            start = seen[ch] + 1

        seen[ch] = end
        maxLength = max(maxLength,end-start+1)
        end+=1

    return maxLength


s = "abcdabce"
print(solulu(s))
        