import csv
try:
    with open('H2019 open ends.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['variable'], row['prompt'], row['label'])
except(UnicodeDecodeError):
    #print("UNICODE ERROR, USING LATIN 1")
    with open('H2019 open ends.csv', newline='', encoding="ISO-8859-1") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['variable'], row['prompt'], row['label'])
    #print("UNICODE ERROR NEVERTHELESS")