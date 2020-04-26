import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=sw%EC%9E%90%EB%8F%99%EC%B0%A8+%EC%A0%95%EA%B7%9C%EC%A7%81&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&radius=25&l=&fromage=any&limit=10&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")