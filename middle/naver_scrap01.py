#네이버 웹페이지 긁어오기
from urllib.request import Request, urlopen # Request class 이므로 객체생성 필요

req = Request('https://www.naver.com/') # 객체 생성
res = urlopen(req)
