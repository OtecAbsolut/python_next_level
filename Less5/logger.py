import logging

def create_logger(path):
    logger = logging.getLogger('default')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(f'{path}')

    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)

    stream = logging.StreamHandler()
    stream.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(stream)
    logger.setLevel(logging.DEBUG)
    return logger
