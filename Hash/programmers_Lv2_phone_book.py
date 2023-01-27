# case 1
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     new_book = phone_book[1:]
#     cnt = 0
    
#     for i in new_book:
#         res = i.find(phone_book[0])
#         if res!=-1: # prefix가 있는 경우=find가 된 경우==int => False
#             cnt+=1
#             break
#         elif res==-1: #prefix가 없는 경우=find가 안된 경우==-1 => True
#             pass
            
#     if cnt > 0:
#         return False
#     return answer

# case 2
# 정확성: 79.2
# 효율성: 16.7
# 합계: 95.8 / 100.0
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     cnt = 0    
#     for idx in range(len(phone_book)-1):
#         if phone_book[idx+1].find(phone_book[idx])!=-1:
#             cnt+=1
#             break
#         elif phone_book[idx].find(phone_book[idx+1])==-1:
#             pass

#     if cnt > 0:
#         return False

#     return answer

# case 3

def solution(phone_book):
    answer = True
    phone_book.sort()
    cnt = 0    
    for idx in range(len(phone_book)-1):
        if phone_book[idx+1].find(phone_book[idx])==0:
            cnt+=1
            break
        elif phone_book[idx].find(phone_book[idx+1])==-1:
            pass

    if cnt > 0:
        return False

    return answer

if __name__ == '__main__':
    phone_book = ["12","123","1235","567","88"]
    solution(phone_book)

