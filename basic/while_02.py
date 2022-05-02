# 무한루프
num = 0
while True:
    print('''처리번호를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료
입력번호 : ''')
    num = int(input()) # 키보드로 입력받은 수를 num에 할당

    if num ==1 :
        print('회원정보 입력')
    elif num == 2 :# else if num==2이면  1은 아니고 2이면 
        print('회원검색')
    elif num == 3 : 
        print('회원수정')
    elif num == 4 : 
        print('회원삭제')
    elif num == 5 : 
        print('프로그램 종료')
        break
    else:
        print('잘못 입력했습니다.')
        continue # 들여쓰기 매우매우 중요중요 

