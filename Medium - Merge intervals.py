def merge(intervals):

    n = len(intervals)
    
    intervals.sort(key = lambda x: x[0])
    result = [intervals[0]]


    for i in range(1,n):

        curr_start, curr_end = intervals[i]
        prev_start, prev_end = result[-1]

        if prev_end >= curr_start:

            result[-1] = [prev_start,max(curr_end,prev_end)]

        else: result.append(intervals[i])

    return result
    





intervals = [[1,3],[2,6],[8,10],[15,18]]
result = [[1,6],[8,10],[15,18]]

print(merge(intervals))