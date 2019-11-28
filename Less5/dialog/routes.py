from .controllers import (
    start_message, event_message, error_answer
)

routes = [
    {'event': 'start', 'controller': start_message},
    {'event': 'message', 'controller': event_message},
    {'event': 'error', 'controller': error_answer}
]
