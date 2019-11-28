# 1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
# содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение;
# отправить сообщение серверу; получить ответ сервера; разобрать сообщение сервера;
# параметры командной строки скрипта client.py <addr> [<port>]:
# addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.
# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

import socket
import json
import time
from protocol import validate_request, make_response, make_400, make_404
import logging
from routes import resolve
from select import select

IP = '0.0.0.0'
PORT = 7777

logger = logging.getLogger('default')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('default.log')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

stream = logging.StreamHandler()
stream.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(stream)
logger.setLevel(logging.DEBUG)

sock = socket.socket()
sock.bind((IP, PORT))
sock.listen(5)
sock.settimeout(0)

logger.debug(f'Сервер запущен и слушает порт:{PORT}')
# error_answer = {
#     'code': 400,
#     'answer': 'Не верный формат запроса'
# }

connections = []
requests = []
try:
    while True:
        try:
            client, address = sock.accept()
            logger.debug(f'Установленно соединение с => {address}')
            connections.append(client)
        except BlockingIOError:
            pass

        rlist, wlist, xlist = select(connections, connections, [], 0)

        for client in rlist:

            data = client.recv(1024)

            try:
                request = json.loads(data)
                event = request['event']
                # name = msg['name_client']
                logger.debug(f'Получено сообщение:\n{request}')
                requests.append(request)
            except Exception as error:
                request, event = None, None
                requests.append(request)
                response = make_400(data.decode('utf-8'))
                logger.debug(f'Ошибочка => {error}')


        if requests:
            for request in requests:
                for client in wlist:
                    if validate_request(request):
                        logger.debug(request.get('event'))
                        controller = resolve(request.get('event'))
                        if controller:
                            try:
                                response = controller(request)
                                response_string = json.dumps(response)
                                client.send(response_string.encode('utf-8'))
                                logger.debug(f'Отправка сообщения: {response_string}')
                                if event == 'start':
                                    while True:
                                        second_data = client.recv(2048)
                                        request = json.loads(second_data)
                                        logger.debug(f'Получено сообщение: {request}')
                                        if validate_request(request):
                                            controller = resolve(request.get('event'))
                                            if controller:
                                                response = controller(request)
                                                logger.debug(response)
                                            else:
                                                response = make_404(request)
                                        else:
                                            response = make_404(request)
                                        response_string = json.dumps(response)
                                        logger.debug(f'Отправка сообщения: {response_string}')
                                        client.send(response_string.encode('utf-8'))
                            except Exception:
                                response = make_response(
                                    request, 500,
                                    'Internal server error.'
                                )
                        else:
                            response = make_404(request)
                    else:
                        response = make_400(request)


                    client.close()
        # if event == 'start':
        #     answer = f'{name}, добро пожаловать в наш сервис'
        #     answer_data = {
        #         'status': 200,
        #         'answer': answer
        #     }
        #     send_msg = json.dumps(answer_data)
        #     client.send(send_msg.encode())
        #
        #     while True:
        #         second_data = client.recv(2048)
        #         try:
        #             second_msg = json.loads(second_data)
        #             event = second_msg['event']
        #             print(f'Получено сообщение:\n{second_msg}')
        #         except Exception as error:
        #             event = 'error'
        #             print('Не опознанное сообщений')
        #
        #         if event == 'message':
        #             answer = f'Уважаемый {name}, библиотека находится за углом'
        #             answer_data = {
        #                 'status': 200,
        #                 'answer': answer
        #             }
        #             send_msg = json.dumps(answer_data)
        #             client.send(send_msg.encode())
        #         else:
        #             try:
        #                 client.send(create_message(error_answer))
        #             except BrokenPipeError:
        #                 print('Сообщения закончились')
        #                 client.close()
        #                 break
        #         time.sleep(1)
        # else:
        #     client.send(create_message(error_answer))
except KeyboardInterrupt:
    logger.debug('До новых встреч')
    sock.close()
finally:
    sock.close()
