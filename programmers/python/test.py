def solution(lottos, win_nums):
    answer = []
    print(lottos)
    print(win_nums)
    max = lottos.count(0)
    tmpList = lottos + win_nums
    result1 = set(tmpList)
    result2 = list(result1)
    print(result2)
    min = len(result2) - 6
    print(min, min+max)
    return answer



solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])
