line = "-"*60 + "\n"

# функция поиска паттерна в контакте
def search_contact(phonebook, keyword) -> str:
    text = ''
    # нумеруем список словарей
    for index, item in enumerate(phonebook):
        # в каждом словаре ищем keyword в поле fullname
        if keyword.lower() in item["fullname"].lower():
            text +=f'Найдено => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Номер записи: {index}\n'
    if text != '':
        text += line
    else:
        text = f'По запросу {keyword} ничего не найдено'
    return text

# функция вывода списка контактов
def list_contacts(book) -> str:
    # шапка
    text = line + "ФИО\t\t|\tТелефон\t\t|\tКомментарий\n" + line
    # поэлементно проходим список. один элемент - словарь
    for item in book:
        text += f'{item["fullname"]}\t\t{item["number"]}\t\t{item["comment"]}\n'
    text += line
    return text