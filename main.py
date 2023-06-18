import os
from utilts.utilts import read_json, get_latest_notes
from directory_class.class_operations import Operation
# Глобальная переменная содержащая путь к обрабатываемому файлу
DATA = os.path.join('date', 'operations.json')


def main(path: str):
    # Получение списка данных из файла
    first_data = read_json(path)
    # Получение списка данных для вывода пользователю
    finish_data = get_latest_notes(first_data)
    # Приведение к классу для обработки данных
    try_2 = [Operation(note) for note in finish_data]
    # Вывод обработанной информации пользователю
    for i in try_2:
        print(f'{i.get_data()} {i.get_description()}\n'
              f'{i.mean_description_from()} -> {i.mean_description_to()}\n'
              f'{i.get_amount_operation()}\n')


if __name__ == "__main__":
    main(DATA)
