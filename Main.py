from datetime import datetime

from Handler import Handler
from Note import Note

if __name__ == '__main__':
    a = Handler('notes.json')
    a.get()
    print('Для выхода введите команду - exit')
    while True:
        command = input("Введите нужную команду: \n1. Добавить - add \n2. Обновить - update "
                        "\n3. Удалить - delete \n4. Показать нужную заметку - show"
                        " \n5. Показать все заметки - show all \n")
        if command == "add":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            a.add(Note(title=title, msg=msg, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        elif command == "update":
            id = input('Введите индентификатор: ')
            a.update(id)
        elif command == "delete":
            id = input("Введите индентификатор: ")
            a.delete(id)
        elif command == "show":
            id = input("Введите индентификатор: ")
            a.show(id)

        elif command == "show all":
            isFiltered = True if input("Показать заметки за определнную дату (Введите +) \nПоказать все заметки (Введите -): ") == "+" else False
            a.showAll(isFiltered)
        elif command == "exit":
            break
        a.save()