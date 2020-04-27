import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)

    # print(indeed_result.text)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)

    pages = pagination.find_all('a')
    # print(pages)
    spans = []
    for page in pages[:-1]:
        # print(page.string)
        spans.append(int(page.string))
        # print(page.find("span"))
        # spans.append(page.find("span").string)
    # print(spans)
    # print(spans[0:-1])
    # print(spans)
    max_page = spans[-1]
    # spans = spans[:-1]

    # for n in range(max_page):
    #   print(f"star={n*50}")
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    # print(str(title))
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company.find("a").string)
    else:
        company = str(company.string)
    company = company.strip()

    location = html.find("span", {"class": "location"})
    # if location is not None:
    #  print(location)
    # else:
    #  print("None")
    # print(location)
    # print(title,':',company,':',location)
    return {'title': title, 'company': company, 'location': location}


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    # print(results)
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    # return jobs
    return jobs