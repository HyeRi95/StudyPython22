# 두개의 값을 입력받아 두개의 변수에 나눠담기
# x, y = input('두 수를 입력하세요(구분자는 /) > ').split('/') # 스페이스로 두 단어를 나누겠다, .split(구분자)

# print(int(x)*int(y)) #숫자가 두개 이상이면 입력시 int 함수 못써서 위에서 int 사용할 수 없다 int(input(~~)) : 불가


# x, y = map(float, input('두 수를 입력하세요(구분자는 /) > ').split('/')) 
# # map(형변환함수) : 내가 받은 모든값을 다른형으로 변환하는 함수 
# # 기본은 string (문자)
# print(x+y)

greeting ="Hello, I'm a student.\"bye\" " # \" , \' 사용, \ 사용시 \\두번 
print(greeting)
