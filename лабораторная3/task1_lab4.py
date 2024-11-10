# TODO импортировать необходимые молули

import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    read = open(INPUT_FILENAME, "r")
    write = open(OUTPUT_FILENAME, "w")

    file_reader = csv.DictReader(read)
    a = []
    for i in file_reader:
        a.append(i)

    json.dump(a, write, indent = 4)
    write.close()
    read.close()

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



