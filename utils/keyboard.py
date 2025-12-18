from telegram import ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            ["🃏 Карта дня", "🔮 Три карты"],
            ["❤️ На любовь", "💼 На работу"],
            ["🗓 На месяц", "⚖️ Выбор"],
        ],
        resize_keyboard=True,
    )
