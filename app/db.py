import sqlite3
from config import DB_PATH

db = sqlite3.connect(DB_PATH)


def add_long_short_pair(long: str, short: str):
    """
    Добавление пары long/short url в БД

    :param long: передаем длинну ссылку в качестве строки
    :param short: передаем короткую ссылку в качестве строки
    :return: пара long/short
    """

    cursor = db.cursor()

    query = '''INSERT INTO urls VALUES (?, ?);'''
    data = (long, short)

    cursor.execute(query, data)

    db.commit()
    print("Данные из Python успешно добавлены в таблицу urls")
    cursor.close()


def get_long_by_short(short: str):
    """
    Функция запрашивает длинную строку через короткую.
    :param short: передаем короткую ссылку в виде строки
    :return: длинная строка
    """
    cursor = db.cursor()
    query = "SELECT long_url FROM urls WHERE short_url = '%s'" % short
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result



def get_short_by_long(long: str):
    """
    Функция запрашивает короткую строку через длинную.
    :param long: передаем длинную ссылку в виде строки
    :return: короткая строка
    """
    cursor = db.cursor()
    query = "SELECT short_url FROM urls WHERE long_url = '%s'" % long
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result

def get_last_row():
    """
    Получение последней записи из таблицы urls
    :return: последняя запись
    """

    cursor = db.cursor()
    query = "SELECT long_url FROM urls ORDER BY long_url DESC LIMIT 1"



if __name__ == '__main__':
    add_long_short_pair("123", "321")
