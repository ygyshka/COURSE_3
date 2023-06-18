import json
from operator import itemgetter


def read_json(path: str):
    """
    Функция чтения файла формата json, перевод в формат python
    :param path:
    :return:
    """
    with open(path, encoding='UTF-8') as data_json:
        python_list = json.loads(data_json.read())
    return python_list


def get_latest_notes(list_notes: list):
    """
    Сортировка полученных данных из файла json , по дате и статусу.
    Вывод последних 5 записей по дате
    :param list_notes:
    :return:
    """
    list_work = []
    sort_data = sorted(
        [note for note in list_notes if note.get('date') is not None], key=itemgetter('date'), reverse=True)
    for note_ in sort_data:
        if len(list_work) < 5:
            if note_['state'] == 'EXECUTED':
                list_work.append(note_)
            else:
                continue
        else:
            break
    return list_work












