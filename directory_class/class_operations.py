from datetime import datetime


class Operation:
    # def __init__(self, date_run=str, review=str, from_get=str, where_get=str, sum_money=str, currency=str):
    #     pass
    # def __init__(self, date_run, review, from_get=None, where_get=None, sum_money=None, currency=None):
    #
    #     self.date_run = date_run
    #     self.review = review
    #     self.from_get = from_get
    #     self.where_get = where_get
    #     self.sum_money = sum_money
    #     self.currency = currency
    #
    # def __repr__(self):
    #
    #     return f'{self.date_run} {self.review}' \
    #            f'{self.from_get} {self.where_get}' \
    #            f'{self.sum_money} {self.currency}'
    def __init__(self, dict_operation):
        """
        Инициализация экземпляра класса
        :param dict_operation:
        """
        self.dict_operation = dict_operation if dict_operation else {}

    def __repr__(self):
        """
        Представление экземпляра класса
        :return:
        """
        return f'Operation: {self.dict_operation}'

    def get_data(self):
        """
        Получение даты операции по формату условия
        :return:
        """
        date = datetime.strptime(self.dict_operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        return date

    def get_description(self):
        """
        Получение описания операции
        :return:
        """
        return self.dict_operation['description']

    def mean_description_from(self):
        """
        Получение и кодировка исходящего пункта операции 
        :return: 
        """""
        if 'from' in self.dict_operation:
            title_from = self.dict_operation['from']
            digit_str = []
            sum_digit_in_str = sum(1 for i in title_from if i.isdigit())
            for i in title_from:
                if i.isdigit():
                    if len(digit_str) > 6 and (len(digit_str) < (sum_digit_in_str - 4 + digit_str.count(' '))):
                        digit_str.append('*')
                        if len(digit_str) % 4 == (0 + digit_str.count(' ')) and len(digit_str) > 0:
                            digit_str.append(' ')
                    else:
                        digit_str.append(i)
                        if len(digit_str) % 4 == (0 + digit_str.count(' ')) and 0 < len(digit_str) < sum_digit_in_str:
                            digit_str.append(' ')

            str_not_digit = ''.join([i for i in self.dict_operation['from'] if not i.isdigit()])
            if 'счет' in title_from.lower():
                return f"{str_not_digit}{''.join(digit_str[-7:]).replace(' ', '')}"
            else:
                return f"{str_not_digit}{''.join(digit_str[0:])}"

        else:
            return ""

    def mean_description_to(self):
        """
        Получение и кодировка пункта куда совершается операция
        :return:
        """
        way_disc_to = self.dict_operation.copy()['to']
        title = []
        sum_digit_in_str = sum(1 for i in way_disc_to if i.isdigit())
        for i in way_disc_to:
            if i.isdigit():
                if len(title) > 6 and len(title) < (sum_digit_in_str - 4 + title.count(' ')):
                    title.append('*')
                    if len(title) % 4 == (0 + title.count(' ')) and len(title) > 0:
                        title.append(' ')
                else:
                    title.append(i)
                    if len(title) % 4 == (0 + title.count(' ')) and 0 < len(title) < sum_digit_in_str:
                        title.append(' ')
        str_not_digit = ''.join([i for i in self.dict_operation['to'] if not i.isdigit()])
        if 'счет' in way_disc_to.lower():
            return f"{str_not_digit}{''.join(title[-7:]).replace(' ', '')}"
        else:
            return ""

    def get_amount_operation(self):
        """
        Получение информации о сумме операции и валюте операции
        :return:
        """
        return f'{self.dict_operation["operationAmount"]["amount"]}' \
               f' {self.dict_operation["operationAmount"]["currency"]["name"]}'
