import csv
from errors import ErrorItemNotFound


def parse_csv(filename):
    """Чтение из файла и формирование словаря"""
    result = dict()
    with open(filename, 'r', encoding="utf-8", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            sku, rec, probability = row
            result.setdefault(sku, []).append((rec, probability))
    return result


class RecFinder:
    """Класс-обработчик"""
    def __init__(self, filename):
        self._data = parse_csv(filename)

    def find_recommendations(self, sku, prob_threshold=None):
        """Основной метод для обработки файла, возвращает нужный лист """
        recommendations = self._data.get(sku)
        if recommendations:
            if prob_threshold:
                result_list = [tup[0] for tup in recommendations if float(tup[1])>=prob_threshold]
            else:
                result_list = [tup[0] for tup in recommendations]
        else:
            raise ErrorItemNotFound("Не обнаружено целевого товара")
        return result_list

if __name__ == "__main__":
    finder = RecFinder("rec.csv")
    res = finder.find_recommendations('QgybZB43EN', 0.8)
    print(res)