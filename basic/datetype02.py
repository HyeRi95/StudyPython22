#문자열
from concurrent.futures import BrokenExecutor
from pickle import TRUE


bruce_ecke = 'Life is short, \n\tYou need Python.' # \n (escapte 문자): enter 표현 줄바꿈  \t : tab 표현
print(bruce_ecke)


multi_line ='''Life is short.
You need Python.
And I need C#, too.
'''

print(multi_line)

print(type(bruce_ecke))

# 리스트(배열)
b = [1,2,3,4]

print(b)

b.append(5) # 리스트 내장함수 중에 append 함수 : 리스트 맨뒤에 추가 
print(b)
b.insert(3,10) # 원하는 인덱스에 추가, 프로그램 언어는 순서(index) 0부터 시작한다 / oracle은 1부터 시작 
print(b) 

b.sort() # 오름차순 정렬
print(b)

b.reverse() # 내림차순 정렬
print(b) 

b.remove(10) # 원소 제거
print(b)
print(b[2])
print(type(b)) # b의 타입 : 리스트

# 튜플
c = (1,2,3,4)
print(c)
# c.append(5) error 튜플에서는 값추가 불가  리스트만큼 내장함수 없다 
print(c[2])

# 딕셔너리 : key와 value의 쌍의 집합
spiderman = {
    'name' : '피터파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memberOfAvengers' : True
}
print(spiderman) # () 튜플 {} 딕셔너리 []리스트
print(spiderman['name'])
# print(spiderman.age) error  
# print(spiderman[2]) error 
#  

