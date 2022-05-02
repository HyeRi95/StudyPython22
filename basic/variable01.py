# 주석입니다. 주석은 프로그래밍에 영향을 끼치지 않습니다.

# 변수
# 변수명은 숫자로 시작X 스페이스X  대소문자 구분  특수문자는_ 가능
# left value 값을 받는쪽, right value 값을 주는쪽 
a = '안녕하세요' # "안녕하세요" ''""둘다 문자열 표현 가능하지만 홑따옴표 출력 할때는 쌍따옴표 사용 "I'm a boy."
print (a)

a = True
print(a)

a = 3.14
print(a)

a = 1/10
print(a)

print('값은', a, '입니다') #출력 방식 2 ,로 구분하며 갯수는 상관없다
a = 3
b = 3.141592
c ='python'
d = (1,2,3)
e = [4,5,6]
f = [7, '8', True] # true false는 문자열 아니다  
g = False
print ('변수의값', 'a=', a , 'b=', b, 'c=', c, 'd=', d)
print ('변수의값', 'e=', e , 'f=', f, 'g=', g) # 튜플: 수정 X () 리스트 : []

Var5 = 5
var5 = '8'
print (Var5, var5)

print(id(a))
print(id(b))
print(id(c))