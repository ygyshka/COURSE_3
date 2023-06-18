from utilts.utilts import read_json, get_latest_notes


def test_read_json(test_way, test_data):
    assert read_json(test_way) == test_data


def test_get_latest_notes_exec():
    """
       тест для функции test_five_last_successful_operations - возвращает последние 5 успешных операций
       """
    test_list = [{'date': '2019-12-08T22:46:21.935582', 'state': 'None'},
                 {'date': '2019-12-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {'date': '2018-12-08T22:46:21.935582', 'state': 'None'},
                 {'date': '2018-12-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {'date': '2017-11-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {'date': '2016-01-08T22:46:21.935582', 'state': 'None'},
                 {'date': '2018-03-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {'date': '2017-10-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {},
                 {'date': '2019-12-08T22:46:21.935582', 'state': 'None'},
                 {'date': '2015-09-08T22:46:21.935582', 'state': 'EXECUTED'},
                 {'date': '2011-12-08T22:46:21.935582', 'state': 'EXECUTED'}]
    assert get_latest_notes(test_list) == [{'date': '2019-12-08T22:46:21.935582', 'state': 'EXECUTED'},
                                           {'date': '2018-12-08T22:46:21.935582', 'state': 'EXECUTED'},
                                           {'date': '2018-03-08T22:46:21.935582', 'state': 'EXECUTED'},
                                           {'date': '2017-11-08T22:46:21.935582', 'state': 'EXECUTED'},
                                           {'date': '2017-10-08T22:46:21.935582', 'state': 'EXECUTED'}]
