# TODO импортировать необходимые модули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
      with open(INPUT_FILENAME, encoding="utf-8") as csv_file:
          reader = csv.DictReader(csv_file)
          data = list(reader)
      with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as json_file:
          json.dump(data, json_file, indent=4, ensure_ascii=False)
      # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
