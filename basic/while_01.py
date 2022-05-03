# while문 학습 : for과 함께 반복적인 문장 수행에 사용
hit = 0

while (hit <100):
    hit += 1

    print(f'나무를 {hit}번 찍었습니다.')
    if hit ==10:
        print('나무가 넘어갑니다!!')
        break # break 없으면 10번 이상으로도 계속 반복 
    else:
        print('나무가 아직 안 넘어갔네요.')
print('나무찍기 완료!!')




