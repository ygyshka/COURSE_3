import os
from utilts.utilts import read_json, get_latest_notes
from directory_class.class_operations import Operation

DATA = os.path.join('date', 'operations.json')


def main(path: str):
    first_data = read_json(path)

    finish_data = get_latest_notes(first_data)

    try_2 = [Operation(note) for note in finish_data]
    for i in try_2:
        print(f'{i.get_data()} {i.get_description()}\n'
              f'{i.mean_description_from()} -> {i.mean_description_to()}\n'
              f'{i.get_amount_operation()}\n')


if __name__ == "__main__":
    main(DATA)
