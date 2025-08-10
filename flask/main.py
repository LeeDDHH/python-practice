from flask import Flask, render_template, request, redirect, send_file
from extractor.wanted import extract_wanted_jobs
from modules.wanted_scraper import csv_first_row
from files import save_to_file

app = Flask('JobScrapper', template_folder='flask/templates')

db = {}


@app.route('/')
def home():
    return render_template("home.html", name='dong')


@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword is None or not keyword:
        return redirect('/')

    if keyword in db:
        wanted = db[keyword]
    else:
        wanted = extract_wanted_jobs(keyword)
        db[keyword] = wanted

    return render_template("search.html", keyword=keyword, jobs=wanted)


@app.route('/export')
def export():
    keyword = request.args.get('keyword')
    if keyword is None or not keyword:
        return redirect('/')

    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, csv_first_row, db[keyword])
    return send_file(f"./src/files/{keyword}_jobs.csv", as_attachment=True, download_name=f"{keyword}_jobs.csv")


app.run("0.0.0.0", port=80, debug=True)

# from extractor.wanted import extract_wanted_jobs
# from modules.wanted_scraper import csv_first_row
# from files import save_to_file

# keyword = input('What do you want to search for?')

# wanted = extract_wanted_jobs(keyword)

# save_to_file(keyword, csv_first_row, wanted)
