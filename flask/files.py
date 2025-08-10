def save_to_file(file_name, jobs):
    file = open(f"./src/files/{file_name}.csv", "w")
    file.write("title, url, company_name, reward\n")

    for job in jobs:
        file.write(f"{job['title']}, {job['url']}, {job['company_name']}, {job['reward']}\n")

    file.close()
