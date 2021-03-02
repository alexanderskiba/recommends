import csv


class Reader:
    """Класс чтения из файла"""
    def __init__(self, filename):
        self.filename = filename
        self.data = dict()

    def read_csv(self):
        """Чтение из файла и формирование словаря"""
        with open('rec.csv', 'r', encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                sku, rec, probabilty = row
                key = self.data.get(sku)
                if key:
                    key.append((rec, probabilty))
                else:
                    self.data[sku] = [(rec, probabilty)]
        return self.data