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
            name = input("Имя: ")
            fam = input("Фамилия: ")
            year = input("Дата рождения (yyyy.mm.dd): ")
            tel = input("Телефон: (x-xxx-xxx-xx-xx): ")

            # создать словарь
            worker = {
                'name': name,
                'fam': fam,
                'year': year,
                'tel': tel,
            }

            # добавление словаря в список
            workers.append(worker)
            # сортировка списка в случае необходимости
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('year', ''))

        elif command.startswith('found '):

            # разобрать команду на части для выделения номера
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый номер
            phone = (parts[1])

            # Инициализировать счетчик
            count = 0
            # Проверить сведения работников из списка
            for worker in workers:
                if worker.get('tel', '') == phone:
                    count += 1
                    print(
                        '{:>4}: {:>15} | {:>15} | {:>15}'.format(count, worker.get('name', ''), worker.get('fam', ''), worker.get('tel', ''))
                    )
            # Если счетчик равен 0, то работники не найдены
            if count == 0:
                print("Работники с заданным телефоном не найдены.")

        elif command == 'all':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 20,
                '-' * 20,
                '-' * 12,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^20} | {:^20} | {:^12} | {:^20} |'.format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Год",
                    "Телефон"
                )
            )
            print(line)

            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:^4} | {:^20} | {:^20} | {:^12} | {:^20} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('fam', ''),
                        worker.get('year', ''),
                        worker.get('tel', '')
                    )
                )

            print(line)

        elif command == 'help':
            # Вывести справку о работе с программой
            print("Список команд:\n")
            print("add - добавить работника;")
            print("all - вывести список работников;")
            print("found <x-xxx-xxx-xx-xx> - найти работника по номеру;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)