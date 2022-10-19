import itertools
from string import ascii_lowercase

import db
from config import URL_LENGTH

url_iterator = itertools.product(ascii_lowercase, repeat=URL_LENGTH)


def check_iterator():
    """
     check_iterator предназначен для синхролнизации итератора с БД
    :return:
    """

    last_short_url = db.get_last_row()

    if not last_short_url:
        return None

    for i in url_iterator:
        if ''.join(i) == last_short_url:
            break

    return None


def shorten(long_url: str = None):
    """
    :param long_url: передаем длину ссылки в качестве строки
    :return: обращение к функции поиска короткой строки в б/д
    """

    if long_url is None:
        return None
    short_url = db.get_short_by_long(long_url)
    if short_url:
        return short_url
    else:
        new_short_url = ''.join(next(url_iterator))
        db.add_long_short_pair(long_url, new_short_url)

        return db.get_short_by_long(long_url)


def redirect(short_url: str = None):
    """
    :param short_url: передаем короткую ссылку в виде строки
    :return: обращение к функции поиска короткой строки в б/д
    """

    return db.get_long_by_short(short_url)


check_iterator()  # для синхронизации итератора с БД
