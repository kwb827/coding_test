def solution(numbers):
    import pandas as pd

    result = []

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])

    result = set(result)
    answer = list(result)
    return sorted(answer)


#입출력 1
print(solution([2, 1, 3, 4, 1]))
