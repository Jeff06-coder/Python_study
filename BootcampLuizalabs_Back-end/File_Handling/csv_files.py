import csv
from pathlib import Path

PATH = Path(__file__).parent

try:
    with open(PATH / "dat1a.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except IOError as exc:
    print(f"Error reading file: {exc}")

#try:
    #with open(PATH / "data.csv", "a", newline="", encoding="utf-8") as file:
        #writer = csv.writer(file)
        #writer.writerow(["John Doe", "john.doe@example.com"])
        #writer.writerow(["Jane Smith", "jane.smith@example.com"])
#except IOError as exc:
    #print(f"Error writing to file: {exc}")

try:
    with open(PATH / "data.csv", "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        print(reader.fieldnames)  # Imprime os nomes das colunas
        for row in reader:
            print(row)
except IOError as exc:
    print(f"Error reading file: {exc}")

