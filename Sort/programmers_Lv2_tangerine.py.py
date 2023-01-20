from collections import Counter

def solution(k, tangerine):
    answer=0
    new_list=[]
    for tan,cnt in Counter(tangerine).most_common():
        for i in range(cnt):
            new_list.append(tan)
    answer = len(list(set(new_list[:k])))
    
    return answer


if __name__=='__main__':
    k =	4
    tangerine =  [1, 3, 2, 5, 4, 5, 2, 3]	

    solution(k, tangerine)


#least_common = Counter(tangerine).most_common()[-1] 최소값 구하기 
#무슨 문제 인지는 모르겠네 counting_sort?