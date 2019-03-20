import socket
import json
import time
import random

# with open('config.json', 'r') as file:
#     config = json.load(file)

IP = 'localhost'
PORT = 7777

# Шаблон сообщения начала диалога
start = {
    'name_client': 'Client1',
    'event': 'start',
}

# Шаблон отправки сообщения на сервер
message = {
    'name_client': 'Client1',
    'event': 'message',
    'text': 'Здраствуйте, не подскажите как пройти в библиотеку?'
}

fail_message = 'Специальное сообщение не в формате json'


def create_message(data_dict):
    msg = json.dumps(data_dict)
    msg_byte = msg.encode()
    return msg_byte


def start_connect(count):
    # Открытие сокета и отправка сообщения
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))
    except ConnectionRefusedError:
        return 'Сервер не отвечает'

    sock.send(create_message(start))

    # ожидаем ответ от сервера
    data = sock.recv(1042)
    msg = json.loads(data)

    if msg['status'] == 200:
        print('Соединение установленно!')
        print(f'***Получено сообщение от сервера***\n'
              f'Статус: {msg["status"]}\n'
              f'Сообщение: {msg["answer"]}')
        for i in range(count):
            # Отправка второго сообщения
            random_message = [message, fail_message][random.randint(0, 1)]  # Выбираем случайное сообщение
            print(f'Отправляем сообщение => {random_message}')
            sock.send(create_message(random_message))
            sock.settimeout(2)

            try:
                data_answer = sock.recv(2048)
            except socket.timeout:
                print('Не дождались сообщения')
                continue

            answer = json.loads(data_answer)
            status = answer["status"]
            msg_client = answer['answer']

            if status == 200:
                print(f'***Получено сообщение от сервера***\n'
                      f'Статус: {status}\n'
                      f'Сообщение: {msg_client}')
            else:
                print('Ошибка')
                print(f'Статус: {status}\n'
                      f'Сообщение: {msg_client}')
                continue

    else:
        print('Ошибка')
        print(f'Статус: {msg["status"]}\n'
              f'Сообщение: {msg["answer"]}')
    sock.close()
    time.sleep(1)
    return 'До свидание'


if __name__ == '__main__':
    start_connect(6)
