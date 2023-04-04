def solution(s):
    if len(s) < 3:
		return len(s)
	
    answer = len(s) 
    for step in range(1, len(s)//2 + 1):
        compressed = ""  
        prev = s[0:step]  
        count = 1  
        for j in range(step, len(s), step):
            
            if prev == s[j:j+step]:
                count += 1
            else:
                if count == 1:
                    compressed += prev
                else:
                    compressed += str(count) + prev
                prev = s[j:j+step]
                count = 1
        if count == 1:
            compressed += prev
        else:
            compressed += str(count) + prev
        answer = min(answer, len(compressed))
    return answer


if __name__ == "__main__":
    s = "abcabcabcabcdededededede"
    solution(s)