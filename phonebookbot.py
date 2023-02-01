from aiogram import Bot, Dispatcher, executor, types
import handlers

async def on_start(_):
    # Вывод в консоль информации о запуске
    print('Бот запущен')

if __name__ == '__main__':
    executor.start_polling(handlers.dp, skip_updates=True, on_startup=on_start)