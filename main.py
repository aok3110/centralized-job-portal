from scraper.scrape_indeed import fetch_jobs


if __name__ == "__main__":
    print("Fetching jobs...")
    jobs = fetch_jobs()
    save_jobs(jobs)
    print("Done.")
