# 예외처리 2 - 예외발생 2

from msilib.schema import Error


x, y = map(int,input('두수를 입력하세요> ').split(' '))
print(f'x = {x}')
print(f'y = {y}')

try:
    z = x/y # z 지역변수 try 구문내에서만 사용 
    print(f'{x} / {y} = {z}')
# except TypeError as e:
#     print('형변환 하세요')
# except ZeroDivisionError as e:
#     print('두번째 수에 0은 넣지마세요')
except Exception as e :
    print(f'예외발생 {e}') # 나머지 예외 발생시 출력 except : print('예외발생')

print('나누기 종료')
