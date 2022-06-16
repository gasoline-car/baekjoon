# 문제
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

# number = int(input())

# for i in range (1,10) :
#     print(number, '*', i, '=', number*i)


sentence = input()
sentence = sentence.split()

num = len(sentence)

list3 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
list2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
list1 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
list0 = ['']

i = 0
while i < num :
  if sentence[i] in list3:
    sentence[i] = 3
  elif sentence[i] in list2:
    sentence[i] = 2
  elif sentence[i] in list1:
    sentence[i] = 1
  else :
    sentence[i] = 0

j = 0
while j < num :
  sentence[j] = int(sentence[j])
  j = j + 1    

tire = 0
k = 0
while k < num-1 :
  if sentence[i] <= sentence[i+1]:
    tire = tire + (sentence[i+1]-sentence[i])
  else :
    tire = tire + (sentence[i]-sentence[i+1])

print(tire)

