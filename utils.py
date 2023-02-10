import datetime
import requests

from payment import Payment


URL = 'https://www.jsonkeeper.com/b/LZX7'

operations_list = sorted(
    requests.get(URL).json(),
    key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
    reverse=True
)

last_operations = []


def get_last_operations(operations: list, last_operations: list) -> None:
    for operation in operations:
        if operation['state'] == 'EXECUTED':
            if 'from' in operation:
                last_operations.append(Payment(operation['date'],
                                               operation['description'],
                                               operation['from'],
                                               operation['to'],
                                               operation['operationAmount']['amount'],
                                               operation['operationAmount']['currency']['name']))
            else:
                last_operations.append(
                    Payment(operation['date'],
                            operation['description'],
                                'Данные об отправителе отсутствуют',
                            operation['to'],
                            operation['operationAmount']['amount'],
                            operation['operationAmount']['currency']['name']))
        if len(last_operations) == 5:
            for operation in last_operations:
                print(operation.payment_info())
            break


get_last_operations(operations_list, last_operations)
