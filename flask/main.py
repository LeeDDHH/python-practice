from extractor.wanted import extract_wanted_jobs
from modules.wanted_scraper import csv_first_row
from files import save_to_file

keyword = input('What do you want to search for?')

wanted = extract_wanted_jobs(keyword)

save_to_file(keyword, csv_first_row, wanted)
