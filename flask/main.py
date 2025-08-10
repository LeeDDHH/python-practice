from flask import Flask

app = Flask('JobScrapper')


@app.route('/')
def home():
    return "Welcome to the Job Scrapper!"


app.run("0.0.0.0", port=80, debug=True)

# from extractor.wanted import extract_wanted_jobs
# from modules.wanted_scraper import csv_first_row
# from files import save_to_file

# keyword = input('What do you want to search for?')

# wanted = extract_wanted_jobs(keyword)

# save_to_file(keyword, csv_first_row, wanted)
