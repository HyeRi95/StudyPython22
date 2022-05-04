# 파일 입출력 1 - 쓰기

# mode = w 항상 파일 새로생성  mode = a 추가 쓰기 , 기존파일에 출력된것 놔두고 밑에 다시 새로 출력  mode = r 읽기
f = open('C:/STUDY/StudyPython22/temp.txt', mode='w', encoding='utf-8') 

# 절대경로 입력시 / 사용해서 구분 # mode = w (쓰기) , utf-8 한글

f.write('안녕하세요.\n') # \n 줄바꿈 
f.write('저는 조혜리 입니다.\n')
f.write('한국사람입니다.\n')

f.close() ## 필수!! 
print('파일 생성완료')


