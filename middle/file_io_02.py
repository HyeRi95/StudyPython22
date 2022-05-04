# 파일 입출력 2 - 파일 읽기

f = open(file='./temp.txt', mode = 'r', encoding = 'utf-8') # 상대경로, 현재 directory : studypython22 

# t = f.read()
while True:
    line = f.readline() #한줄씩 출력
    if not line : #라인이 없으면 = 글이 없으면 
        break
    print(line, end='') #입력된 값에 \n 존재하므로 한줄씩 띄어져서 읽는다 >> end='' 입력해줌으로써 해결 
# print(t)

f.close() ## 필쑤!!
print('파일 읽기 완료')