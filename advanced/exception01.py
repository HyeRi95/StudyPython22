# 예외처리 1 - 예외발생
def multi(a,b):
    res = a*b
    return res

def divide (a,b):
    res = 0

    try:
        res = a/b
    except Exception as e:
        print(f'예외발생 {e}') # 모든 예외 처리 가능 
    finally :
        return res # finally 항상 res값 반환

if __name__ =='__main__': # 프로그램 시작점
    print('곱셈/나눗셈')
# try:                    # 예외처리 
#     print(divide(6,0))
   
# except ZeroDivisionError as e:
#     # print(e)
#     print('b에다가 0 쫌 넣지마세요!!! 이 바보야!@!~!!!')

    print(multi(6,6))
    print('종료')

# 예외가 발생한줄
# 예외 발생코드 
# 예외가 발생한 원인

#중단점 설정 해제 f9
#프로시저 단위실행 f10
#스텝인투 한단계씩 코드 실행 f11
#디버그 시작 f5
#shift +f5 디버깅 종료