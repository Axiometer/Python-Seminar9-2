import csv

# Записываем в файл CSV список словарей
def write_to_csv(phonebook, filename, write_mode = "w"):
    with open(filename, write_mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["fullname", "number", "comment"])
        writer.writeheader()
        for item in phonebook:
            writer.writerow(item)

# Читаем из файла CSV список словарей
def read_from_csv(filename):
    book = []
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['fullname', 'number', 'comment'])
        # пропускаем шапку
        next(reader)
        book.extend(reader)
    return book

def export_file(phonebook, filename):
    write_to_csv(phonebook, filename)
