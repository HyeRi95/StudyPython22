# 객체지향 
class Car:
    number = '54라 9538'
    company = '현대자동차'
    gear_mode = 'Automatic'
    fuel = '휘발유'

    def setPower(self):
        
        print('시동을 겁니다.')

    def setPark(self):
        self.setGear('p') # 클래스의 내부함수를 불러서 다시 쓸수있다 
        print('주차합니다.')

    # r(후진), n(중립), p(파킹), d(중립), s(스포츠모드)
    def setGear(self,gear:str):
        print(f'{gear}모드로 전환합니다.')
    
    def accerator(self):
        print('엑셀을 밟습니다.')

    def pushbreak(self):
        print('브레이크를 밟습니다.')
    
if __name__ == '__main__':
    mycar = Car()
    print(f'제조사는 {mycar.company} 입니다.')
    mycar.setPower()
    mycar.setGear('d')
    mycar.accerator()
    mycar.pushbreak()
    mycar.setPark()