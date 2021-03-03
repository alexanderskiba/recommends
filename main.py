from csv_reader import Reader
from target_handler import Handler
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

if __name__ == "__main__":
    reader = Reader("rec.csv")
    data = reader.read_csv()
    # создадим объект обработчика
    text_handler = Handler("QgybZB43EN", 0.5) # 0.8 0.9
    # запустим метод для целевой обработки(возврата списка рекомендаций для указанного товара)
    target_list = text_handler.process(data)
    print(target_list)
    # for key, value in data.items():
    #     print(key, value)