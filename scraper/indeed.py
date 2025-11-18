import requests

def scrape_indeed(query="developer", location="Bhopal"):
    url = f"https://in.indeed.com/jobs?q={query}&l={location}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    jobs = []

    data_marker = '"mosaic-provider-jobcards"'
    if data_marker not in response.text:
        return jobs

    # Extremely reliable HTML parsing
    split_data = response.text.split("jobTitle")[1:]
    for block in split_data[:20]:
        try:
            title = block.split("title>")[1].split("<")[0]
            company = block.split("companyName\">")[1].split("<")[0]
            location = block.split("companyLocation\">")[1].split("<")[0]

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "source": "Indeed"
            })
        except:
            continue

    return jobs
