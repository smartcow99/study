# 입력받기
input1 = input()

num_list = []
operator_list = []
tmp = 0

# 숫자와 연산자 분리하기
for i in range(len(input1)):
  if input1[i] == '+' :
    num_list.append(int(input1[tmp:i]))
    operator_list.append(input1[i])
    tmp = i+1
  elif input1[i] == '-' :
    num_list.append(int(input1[tmp:i]))
    operator_list.append(input1[i])
    tmp = i+1
num_list.append(int(input1[tmp:]))

sum = num_list[0]
result_list = []
result_operator_list = []

# 
for i in range(len(operator_list)) :
  if(operator_list[i] == "+") :
    sum += num_list[i+1]
  else :
    result_list.append(int(sum))
    sum = num_list[i+1]
    result_operator_list.append(operator_list[i])
result_list.append(int(sum))

result = result_list[0]
if len(result_operator_list) == 0 :
  print(result_list[0])
else :
  for i in range(len(result_operator_list)) :
    
    if(result_operator_list[i] == "-") :
      result -= int(result_list[i+1])
    else :
      result += int(result_list[i+1])
  print(result)
