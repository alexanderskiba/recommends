import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from validator import validator
from logic import RecFinder
from errors import ErrorItemNotFound

FILE = "recommends.csv"
finder = RecFinder(FILE)


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        """Метод, отправляющий сообщение с JSON"""
        length = int(self.headers.get('content-length'))
        try:
            message = json.loads(self.rfile.read(length))
        except json.decoder.JSONDecodeError:
            message = json.dumps({'status': False, 'error': 'Bad request'}).encode('utf-8')
            self.response_to_client(code=423 , message=message)

        err = validator(data=message)
        if err:
            message = json.dumps({'status': False, 'error': err}).encode('utf-8')
            self.response_to_client(code=423, message=message)
        try:
            self.response_to_client(code=200, message=self.message_handler(message))
        except ErrorItemNotFound:
            message = json.dumps({'status': False, 'error': "Bad request"}).encode('utf-8')
            self.response_to_client(code=400, message=message)

    def response_to_client(self, code, message):
        """Отправка сообщения клиенту"""
        self._set_headers()
        self.send_response_only(code=code, message=message)
        self.end_headers()
        return None

    def message_handler(self, message):
        """Обработка сообщения от клиента и выдача списка"""
        # finder = RecFinder(FILE)
        if message.get("prob_threshold"):
            result = finder.find_recommendations(message["recommend_item"], message["prob_threshold"])
            return {"status": True,"target_list": result}
        else:
            result = finder.find_recommendations(message["recommend_item"])
            return {"status": True,"target_list": result}



def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    run()