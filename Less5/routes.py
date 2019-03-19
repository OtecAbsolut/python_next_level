import os
from functools import reduce
from importlib import __import__
from settings import INSTALLED_MODULES



def get_server_routes():
    return reduce(
        lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(
            lambda submodules, module: submodules + [getattr(module, 'routes', [])],
            reduce(
                lambda modules, module: modules + [__import__(f'{module}.routes')],
                INSTALLED_MODULES,
                []
            ),
            []
        ),
        []
    )

#
# def get_server_routes():
#     routes = []
#     modules = []
#
#     for itm in INSTALLED_MODULES:
#         module = __import__(f'{itm}.routes')
#         modules.append(module)
#
#     for module in modules:
#         routes.append(getattr(module, 'routes', []))
#     rout_collections = getattr(routes[0], 'routes', [])
#     return rout_collections


def resolve(action, routes=None):
    routes_mapping = {
        route['event']: route['controller']
        for route in routes or get_server_routes()
    }
    print(routes_mapping)
    return routes_mapping.get(action, None)


if __name__ == '__main__':
    # routs = [
    #     {'event': 'start', 'controller': start_message},
    #     {'event': 'message', 'controller': event_message},
    #     {'event': 'error', 'controller': error_answer}
    # ]
    request = {
        'name_client': 'Client1',
        'event': 'start',
    }
    print(get_server_routes())
    print(resolve('start'))
    routes = None
    routes_mapping = {
        route['event']: route['controller']
        for route in routes or get_server_routes()
    }
