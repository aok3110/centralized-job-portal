import requests
from bs4 import BeautifulSoup

def scrape_timesjobs(query="developer"):
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&txtKeywords={query}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.find_all('li', class_='clearfix job-bx'):
        title = job.find('h2').text.strip()
        company = job.find('h3').text.strip()
        location = job.find('span', class_='srp-place').text.strip()

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "source": "TimesJobs"
        })

    return jobs
