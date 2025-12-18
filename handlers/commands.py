from telegram import Update
from telegram.ext import ContextTypes

from utils.keyboard import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я бот для трактовки карт Таро.\n\n"
        "Доступные варианты:\n"
        "🃏 Карта дня — общий совет на сейчас.\n"
        "🔮 Три карты — прошлое / настоящее / будущее.\n"
        "❤️ На любовь — карта про отношения.\n"
        "💼 На работу — карта про карьеру и деньги.\n"
        "🗓 На месяц — общий расклад на ближайший месяц.\n"
        "⚖️ Выбор — расклад на выбор между двумя вариантами.\n\n"
        "Выбери вариант на клавиатуре или используй команды: "
        "/card, /three, /love, /work, /month, /situation, /choice."
    )
    await update.message.reply_text(text, reply_markup=main_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✨ Помощь по боту Таро\n\n"
        "Основные команды:\n"
        "• /start — приветствие и основное меню.\n"
        "• /card — карта дня, общий совет.\n"
        "• /three — расклад: прошлое / настоящее / будущее.\n"
        "• /love — карта на любовь и отношения.\n"
        "• /work — карта на работу и финансы.\n"
        "• /month — общий расклад на месяц.\n"
        "• /situation — расклад на ситуацию (что происходит / причина / совет).\n"
        "• /choice — расклад на выбор между двумя вариантами.\n"
        "• /deck — показать всю колоду карт (отсортировано).\n"
        "• /feedback <текст> — оставить отзыв или пожелание автору.\n\n"
        "Также можно пользоваться кнопками под полем ввода сообщения."
    )
    await update.message.reply_text(text)


async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime

    if not context.args:
        await update.message.reply_text(
            "Чтобы оставить отзыв, напиши команду так:\n"
            "/feedback очень понравился расклад, хочу больше про отношения 💕"
        )
        return

    feedback_text = " ".join(context.args)
    user = update.effective_user
    username = f"@{user.username}" if user and user.username else "без username"
    user_id = user.id if user else "unknown"

    line = (
        f"[{datetime.utcnow().isoformat()}] "
        f"user_id={user_id}, {username}: {feedback_text}\n"
    )

    try:
        with open("feedbacks.txt", "a", encoding="utf-8") as f:
            f.write(line)
        await update.message.reply_text(
            "Спасибо за отзыв! 🌙 Я передам его автору бота."
        )
    except Exception:
        await update.message.reply_text(
            "Не удалось сохранить отзыв, но спасибо за попытку 💜"
        )
