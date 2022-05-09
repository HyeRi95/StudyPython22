# 주소록 프로그램 v1.5
# 작성일 : 2022 - 05 - 09
# 작성자 : HyeRi Cho
# 설명 : 갑자기 쌀쌀해진 월요일 ㅠ_ㅜ 파일DB에서 Oracle로 변경 
import os
import cx_Oracle as ora 

# 연락처 클래스
class Contact :
    name = '';  phone_num = '';  e_mail = '';  addr = '' # left value로 보통 사용 

    def __init__(self, name, phone_num , e_mail, addr) -> None: # __init__ 사용하면 left value값 self.name 사용 , None 이라 return X
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str: # retrun 해줘야한다 
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'========================================'
                   )

        return str_val

def initDB(): # 데이터베이스 초기화
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user = 'scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn


def run():

    conn = initDB() # 오라클 연결해서 연결객체 생성 
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            isval = set_contact(conn)
            if isval :
                input('연락처 추가 성공/n계속하려면 엔터를 누르세요.') # 아무값도 받지않고 엔터대기 (엔터치면 다음으로 넘어감)
            else :
                input('오류발생! 관리자에게 문의하세요.')
            clearConsole()
        elif sel_menu ==2: #연락처 출력
            clearConsole()
            get_contact(conn)
            input('계속하려면 엔터를 누르세요.') #엔터대기 
            clearConsole()
        elif sel_menu ==3:
            clearConsole()
            name= input('삭제할 이름 입력 > ')
            del_contact(conn, name)
            input('연락처 삭제성공\n계속하려면 엔터를 누르세요.')
            clearConsole()
           
        elif sel_menu ==4: # 종료 
            conn.close()
        
            break
        else:
            clearConsole()
           
# 주소록 입력함수
def set_contact(conn):  # -> None : return 값 없음 (생략가능) , \ 역슬래쉬 : 너무길어 한줄에 못 적을때 
    contact = None # contact 초기화
    isSucceed = False # 입력성공여부
    try : # 아무입력없이 엔터 또는 입력정보 갯수가 틀렸을때의 예외처리 
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /)) > ').split('/')
        contact = Contact(name, phone_num, e_mail, addr )
        #DB 처리 
        cur = conn.cursor()
        query = ('INSERT INTO addressbook ' # 공백없으면 예외발생 데이터 저장 안됨 쿼리적을때 , 안된다
                 'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
                 #INSERT INTO addressbook(name, phone_num,e_mail, addr)  순서가 다르면 이렇게 꼭 적어줘야 
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close() 
        isSucceed = True
    except Exception as e:
        print('입력갯수 확인 (이름/핸드폰/이메일/주소)')
        isSucceed = False
    finally:
          return isSucceed #True면 DB 입력성공, False면 DB 입력실패 

# 주소록 전체 출력
def get_contact(conn):
    cur = conn.cursor()
    query = 'SELECT name, phone_num, e_mail, addr FROM addressbook'
    for row in cur.execute(query) :
        contact = Contact(row[0], row[1], row[2], row[3])
        print(contact)
    cur.close()

# 주소록 삭제
def del_contact(conn, name):
    cur = conn.cursor()
    query =f"DELETE FROM addressbook WHERE name = '{name}'" # f << 사용법 잘 알아두자 
    cur.execute(query)
    conn.commit()
    cur.close()

#메뉴 출력 및 선택
def get_menu():
    str_menu = ('--주소록 프로그램 v1.1--\n'
             '1. 연락처 추가\n'
             '2. 연락처 출력\n'
             '3. 연락처 삭제\n'
             '4. 종료\n')

    print(str_menu)
    # 0~9 숫자 외에는 value 에러 발생 > 예외처리
    menu = 0 #초기화 예외처리시 menu값 없어지므로 
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e :
        print(e)
    finally:
        return menu

def clearConsole():
    command = 'clear' # mac unix, linux 화면클리어 명령어
    if os.name in('nt', 'dos'):
        command ='cls' #window, dos 화면 clear 명령어 
    os.system(command) # 콘솔에서 명령을 실행한다

if __name__ == '__main__' :
    try:
        run() # 더블클릭하고 f12 단축키 같은 단어 찾기 
    except KeyboardInterrupt as e:
        print('Ctrl+c 종료') # ctrl+c 키로 종료시 깔끔하게 문구 출력하고 종료 
    
    