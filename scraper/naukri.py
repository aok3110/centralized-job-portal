import requests

def scrape_naukri(query="developer", location="Bhopal"):
    url = f"https://www.naukri.com/{query}-jobs-in-{location}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    jobs = []

    for item in response.text.split('jobTuple')[1:20]:
        try:
            title = item.split('title="')[1].split('"')[0]
            company = item.split('title="')[2].split('"')[0]
            location = item.split('placeHolder="')[1].split('"')[0]

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "source": "Naukri"
            })
        except:
            continue

    return jobs
