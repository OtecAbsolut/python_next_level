from datetime import datetime


def validate_request(raw):
    try:
        request_time = raw.get('name_client')
        request_action = raw.get('event')
    except AttributeError:
        return False

    if request_time and request_action:
        return True
    return False


def make_response(request, code, data=None):
    try:
        event = request.get('event')
        name = request.get('name_client')
    except AttributeError:
        event = None
        name = None
    return {
        'event': event,
        'name_client': name,
        'data': data,
        'code': code,
    }


def make_400(request):
    return make_response(request, 400, 'Wrong request format')


def make_404(request):
    return make_response(request, 404, 'Action is not supported.')
