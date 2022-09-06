import logging
import json

FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

def get_logger(name):
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt=DATE_FORMAT)
    return logging.getLogger(name)

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None