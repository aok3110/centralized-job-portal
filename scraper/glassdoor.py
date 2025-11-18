import requests
from bs4 import BeautifulSoup

def scrape_glassdoor():
    url = "https://www.glassdoor.com/rss/jobs.rss?locId=2837784"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")

    jobs = []
    for item in soup.find_all("item")[:20]:
        jobs.append({
            "title": item.title.text,
            "company": item.author.text,
            "location": "Bhopal",
            "source": "Glassdoor"
        })

    return jobs
