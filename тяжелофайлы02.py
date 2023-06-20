import csv
import time

with open('rows_300.csv', mode='w', newline='') as csv_file:
    fieldnames = ['№', 'Дата и время', 'Секунда', 'Микросекунда']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for i in range(1, 301):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        current_second = time.strftime('%S')
        current_microsecond = time.strftime('%f')

        writer.writerow({'№': i, 'Дата и время': current_time, 'Секунда': current_second, 'Микросекунда': current_microsecond})

        time.sleep(0.01)
