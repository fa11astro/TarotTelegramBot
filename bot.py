from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import TOKEN
from handlers import commands, spreads


def main():
    """Точка входа в приложение."""
    if not TOKEN:
        raise RuntimeError("Не найден токен: установите переменную окружения BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    # Регистрация обработчиков команд
    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("help", commands.help_command))
    app.add_handler(CommandHandler("card", spreads.card))
    app.add_handler(CommandHandler("three", spreads.three))
    app.add_handler(CommandHandler("love", spreads.love))
    app.add_handler(CommandHandler("work", spreads.work))
    app.add_handler(CommandHandler("feedback", commands.feedback))
    app.add_handler(CommandHandler("month", spreads.month))
    app.add_handler(CommandHandler("situation", spreads.situation))
    app.add_handler(CommandHandler("choice", spreads.choice))

    # Обработчик текстовых сообщений (кнопки)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, spreads.handle_keyboard_text))

    app.run_polling()


if __name__ == "__main__":
    main()
