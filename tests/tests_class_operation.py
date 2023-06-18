from directory_class.class_operations import Operation

test_operation = {'date': '2019-12-08T22:46:21.935582',
                       'description': 'Открытие вклада',
                       'id': 863064926,
                       'operationAmount': {'amount': '41096.24',
                                           'currency': {'code': 'USD', 'name': 'USD'}},
                       'state': 'EXECUTED',
                       'to': 'Счет 90424923579946435907'}
test_operation_2 = {'date': '2019-12-07T06:17:14.634890',
                         'description': 'Перевод организации',
                         'from': 'Visa Classic 2842878893689012',
                         'id': 114832369,
                         'operationAmount': {'amount': '48150.39',
                                             'currency': {'code': 'USD', 'name': 'USD'}},
                         'state': 'EXECUTED',
                         'to': 'Счет 35158586384610753655'}

test_operation_3 = {'date': '2019-12-07T06:17:14.634890',
                         'description': 'Перевод организации',
                         'from': 'Счет 35158586384610753655',
                         'id': 114832369,
                         'operationAmount': {'amount': '48150.39',
                                             'currency': {'code': 'USD', 'name': 'USD'}},
                         'state': 'EXECUTED',
                         'to': 'Счет '}

test_1 = Operation(test_operation)
test_2 = Operation(test_operation_2)
test_3 = Operation(test_operation_3)


def test_date_operation():
    """
    тест для функции date_operation - возвращает дату в заданном формате
    """
    assert test_1.get_data() == '08.12.2019'
    assert test_2.get_data() == '07.12.2019'


def test_get_description():
    """
    тест для функции title_operation - возвращает название операции
    """
    assert test_1.get_description() == 'Открытие вклада'
    assert test_2.get_description() == 'Перевод организации'


def test_mean_description_from():
    """
    тест для функции meaning_from - возвращает поле откуда, если имеется
    """
    assert test_1.mean_description_from() == ''
    assert test_2.mean_description_from() == 'Visa Classic 2842 87** **** 9012'
    assert test_3.mean_description_from() == 'Счет **3655'


def test_mean_description_to():
    """
    тест для функции meaning_to - возвращает поле куда
    """
    assert test_1.mean_description_to() == 'Счет **5907'
    assert test_2.mean_description_to() == 'Счет **3655'
    assert test_3.mean_description_to() == 'Счет '


def test_get_amount_operation():
    """
    тест для функции amount_operation - возвращает сумму и валюту операции
    """
    assert test_1.get_amount_operation() == '41096.24 USD'