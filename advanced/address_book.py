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
    clearConsole()

    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            lst_contact.append(contact)
            input() # 아무값도 받지않고 엔터대기 (엔터치면 다음으로 넘어감)
            clearConsole()
        elif sel_menu ==2: #연락처 출력
            clearConsole()
            get_contact(lst_contact)
            input() #엔터대기 
            clearConsole()
        elif sel_menu ==3:
            clearConsole()
            name= input('삭제할 이름 입력 > ')
            del_contact(lst_contact, name)
            input()
            clearConsole()
        elif sel_menu ==4:
            break

        else:
            clearConsole()
           

# 주소록 입력함수
def set_contact():  # -> None : return 값 없음 (생략가능) , \ 역슬래쉬 : 너무길어 한줄에 못 적을때 
    name, phone_num, e_mail, addr = \
        input('정보입렴(이름, 핸드폰, 이메일, 주소(구분자 /) > ').split('/')
    contact = Contact(name, phone_num, e_mail, addr )
    #print(contact)
    return contact
# 주소록 전체 출력
def get_contact(lst_contact):
    for contact in lst_contact :
        print(contact)

# 주소록 삭제
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

def get_menu():
    str_menu = ('--주소록 프로그램 v1.1--\n'
             '1. 연락처 추가\n'
             '2. 연락처 출력\n'
             '3. 연락처 삭제\n'
             '4. 종료\n')

    print(str_menu)
    menu = input('메뉴 입력 : ')
    return int(menu)

def clearConsole():
    command = 'clear' # mac unix, linux 화면클리어 명령어
    if os.name in('nt', 'dos'):
        command ='cls' #window, dos 화면 clear 명령어 
    os.system(command) # 콘솔에서 명령을 실행한다

if __name__ == '__main__' :
    
    run()