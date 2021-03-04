#Web API для выдачи рекомендации по указанному товару

Сервис, позволяющий получить список рекомендаций по требуемому товару,
есть возможность опционально указать порог минимальной близости для рекомендаций.

## Как начать?
Для начала необходимо склонировать данный git-репозиторий.

Далее, в файле `server.py` в переменную `FILE` необходимо записать целевой файл для чтения(файл должен находиться в текущей директории), в переменную `PORT` можно записать порт,
на котором будет запускаться сервер(по умолчанию порт 8080).

Чтобы запустить сервер, в терминале текущей директории наберите команду `python3 server.py`, либо инициируйте запуск сервера в IDE соответствующим способом.

<ins>Сервер может запускаться от двух до пяти минут в зависимости от мощности компьютера</ins>

##Отправка и структура запроса
Запрос можно отправлять утилитой Postman или средствами python, используя библиотеку requests(на этот случай в директории есть файл `client.py`) 
На сервер можно отправлять POST-запросы по url `http://localhost:8080/application/json`:

####Для получения списка рекомендаций для указанного товара необходимо отправить запрос следующего вида:

`{"recommend_item":"QgybZB43EN"}`

Ответ сервера будет следующим :

``HTTP/1.0 200 {'status': True, 'target_list': ['lMFIE2oOr7', '2mLkIySjUe'
    ]
}``

####Для получения списка рекомендаций с опциональным параметром порога минимальной близости рекомендации, необходимо отправть запрос следующего вида: 

`{"recommend_item":"QgybZB43EN", "prob_threshold": 0.9}`

Ответ сервера:

`HTTP/1.0 200 {'status': True, 'target_list': ['2mLkIySjUe'
    ]
}`

####Важно: 
Ключи в словаре должны быть именно такими, как в примере, иначе сервер вернет ошибку 400,
как и на любой некорретный запрос:

Некорректный запрос:
`{
    "recommtem":"QgybZB43EN", "prob_threshold": 0.9
}`

Ответ сервера:

`HTTP/1.0 400 b'{"status": false, "error": ["error_bad_request"]}'`

Запрос с несуществующим ключом:

`{
    "recommend_item":"tovar", "prob_threshold": 0.9
}`

Ответ сервера:

`HTTP/1.0 400 b'{
    "status": false,
    "error": "Bad request"
}'`

###Стратегия масштабирования при увеличении нагрузки

При увеличении нагрузки можно использовать модуль Multiprocessing и класс Pool, который можно
использовать для параллельного выполнения функции между несколькими входами.

###Потребление ресурсов
Оперативная память: 11 Gb
Загрузка CPU старте сервера порядка 80% (Intel core i5, 2.2 GHz)
После старта сервера и записи данных в оперативную память, загрузка процессора возвращается к штатным значениям.

###Время ответа API
Время ответа составляет от 10 до 40 мс.

