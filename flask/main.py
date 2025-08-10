from extractor.wanted import extract_wanted_jobs
from files import save_to_file

keyword = input('What do you want to search for?')

wanted = extract_wanted_jobs(keyword)

print(wanted)

save_to_file(keyword, wanted)
