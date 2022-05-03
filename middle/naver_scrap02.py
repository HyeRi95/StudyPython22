# naver (구글) 웹페이지 긁어오기 2
import requests as req

res = req.get('https://www.naver.com')
#print(res.status_code)
print(res.content) # 터미널 창에 cls << 정리 