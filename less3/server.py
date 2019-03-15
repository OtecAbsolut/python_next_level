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
from less3.client import create_message
import time


IP = '0.0.0.0'
PORT = 7777
print('Сервер запущен и слушает порт:', PORT)

sock = socket.socket()
sock.bind((IP, PORT))
sock.listen(5)

error_answer = {
    'status': 400,
    'answer': 'Не верный формат запроса'
}

while True:
    client, address = sock.accept()
    print(f'Установленно соединение с => {address}')
    data = client.recv(2048)

    try:
        msg = json.loads(data)
        event = msg['event']
        name = msg['name_client']
        print(f'Получено сообщение:\n{msg}')
    except Exception as error:
        event = 'error'
        name = None
        print(f'Ошибочка => {error}')

    if event == 'start':
        answer = f'{name}, добро пожаловать в наш сервис'
        answer_data = {
            'status': 200,
            'answer': answer
        }
        send_msg = json.dumps(answer_data)
        client.send(send_msg.encode())

        while True:
            second_data = client.recv(2048)
            try:
                second_msg = json.loads(second_data)
                event = second_msg['event']
                print(f'Получено сообщение:\n{second_msg}')
            except Exception as error:
                event = 'error'
                print('Не опознанное сообщений')

            if event == 'message':
                answer = f'Уважаемый {name}, библиотека находится за углом'
                answer_data = {
                    'status': 200,
                    'answer': answer
                }
                send_msg = json.dumps(answer_data)
                client.send(send_msg.encode())
            else:
                try:
                    client.send(create_message(error_answer))
                except BrokenPipeError:
                    print('Сообщения закончились')
                    client.close()
                    break
            time.sleep(1)
    else:
        client.send(create_message(error_answer))
