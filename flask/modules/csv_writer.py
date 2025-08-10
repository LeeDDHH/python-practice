import csv


class CSVWriter:
    def __init__(self, filename, headers):
        self.filePath = f"./src/files/{filename}_jobs.csv"
        self.headers = headers

    def write(self, datas):
        file = open(self.filePath, mode='w', newline='')

        writer = csv.writer(file)
        writer.writerow(self.headers)
        for data in datas:
            writer.writerow(data.values())

        file.close()
