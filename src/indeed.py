import requests
from bs4 import BeautifulSoup

LIMIT =50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():

  result = requests.get(URL)

  #print(indeed_result.text)

  soup = BeautifulSoup(result.text,"html.parser")

  pagination = soup.find("div",{"class":"pagination"})
  #print(pagination)

  pages = pagination.find_all('a')
  #print(pages)
  spans = []
  for page in pages[:-1]:
    #print(page.string)
    spans.append(int(page.string))
    #print(page.find("span"))
    #spans.append(page.find("span").string)
  #print(spans)
  #print(spans[0:-1])
  #print(spans)
  max_page = spans[-1]
  #spans = spans[:-1]

  for n in range(max_page):
    print(f"star={n*50}")
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)
  return jobs