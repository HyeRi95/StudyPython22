# 주소록 프로그램 v1.1
# 작성일 : 2022 - 05 - 04
# 작성자 : HyeRi Cho
# 설명 : 첫번째 기초 마무리 프로젝트
import os
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

def run():
    lst_contact = [] #빈리스트 생성 
    load_contact(lst_contact) #프로그램 시작할때 파일 db에 있는 값을 읽어온다 
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            if contact is None: # contact가 비면 리스트추가 불가 > 다시 while문 처음으로 올라가서 실행 
                input('계속하려면 엔터를 누르세요.')
                clearConsole()# 항상 메뉴가 상단에 나오도록 
                continue 
            lst_contact.append(contact)
            input('연락처 추가 성공/n계속하려면 엔터를 누르세요.') # 아무값도 받지않고 엔터대기 (엔터치면 다음으로 넘어감)
            clearConsole()
        elif sel_menu ==2: #연락처 출력
            clearConsole()
            get_contact(lst_contact)
            input('계속하려면 엔터를 누르세요.') #엔터대기 
            clearConsole()
        elif sel_menu ==3:
            clearConsole()
            name= input('삭제할 이름 입력 > ')
            del_contact(lst_contact, name)
            input('연락처 삭제성공\n계속하려면 엔터를 누르세요.')
            clearConsole()
           
        elif sel_menu ==4: # 종료 
            save_contact(lst_contact) #종료 전에 파일 DB 저장 
            break
        else:
            clearConsole()
           
# 주소록 입력함수
def set_contact():  # -> None : return 값 없음 (생략가능) , \ 역슬래쉬 : 너무길어 한줄에 못 적을때 
    contact = None # contact 초기화
    try : # 아무입력없이 엔터 또는 입력정보 갯수가 틀렸을때의 예외처리 
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /)) > ').split('/')
        contact = Contact(name, phone_num, e_mail, addr )
    #print(contact)
    except Exception as e:
        print('입력갯수 확인 (이름/핸드폰/이메일/주소)')
    finally:
         return contact # 잘못되면 none 리턴, contact 객체 리턴 

# 주소록 전체 출력
def get_contact(lst_contact):
    for contact in lst_contact :
        print(contact)

# 주소록 삭제
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

# 주소록 파일 DB 저장
def save_contact(lst_contact:list):
    f = open('./advanced/db_contact.txt', mode ='w',encoding = 'utf-8') # db_contact.txt 사용하려면 콘솔에서 실행 ./advanced/db_contact.txt 터미널에서 실행 
    for contact in lst_contact:
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')
    f.close()
    
# 주소록 파일 DB 로드
def load_contact(lst_contact:list): # type 지정해주면 content assistance 무리없이 사용가능 
    f = open('./advanced/db_contact.txt', mode ='r',encoding = 'utf-8')
    while True:
        line = f.readline()
        if not line: break

        lines = line.rstrip('\n').split('/')  # \n제거 하고, 구분자는 /로 한후  값을 리스트로 보낸다 
        if len(lines) != 4: continue 
        # 220506 저장된 db에서 엔터가 입력되어 빈줄이 생기고 리스트에 값이 저장되지 않았을때 생기는 문제 해결
        # 리스트에 값이 저장 안된건 무시하고 그대로 진행  
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        lst_contact.append(contact)

    f.close() # open - close 잘 하자     

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
    
    