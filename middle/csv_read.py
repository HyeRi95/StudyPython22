# CSV 파일 읽기
import csv

file_name = 'busanbus_211231.csv'

f = open('./'+file_name, mode ='r', encoding ='utf-8')  # 한글 출력 위해서 utf-8 or cp949 두개중 하나 
# 데이터를 받아와서 utf-8 파일로 인코딩 변환후 utf-8로 사용하자 

reader = csv.reader(f, delimiter = ',') # csv 파일 열어서 구분자를 확인한다, 구분자가 , 일 경우 delimiter = ','

next(reader) # 제목줄이 있을때 필요없을 경우 사용 : 제목줄(head) 삭제 
for line in reader: # 한줄 지울때 shift+delete
    print(line)

f.close() ##  필 쑤 !! 