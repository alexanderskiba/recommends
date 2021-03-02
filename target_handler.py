class Handler:
    """Класс-обработчик"""
    def __init__(self, sku, probability=None):
        self.sku = sku # Товар
        self.probability = probability # Вероятность совпадения
        self.result_list = list() # Лист с рекомендациями

    def process(self, data): #принимаем на вход словарь и обработаем его значения
        """основной метод для обработки файла, возвращает нужный лист """
        if self.probability is None: # если нет доп. параметра, то просто вернем значений для указанного товара
            for tup in data[self.sku]:
                self.result_list.append(tup[0])
            return self.result_list
        else: # если задана требуемая вероятность, бежим по списку, смотрим на значение вероятность, если совпало, добавляем лист
            for tup in data[self.sku]:
                if self.probability == float(tup[1]):
                    self.result_list.append(tup[0])
            return self.result_list