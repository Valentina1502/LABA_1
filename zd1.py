#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

if __name__ == '__main__':
    # список работников
    workers = []

    # организация бесконечного цикла запроса команд
    while True:
        # запросить команду из терминала
        command = input(">>>").lower()

        # выполнить действие в соответствии с командой
        if command == 'exit':
            break

        elif command == 'add':
            # запрос данных пользователя
            name = input("Фамилия и инициалы? ")
            post = input("Должность? ")
            year = int(input("Год поступления? "))

            # создать словарь
            worker = {
                'name': name,
                'post': post,
                'year': year,
            }

            # добавление словаря в список
            workers.append(worker)
            # сортировка списка в случае необходимости
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Должность",
                    "Год"
                )
            )
            print(line)

            # вывод данных о всех сотрудниках
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('post', ''),
                        worker.get('year', '')
                    )
                )

            print(line)

        elif command.startswith('select '):
            # получить текущую дату
            today = date.today()

            # разобрать команду на части для выделения номера года
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый стаж
            period = int(parts[1])

            # Инициализировать счетчик
            count = 0
            # Проверить сведения работников из списка
            for worker in workers:
                if today.year - worker.get('year', today.year) >= period:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, worker.get('name', ''))
                    )
            # Если счетчик равен 0, то работники не найдены
            if count == 0:
                print("Работники с заданным стажем не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)