def dfs(numbers, target, idx, sum):
    if idx == len(numbers):
        if sum == target:
            return 1
        return 0 
    return dfs(numbers, target, idx+1, sum+numbers[idx]) + dfs(numbers, target, idx+1, sum-numbers[idx])

def solution(numbers, target):
    idx = 0
    sum = 0
    answer = dfs(numbers, target, idx, sum)
    print(answer)
    return answer

# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return

#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])

# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer

if __name__=="__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    solution(numbers, target)
