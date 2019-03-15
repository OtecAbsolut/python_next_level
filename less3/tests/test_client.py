from less3.client import create_message, start_connect

TEST_MESSAGE_LIST = [
    'some not dict text',
    {'name_client': 'Client1', 'event': 'start'},
    {'name_client': 'Client1', 'event': 'message', 'text': 'Здраствуйте, не подскажите как пройти в библиотеку?'}
]

ASSERT_MESSAGE = [
    b'"some not dict text"',
    b'{"name_client": "Client1", "event": "start"}',
    b'{"name_client": "Client1", "event": "message", "text": "\\u0417\\u0434\\u0440\\u0430\\u0441\\u0442\\u0432\\u0443\\u0439\\u0442\\u0435, \\u043d\\u0435 \\u043f\\u043e\\u0434\\u0441\\u043a\\u0430\\u0436\\u0438\\u0442\\u0435 \\u043a\\u0430\\u043a \\u043f\\u0440\\u043e\\u0439\\u0442\\u0438 \\u0432 \\u0431\\u0438\\u0431\\u043b\\u0438\\u043e\\u0442\\u0435\\u043a\\u0443?"}'
]

START_RESULT = ['Сервер не отвечает', 'До свидание']


def test_create_message():
    for i, text in enumerate(TEST_MESSAGE_LIST):
        result = create_message(text)
        assert result == ASSERT_MESSAGE[i]


def test_start_connect():
    result = start_connect(5)
    if result in START_RESULT:
        answer = 'ok'
    else:
        answer = 'error'
    assert answer == 'ok'
