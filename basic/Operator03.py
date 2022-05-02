# 문자열 포맷팅
name = '조혜리'
login_str = '{0}님 로그인중'.format(name) 

print(login_str)

# 문자열 포맷팅 방법
print('{0}, {1}, {2}'.format('하나', 2, True))

print(f"{'하나'}, {2}, {login_str}")

# 소수점 표현 
PI = 3.14159268
print('{0:0.2f}'.format(PI)) # 소수점 두자리까지 표현 
print(f'{PI:0.3f}')

full_name = 'Hugo MG sung'
sp_names = full_name.split() # 하나의 문자열을 ' '으로 잘라서 리스트로 만든다
print(sp_names)
print(sp_names[0])

greeting = 'Hello, World'
words = greeting.split(',') # 문자열을 ,로 잘라서 리스트로 만든다 공백은 따로 처리못한다 
print(words)

hi = '      Hello~   '
print(hi.lstrip()) # oracle LTRIM()
print(hi.rstrip()) # oracle RTRIM()
print(hi.strip())  # oracle TRIM()
print(words[1].strip()) # words 리스트의 [1]에 공백을 없애준다

#문자열 특정 단어, 문자열 값 변경
print(full_name.replace('Hugo MG', 'Ashley')) #Hugo MG 를 Ashley로 변경

# 리스트 연산
arr = ['1',2,3,'4',5]

print(arr[4]+arr[2]) # 리스트의 3번째 index 값과 0번째 index 값 연산
print(arr[3] + arr[0]) # 문자열일때 문자열 두개 합치기도 가능 
print(arr[3]*3) # index 3번의 4라는 문자를 3번 출력 (문자)

# 이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']] # 2차원 배열
print(arr2[3])
print(arr2[3][1]) # arr2의 index 3에 있는 리스트 내에서 index 1번에 있는 My 출력
print(arr2[3][1][0]) # arr2의 index 3에 있는 리스트 내에서 index 1번에 있는 My 내의 index 0번인 M 출력

arr3 = arr +arr2
print(arr3)


