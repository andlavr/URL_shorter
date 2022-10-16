import itertools
from string import ascii_lowercase
from app import db
from config import URL_LENGTH, BASE_URL

url_iterator = itertools.product(ascii_lowercase, repeat=URL_LENGTH)


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
        new_short_url = BASE_URL + ''.join(next(url_iterator))
        db.add_long_short_pair(long_url, new_short_url)

        return db.get_short_by_long(long_url)


def redirect(short_url: str = None):
    """
    :param short_url: передаем короткую ссылку в виде строки
    :return: обращение к функции поиска короткой строки в б/д
    """

    return db.get_long_by_short(short_url)


# if __name__ == '__main__':
#     url_shortener = UrlShortener()
#     url_shortener.shorten(
#         'https://www.google.com/search?q=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0+%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4&oq=ghjdthrf+gthtdjl&aqs=chrome.1.69i57j0i10l9.8201j1j15&sourceid=chrome&ie=UTF-8')
#     url_shortener.shorten('asd')
#     print(url_shortener.shorten('qwerty'))
#     #print(url_shortener.short_urls)
#     print('redirect:', (url_shortener.redirect('short.ly/aaaaa')))
