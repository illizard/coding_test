import re 

def solution(s):
    answer = []
    s = s[1:-1]
    pattern = '\{[^\{\}]*\}'
    str_list = re.findall(pattern, s)
    str_list.sort(key=len) #print(str_list.sort(key=len))하면 None 뜸
    
    sorted_str_list=[]
    for i in str_list:
        sorted_str_list.append(str(i[1:-1]).split(','))

    answer.append(int(list(sorted_str_list[0])[0]))
    for idx in range(len(sorted_str_list)-1):
        plus = set(sorted_str_list[idx+1]) - set(sorted_str_list[idx]) #앞선 값과 이전 값과의 차집합
        answer.append(int(''.join(list(str(plus)[1:-1])[1:-1])))
    return answer
    
if __name__=="__main__":
    s = "{{20,111},{111}}"		
    solution(s)