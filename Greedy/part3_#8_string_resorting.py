#sort(reverse=True)
#upper(), capitalize(), title()
#String.join()으로 리스트의 모든 요소들을 하나의 문자열로 변환
#result = ' '.join(s for s in str_list)
# list_a = map(int, list_a) 
#runtime within 1s
#float 처리하려면 어케 하지? 

#tmp_list.append(ele.upper())  #['A', 'D', 'S', '6']
#tmp_list.append(ele.upper)  #[<built-in method upper of str object at 0x7f26660dc458>, <built-in method upper of str object at 0x7f26660edc70>, <built-in method upper of str object at 0x7f266614de30>, '6']

def StringResorting(input_string):
  cnt=0
  #for_flaot = float(0.0)
  tmp_list = []
  input_string.sort()
  for ele in input_string:  
    if ele is '1':
      cnt += int(ele)
    elif ele is '2':
      cnt += int(ele)
    elif ele is '3':
      cnt += int(ele)
    elif ele is '4':
      cnt += int(ele)
    elif ele is '5':
      cnt += int(ele)
    elif ele is '6':
      cnt += int(ele)
    elif ele is '7':
      cnt += int(ele)
    elif ele is '8':
      cnt += int(ele)
    elif ele is '9':
      cnt += int(ele)
    elif ele is '0':
      cnt += int(ele)
    else:
      tmp_list.append(ele.upper())  
  tmp_list.append(str(cnt))
  sorted_stings = ''.join(s for s in tmp_list)
  return sorted_stings

def main(sorted_stings):
  print(sorted_stings)
  return 0

if __name__=="__main__":
  input_string = list(input('input stings as capital characters: '))
  sorted_stings = StringResorting(input_string)
  main(sorted_stings)