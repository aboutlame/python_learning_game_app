import telebot
from telebot import types

TOKEN = "7902109259:AAHkRGPFIkxrRrsph59QopPbXvJWDKVcigU"
bot = telebot.TeleBot(TOKEN)
WEB_APP_URL = "https://aboutlame.github.io/python_learning_game_app/"


@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Создаем inline-кнопку
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🚀 Запустить игру!", web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(btn)

    try:
        # Открываем локальный файл с картинкой
        with open("images/2.jpg", "rb") as photo:
            bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption="🐍 *Добро пожаловать в «Путь Пайтика»!*\n\n"
                "Это увлекательная игра, в которой ты изучаешь Python прямо в Telegram!\n\n"
                "Хочешь учиться с личным наставником? Жми /course",
                parse_mode="Markdown",
                reply_markup=markup,
            )
    except FileNotFoundError:
        # Если картинка не найдена, отправляем текст
        bot.send_message(
            chat_id=message.chat.id,
            text="🐍 *Добро пожаловать в «Путь Пайтика»!*\n\n"
            "Это увлекательная игра, в которой ты изучаешь Python прямо в Telegram!\n\n"
            "Хочешь учиться с личным наставником? Жми /course",
            parse_mode="Markdown",
            reply_markup=markup,
        )


@bot.message_handler(commands=["course"])
def promote_course(message):
    # Создаем inline-кнопку для записи
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="📝 Бесплатное занятие!",
        url="https://t.me/informatic_artem",
    )
    markup.add(btn)

    try:
        # Открываем картинку для курса
        with open("images/sign_up_course.jpg", "rb") as photo:
            bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption="📚 *Полная подготовка к ЕГЭ/ОГЭ по информатике с Артемом Александровичем!*\n\n"
                "Пайтик: «Я помогу с основами Python, но для экзамена нужно больше!»\n\n"
                "На курсе ты получишь:\n"
                "✨ Разбор всех типов задач ЕГЭ/ОГЭ\n"
                "🔥 Куратор на связи — ответит на любой вопрос\n"
                "📈 Техники решения задач на Python\n"
                "💻 Подготовку к сложным заданиям\n\n"
                "Жми кнопку ниже и напиши «Хочу на курс от Пайтика» 👇",
                parse_mode="Markdown",
                reply_markup=markup,
            )
    except FileNotFoundError:
        # Если картинки нет, отправляем текст
        bot.send_message(
            chat_id=message.chat.id,
            text="📚 *Полная подготовка к ЕГЭ/ОГЭ по информатике с Артемом Александровичем!*\n\n"
            "Пайтик: «Я помогу с основами Python, но для экзамена нужно больше!»\n\n"
            "На курсе ты получишь:\n"
            "✨ Разбор всех типов задач ЕГЭ/ОГЭ\n"
            "🔥 Куратор на связи — ответит на любой вопрос\n"
            "📈 Техники решения задач на Python\n"
            "💻 Подготовку к сложным заданиям\n\n"
            "Жми кнопку ниже и напиши «Хочу на курс от Пайтика» 👇",
            parse_mode="Markdown",
            reply_markup=markup,
        )


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling()
