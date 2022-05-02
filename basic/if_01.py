# if문

name = '홍길동'
gender = '여'

print('---첫번째 결과---')
if name == '홍길동' : # : 적어준다 들여쓰기 중요 
    if gender =='남':
        print('진료실로 들어갑니다.')
        print('의사쌤한테 인사합니다.')
    else :
        print('성별이 다르네요~')
else : # : 적어준다
    print('부를때까지 기다리세요.')
    print('궁시렁거립니다.')

print('\n')
print('---두번째 결과---')
if name == '홍길동' and gender == '남' : 
    print('진료실로 들어갑니다.')
    print('의사쌤한테 인사합니다.')
    
else : # : 적어준다
    print('부를때까지 기다리세요.')
    print('궁시렁거립니다.')

num = 10

if num != 9:
    print('9가 아닙니다')
else :
    print('9입니다')


