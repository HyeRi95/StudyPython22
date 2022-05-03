# 구구단 프로그램 
# 2x1=2 ... 2x9=18  x x y = xy
# 3x1=3 ... 3x9=27
# 9x1=9 ... 9x9=81

print('---구구단 프로그램---')
for x in range(2,10) : 
    print(f'{x}단 시작')
    for y in range(1,10):
        print(f'{x}x{y}={x*y:2d}',end=' ') # 자릿수 맞추기 2d: 두자릿수 정수로 출력 d 정수 f 실수 s 문자열 
    print('')    # print('\n')하나의 단이 끝나면 enter

