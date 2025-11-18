from flask import Flask, render_template, jsonify
from scraper.indeed import scrape_indeed
from scraper.naukri import scrape_naukri
from scraper.timesjobs import scrape_timesjobs
from scraper.glassdoor import scrape_glassdoor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/jobs")
def jobs():
    jobs = []
    jobs += scrape_indeed()
    jobs += scrape_naukri()
    jobs += scrape_timesjobs()
    jobs += scrape_glassdoor()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
