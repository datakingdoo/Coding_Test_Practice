def solution(n, k):

    answer = n*12000 + (k-n//10)*2000

    return answer

solution(10, 3)
print(solution(64,6))