"""
https://devman.org/encyclopedia/python_advanced/generator_internals/
"""

import requests


class SolutionAttemptsFetcher:
    """
    Генератор – это объект такого класса, который удовлетворяет протоколу итератора.
    Но генератор, в отличие от итератора, не обходит (не итерирует) коллекцию,
    а возвращает (генерирует) новые данные. Вот так выглядит генератор,
    который постранично загружает данные о попытках сдать задачи на devman.org:
    """

    SOLUTION_ATTEMPTS_URL = 'https://devman.org/api/challenges/solution_attempts/'
    PAGE_LIMIT = 10

    def __init__(self):
        self.current_page_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page_number >= SolutionAttemptsFetcher.PAGE_LIMIT:
            raise StopIteration()
        params = {'page': self.current_page_number}
        page = requests.get(SolutionAttemptsFetcher.SOLUTION_ATTEMPTS_URL,
                            params).json()
        self.current_page_number += 1
        return page['records']


def fetch_solution_attempts():
    """
    Тот же генератор как функция
    :return:
    """
    solution_attempts_url = 'https://devman.org/api/challenges/solution_attempts/'
    page_limit = 10
    for current_page_number in range(1, page_limit):
        params = {'page': current_page_number}
        page = requests.get(solution_attempts_url, params).json()
        yield page['records']


# Тоде самое про компрехеншены
def fetch_solution_attempts_page(page_number):
    solution_attempts_url = 'https://devman.org/api/challenges/solution_attempts/'
    params = {'page': page_number}
    page = requests.get(solution_attempts_url, params).json()
    return page['records']

page_limit = 10
attempt_pages = (
    fetch_solution_attempts_page(current_page_number)
    for current_page_number in range(1, page_limit)
)
for attempt_page in attempt_pages:
    print(len(attempt_page))