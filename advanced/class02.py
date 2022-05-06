# 클래스 상속 
class Vehicle:
    name ='탈것'
    color = '색상'

    def __init__(self, color = None) -> None: # 초기화,  부모클래스에 작성시 자식클래스에서도 실행 
        self.color = color
        print(f'{self.color}색 {self.name} 생성!')


    def desc(self):
            print(f'{self.name} 객체')

    def move(self):
            print(f'{self.name} 이동!')

class Car(Vehicle) : # Vehicle 클래스를 상속받는 Car클래스 만든다
    name='자동차' # name은 vehicle에서 받은것 
    brand ='현대'
    def __init__(self, color=None) -> None:
        super().__init__(color) # super >> 부모거 초기화 
        print(f'{color}색 {self.brand}  {self.name} 생성!!!')
   
    def move(self):
       # print(f'{self.name} 달린다!') # vehicle 클래스에 있는 함수 사용, 자식 name이 들어가서 함수 실행 
        super().move() # 부모클래스인 vehicle 클래스에 있는 move 함수를 사용
        print(f'{self.name} 달린다!')

    def stop(self):
        print('브레이크로 멈춤') 
    
if __name__ =='__main__':
    vcl = Vehicle('검은')
    vcl.desc()
    vcl.move()

    mycar = Car('흰') # 변수가 하나 있어서 흰 넣으면 나오느건가 
    mycar.desc()
    mycar.move()
    mycar.stop()