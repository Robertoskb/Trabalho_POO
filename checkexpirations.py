from datetime import datetime
from data.jsonhandler import JsonHandler

date_format = r"%Y-%m-%d %H:%M:%S.%f"

parser_date = lambda date: datetime.strptime(date, date_format)
file = JsonHandler('data/data.json')


def check_expirations():
    now = datetime.now()
    data = file.read_json

    new_data = []
    for note in data:
        expiration = note['expiration']
        date = parser_date(note['date'])

        difference = now - date

        if difference.days <= expiration:
            new_data.append(note)

    file.write_json(new_data)

    return new_data
