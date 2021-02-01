import csv

data = ["hello", "world"]
with open("csvfile.csv", "wb") as csv_file:
    for line in data:
        csv_file.write(line.encode())
        csv_file.write("\n".encode())
