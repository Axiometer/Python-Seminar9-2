import os
import phonebook_files
import phonebook_view

from aiogram import Bot, Dispatcher, executor, types

bottask = ''

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
    TOKEN = file.readline().strip()

bot = Bot(TOKEN)
dp = Dispatcher(bot)

filename = os.path.dirname(os.path.realpath(__file__)) + '/phonebook.csv'
phonebook = phonebook_files.read_from_csv(filename)

# Приветствие
@dp.message_handler(commands=['start', 'старт'])
async def start(message: types.Message):
    name = message.from_user.full_name
    text = """
        Выберите действие:

        /A: Добавить контакт
        /L: Вывести список контактов
        /S: Поиск контакта
        /R: Удалить контакт
        /E: Экспорт файла
        /Q: Выход
        """
    await message.answer(f'{name}, Доброго времени суток!\n{text}')

@dp.message_handler(commands=['L', 'l'])
async def list_database(message: types.Message):
    text = phonebook_view.list_contacts(phonebook)
    await message.answer(text)


@dp.message_handler(commands=['S', 's'])
async def search_database(message: types.Message):
    global bottask
    bottask = 'search'
    await message.answer('Введите текст для поиска:')

@dp.message_handler(commands=['A', 'a'])
async def append_database(message: types.Message):
    global bottask
    bottask = 'append'
    await message.answer('Введите контакт для добавления в формате <ФИО>, <телефон>, <комментарий>:')

@dp.message_handler(commands=['R', 'r'])
async def remove_database(message: types.Message):
    global bottask
    bottask = 'remove'
    await message.answer('Введите имя контакта для удаления:')

@dp.message_handler(commands=['E', 'e'])
async def expoert_database(message: types.Message):
    global bottask
    bottask = 'export'
    await message.answer('Введите имя файла для экспорта:')

@dp.message_handler()
async def mainhandler(message: types.Message):
    global bottask
    items = []
    text = '...неизвестная команда...'
    if bottask == 'search':
        text = phonebook_view.search_contact(phonebook, message.text)
        bottask = ''
    if bottask == 'append':
        items = message.text.split(',')
        if len(items) != 3:
            text = "Введено неправильное количество данных"
        else:
            print(items)
            add_item(phonebook, items[0], items[1], items[2])
            text = f'Контакт {items[0]}, {items[1]}, {items[2]} успешно добавлен...'
        bottask = ''
    if bottask == 'remove':
        for index, item in enumerate(phonebook):
            if message.text.lower() in item["fullname"].lower():
                text = f'Найдено => ФИО: {item["fullname"]} | Телефон: {item["number"]} | Комментарий: {item["comment"]} | Номер записи: {index}\n'
                phonebook.pop(index)
        if text == '...неизвестная команда...':
            text = 'Ничего не найдено'
        else:
            text += 'Записи удалены'
        bottask = ''
    if bottask == 'export':
        phonebook_files.write_to_csv(phonebook, message.text)
        text = f'Файл {message.text} создан на сервере'
        bottask = ''
    await message.answer(text)

def add_item(phonebook, name, number, comment):
    bookitem = {"fullname": "", "number": "", "comment": ""}
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem['comment'] = comment
    phonebook.append(bookitem)
