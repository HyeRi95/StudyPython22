# 문자열 연산
first = 'Hello'
second = 'World!'

print(first + second) # 문자연산 + 문자열 합차기

print(first, second) # CONCAT와 동일 자동으로 띄어쓰기
# 문자열 연산에는 + 와 *만 존재 

print(first * 3) # n번 출력

# 문자열의 길이 내장함수
print(len('한글'))
print(len(first))

# 리스트 연산
print(first[0]) # first에 부여된 문자열에서 0번째 index에 있는 문자 출력
print(first[-1])# index 거꾸로도 가능
print(first[-2])  
print(first[-3])  
print(first[-4])  
print(first[-5]) 
#print(first[-6]) index 범위 벗어난 값 error

# 현재 일시
current_date = '2022-05-02 14:23:45'
year = current_date[0:4] # 시작 index는 그대로 넣어주고  n번째 index 까지 출력 하고싶을때 n+1을 넣어줘야한다  
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
sec = current_date[17:19]
print(year,'년', month, '월', day, '일')
print(hour, '시', min, '분', sec, '초')

print(current_date[-2:],'초') # 거꾸로 할때는 0을 넣지않고 실행 
print(current_date[-5:-3],'분') 
# 문자열은 리스트로 하더라도 값 변경 안되고 튜플과 동일


l = [1,2,3,4,5]
l[0] = 10
print(l)

p = 'python'
print(p)
#p[0] = 'P' #Python 대문자 P 변경 안됨
print('P' + p[1:]) # [1:] : index 1 부터 끝까지 
p2 = 'P' + p[1:]
print(p2)

print(p.upper()) # p라는 class를 대문자로 변경 (p가 부여받은 문자 모두 대문자)
print(p2.lower()) # 소문자로 변경



