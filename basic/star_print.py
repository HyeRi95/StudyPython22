# *찍기
for x in range (1,6):
    for y in range(1,6): #범위를 바꿔서 다른 형태의 star 출력 #(6-x,6) 
        print('*', end='') #줄이 바뀌지 않고 그 다음 값이 바로 뒤에 출력된다 
    print('')

print('Hello', end=' ') 
print('World')

for x in range (1,6):
    for y in range(x,6): 
        print('*', end='')  
    print('')

print('Hello', end=' ') 
print('World')

for x in range (1,6):
    for y in range(6-x,6): 
        print('*', end='')
    print('')

print('Hello', end=' ') 
print('World')

#python star printing 공부하기