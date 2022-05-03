#첫번째 간단한 로또
import random as rnd

numbers = [i for i in range(1,46)] #순차적으로 만들때 사용 

lotto = [] #로또번호 저장

for i in range(6): #0~5까지 for문 6번 실행
    lotto.append(rnd.choice(numbers)) # append 하나씩 추가
lotto.sort() # sort 정렬
print(lotto) 


