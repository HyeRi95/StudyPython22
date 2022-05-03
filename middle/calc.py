#계산기 프로그램 함수 선언은 위에서 
'''
함수선언 구조
def 함수명(매개변수):
    처리로직1
    처리로직2
'''

def plus(a, b):
    res = a + b
    return res # 엔터 두번 함수 정의 끝 

def minus(a, b):
    res = a - b # return 뒤에 변수 사용 안할시에 res 연한색으로 표시 : 변수 지정하고 사용하지 않았다고 알려주는것
    return res

def multiple(a, b):
    res = a * b
    return res # return은 나를 호출한 곳에 값을 전해주고 함수는 종료 , 함수 실행후 res 값을 반환 하고 함수 종료

def divide(a, b):
    if b == 0:
        return 0

    res = a / b # res : 지역변수 함수내에서만 사용되는 변수 각각의 함수의 res는 다르다 
    return res



# 연습
def adds(*args) : # parameter , arguments // *agrs : 매개변수 갯수가 일정치 않은 경우 사용 
    res = 0
    for i in args:
        res += i

    return res

print(adds(1,2,3,4,5,6,7,8,9,10))
print(adds(1,2,3))
print(adds(5,7,9,11,455))


def mul_and_div(a, b): # 함수결과가 하나 이상인 경우 
    return (a*b, a/b) # 튜플 리턴 

def add_and_minus_and_multi_and_div(a,b):
    return(a+b, a-b, a*b, a/b)

(mul_val, div_val) = mul_and_div(16,2)
print (mul_val)
print (div_val)
print(mul_and_div(16,2)) # 결과값은 튜플로 출력된다

print(add_and_minus_and_multi_and_div(17,5))
#연습끝


# num = 0
# x = 0
# y = 0
# val = 0
# while True:
#     print('''---메뉴---
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셈
# 4. 나눗셈
# 5. 종료
# 숫자입력 : ''', end=' ')
#     num =int(input())
   
#     if num ==1 :
#         print('첫번째 값을 입력하세요 : ', end=' ')
#         x = int(input())
#         print('두번째 값을 입력하세요 : ', end=' ' )
#         y = int(input())
#         val = plus(x,y) # 함수호출, val에는 plus 함수의 return 값 res를 할당  
#         print('결과값 : ', f'{x} + {y} = {val}')
#     elif num==2:
#         print('첫번째 값을 입력하세요 : ', end=' ')
#         x = int(input())
#         print('두번째 값을 입력하세요 : ', end=' ' )
#         y = int(input())
#         val = minus(x,y) # 함수호출, val에는 plus 함수의 return 값 res를 할당  
#         print('결과값 : ', f'{x} - {y} = {val}')
#     elif num==3:
#         print('첫번째 값을 입력하세요 : ', end=' ')
#         x = int(input())
#         print('두번째 값을 입력하세요 : ', end=' ' )
#         y = int(input())
#         val = multiple(x,y) # 함수호출, val에는 plus 함수의 return 값 res를 할당  
#         print('결과값 : ', f'{x} x {y} = {val}')
        
#     elif num==4:
#         print('첫번째 값을 입력하세요 : ', end=' ')
#         x = int(input())
#         print('두번째 값을 입력하세요 : ', end=' ' )
#         y = int(input())
#         val = divide(x,y) # 함수호출, val에는 plus 함수의 return 값 res를 할당  
#         print('결과값 : ', f'{x} ÷ {y} = {val}')
#     elif num ==5:
#         break
#     else:
#         continue
    




