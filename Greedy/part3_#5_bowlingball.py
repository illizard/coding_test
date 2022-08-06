# part3_#5_bowlingball.py
# greedy 

import random

#조건에 맞는 n_number, m_max_weight를 제어하고, k_weight_list를 만든다.
def calculate_matrix(n_number, m_max_weight):
    if n_number >= 1 and n_number <= 1000:  #조건에 맞게 n_number 컨트롤   
        if m_max_weight >= 1 and m_max_weight <= 10:
            k_weight_list = [random.randint(1,m_max_weight) for each_ball in range(n_number)]
            print(k_weight_list)
        else: 
            print('wrong max weight')
    else: #number 범위가 아니면 예외처리 
        print('wrong number')
    #만들어진 k_weight_list를 matrix 형태로 만들어서 i, j를 이터레이션 돌리는 인접행렬로 만들어서 서로의 연결성을 cnt에 담는다.
    cnt = 0 
    for i in k_weight_list: 
        for j in k_weight_list:     #2중 for문으로 매트릭스 형태 만듦(i,j는 2사람이라서) 
            if i != j:                      #i와 j가 같으면 안되므로(회로 금지, 자기 자신을 또 뽑을 수는 없음, 비복원추출) & 같은 무게 금지 
                cnt+=1
            else: 
                pass
    final_cnt = cnt // 2 # 행렬의 대각성분중 상위대각성분만 가져오면됨, 중복되는 연결 중에 하나만 가져오면 됨. 
    return final_cnt

def main(final_cnt):
    print(f'total count is: {final_cnt}')
    return 0

if __name__ == "__main__":   
    #initialize the number of ball, max_weight of each ball and ball list
    n_number = int(input('input the number of ball: \n'))
    m_max_weight = int(input('input the weight of ball: \n'))
    final_cnt = calculate_matrix(n_number, m_max_weight)
    main(final_cnt)




# 실행시간 1초 이내 
# 매트릭스로 짤 수는 없을까? for 문 돌리는 데 시간이 오래 걸리나?  
# row = n 
# col = m
# mat 2개 비교    

# int(input(
# k_weight_list = [random.randint(1,m_max_weight) for each_ball in range(n_number)]
# if n_number >= 1 and n_number <= 1000: