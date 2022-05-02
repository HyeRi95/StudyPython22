# for문 학습
#arr =[1,2,3,4,5,6,7,8,9,10]
# 한줄 주석 
'''다중문자열 == 여러줄 주석
'''
'''
result = 0

# for x in arr : # arr 합 구하기
    #result = result + x

for x in range(1,101): # n 까지 합 구하고싶을때 n+1을 뒤의 범위에 적어준다
    result = result + x

print('배열의 합 =', result)

arr2 = ('me','my','friend', 'jane') # 튜플 리스트 상관 없다 

for item in arr2:
    print(f'{item:>10}') # 10자리로 맞춰서 출력 
    #print(f'{item}') 출력 
    #print(f'{item * 2}') index별 2개씩 출력 


# 1~10까지 수에서 짝수 구분하기 

for num in range (1,11,2) : # (시작숫자, 최댓값+1, 증가량) : (1,11,2) 1부터 10까지 2씩 증가 
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다')
    else :
        print(f'{num}는 홀수입니다.')
'''

# for문 내에서 사용하는 continue, break
values = [1,3,5,7,9,11,13,15,17,19]
num = 0
for item in values :
    num += 1 # num = num+1
    if (num % 2) == 0:
        #break # 반복문 탈출
        continue # if 조건만 패스하고 다음값으로 진행한다 
    else :
        print(f'{num}번 수는 {item}입니다.')







