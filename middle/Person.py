#사람객체를 위한 클래스 Person, 객체를 만드는 틀 = class 
# 객체는 대부분 속성, 행위 둘다 가지고 있어야, 속성은(명사) 변수, 행위(동사)는 함수 
class Person:
    __name = '' #이름속성    __name로 변경하면 조혜리 출력 X  // __name 변수명은 객체가 만들어진 이후에 속성을 바꾸고싶지않을때 
    age =  0
    height = 100
    weight = 30 #몸무게 속성

    # 생성자 재정의, 객체를 생성시 p.name 으로 이름 변경 못하게 한다 (보안) 
    def __init__(self, name = None) -> None:  # 생성자 리턴값이 없다
        if name == None:
            self.__name = '홍길동' # 매개변수 없이 객체 생성할때 홍길동이 디폴트값으로 출력
        else :
            self.__name = name
        
        print(f'{self.__name} 탄생!!')
    
    #매직메서드 __str__ 사용 재정의
    def __str__(self) -> str: # 리턴값이 string (문자)
        value = f'''객체 : {self.__name}
나이 : {self.age}
키 : {self.height}'''
        return value

    def walk(self, speed): # 클래스 내에서 함수를 사용하려면 항상 self가 필수여야 
        print(f'{self.__name}이(가) {speed}km/h로 걷는다.')
        return
    
    def run(self, speed):
          print(f'{self.__name}이(가) {speed}km/h로 뛴다.')


p = Person('조혜리') # 생성자 재정의 했기 때문에 매개변수 없이는 사용하지 못한다 
# p = Person() # >> class는 객체틀 변수 p에 class 넣어서 객체생성
# p.__name ='조혜리' #p.name = '조혜리'
p.age = 20
p.height = 170
p.weight = 50
p.walk(2)
p.run(10)

print(p)

