import os
import sqlite3
import os

from config import DB_PATH

if not os.path.exists(DB_PATH):
    db = sqlite3.connect(DB_PATH, check_same_thread=False)

    cursor = db.cursor()
    cursor.execute(
        """create table urls(
               long_url  varchar not null
                    constraint UK_Long
                        unique,
               short_url varchar not null
                    constraint UK_Short
                        unique,
               constraint urls_pk
                    primary key (short_url, long_url)
    )"""
    )

    # cursor.execute("create unique index sqlite_autoindex_urls_3 on urls (short_url)")
    # cursor.execute("create unique index urls_long_url_uindex on urls (long_url)")
    # cursor.execute("create unique index urls_short_url_uindex on urls (short_url)")

    db.commit()
    cursor.close()

    db.close()

db = sqlite3.connect(DB_PATH, check_same_thread=False)


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
    result = cursor.fetchone()
    cursor.close()

    if not result:  # для None
        return result

    return result[0]


def get_short_by_long(long: str):
    """
    Функция запрашивает короткую строку через длинную.
    :param long: передаем длинную ссылку в виде строки
    :return: короткая строка
    """
    cursor = db.cursor()
    query = "SELECT short_url FROM urls WHERE long_url = '%s'" % long
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if not result:  # для None
        return result

    return result[0]


def get_last_row() -> str:
    """
    Получение последней записи из таблицы urls

    :return: последняя запись
    """

    cursor = db.cursor()
    cursor.execute("SELECT short_url FROM urls ORDER BY short_url DESC LIMIT 1")

    result = cursor.fetchone()

    cursor.close()

    if not result:  # для None
        return result

    return result[0]


if __name__ == '__main__':
    get_last_row()
