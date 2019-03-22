from .controllers import (
    start_message, event_message, error_answer, test_example
)

routes = [
    {'event': 'start', 'controller': test_example},
    {'event': 'message', 'controller': event_message},
    {'event': 'error', 'controller': error_answer}
]
