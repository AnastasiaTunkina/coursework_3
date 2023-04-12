import json
from datetime import datetime


class Data:
    def __init__(self, path):
        self.path = path

    def get_data(self) -> list:
        """Get the data in json format"""

        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def __repr__(self):
        return f'Python Path: {self.path}'


class ReformattedData:
    def __init__(self, data: list):
        self.data = data

    def sort(self) -> list:
        """Sort the data"""

        self.data.sort(key=lambda x: datetime.strptime(x.get('date', '2000-01-01 00:00'), "%Y-%m-%d %H:%M"),
                       reverse=True)
        return self.data

    def reformat_data(self) -> list:
        """Reformat date and time data"""

        for dictionary in self.data:
            for key, value in dictionary.items():
                if key == 'date':
                    new_value = value.replace('T', ' ')
                    dictionary[key] = new_value[:16]
        return self.sort()

    def __repr__(self):
        return f'Python Data: {self.data}'

def main(data: list) -> list:
    """Main function"""

    last_operations = []
    for dictionary in data:
        if 'state' in dictionary.keys():
            if dictionary['state'] == 'EXECUTED':
                date = dictionary['date'][:10]
                date = datetime.strptime(date, '%Y-%m-%d')
                correct_date = date.strftime('%d.%m.%Y')
                to_where = dictionary['to'].split(' ')
                if dictionary['description'] != 'Открытие вклада':
                    card = dictionary['from'].split(' ')
                    card_number = card[-1]
                    output = f'{correct_date} {dictionary["description"]}\n' \
                             f'{" ".join(card[:-1])} {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]} -> {"".join(to_where[:-1])} **{to_where[-1][-4:]}\n' \
                             f'{dictionary["operationAmount"]["amount"]} {dictionary["operationAmount"]["currency"]["name"]}'
                    last_operations.append(output)
                else:
                    output = f'{correct_date} {dictionary["description"]}\n' \
                             f'{"".join(to_where[:-1])} **{to_where[-1][-4:]}\n' \
                             f'{dictionary["operationAmount"]["amount"]} {dictionary["operationAmount"]["currency"]["name"]}'
                    last_operations.append(output)
    return last_operations