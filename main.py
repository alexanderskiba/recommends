import csv
import bisect


class Handler:
    """Класс-обработчик"""
    def __init__(self, sku, probability=None):
        self.sku = sku
        self.probability = probability

    def process(self):
        """основной метод для обработки файла """

