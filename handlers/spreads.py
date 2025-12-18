import random
from typing import List

from telegram import Update
from telegram.ext import ContextTypes

from data.tarot_deck import TAROT_DECK, TarotCard
from utils.logging import log_spread


async def card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(TAROT_DECK)
    log_spread("card_day", update.effective_user, [card])
    text = (
        "🃏 Карта дня\n\n"
        f"{card['name']}\n\n"
        f"Общее значение: {card['general']}\n"
        f"Совет: {card['advice']}"
    )
    await update.message.reply_text(text)


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cards = random.sample(TAROT_DECK, k=3)
    positions = ["Прошлое", "Настоящее", "Будущее"]

    lines = ["🔮 Расклад: прошлое / настоящее / будущее\n"]
    for pos, card in zip(positions, cards):
        lines.append(f"{pos}: {card['name']} — {card['general']}")

    log_spread("three_cards", update.effective_user, cards)
    await update.message.reply_text("\n".join(lines))


async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(TAROT_DECK)
    log_spread("love", update.effective_user, [card])
    text = (
        "❤️ Расклад на любовь и отношения\n\n"
        f"Карта: {card['name']}\n\n"
        f"В любви: {card['love']}\n\n"
        "Смотри на карту через призму чувств, партнёрства, открытости и доверия."
    )
    await update.message.reply_text(text)


async def work(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(TAROT_DECK)
    log_spread("work", update.effective_user, [card])
    text = (
        "💼 Расклад на работу и финансы\n\n"
        f"Карта: {card['name']}\n\n"
        f"В работе: {card['work']}\n"
        f"Финансы: {card['finance']}\n\n"
        "Смотри на карту через призму карьеры, проектов, денег и реализации себя."
    )
    await update.message.reply_text(text)


async def month(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cards = random.sample(TAROT_DECK, k=4)
    positions = ["Тема месяца", "Главный вызов", "Поддержка", "Результат / итоги"]

    lines = ["🗓 Расклад на месяц\n"]
    for pos, card in zip(positions, cards):
        lines.append(f"{pos}: {card['name']} — {card['general']}")

    log_spread("month", update.effective_user, cards)
    await update.message.reply_text("\n".join(lines))


async def situation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cards = random.sample(TAROT_DECK, k=3)
    positions = ["Что происходит", "Причина / корень", "Совет"]

    question = " ".join(context.args) if context.args else None

    lines = ["🌀 Расклад на ситуацию\n"]
    if question:
        lines.append(f"Вопрос: {question}\n")

    for pos, card in zip(positions, cards):
        lines.append(f"{pos}: {card['name']} — {card['general']}")

    log_spread("situation", update.effective_user, cards, question=question)
    await update.message.reply_text("\n".join(lines))


async def choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args or []

    if len(args) >= 2:
        # условный формат: /choice Вариант_A / Вариант_B
        raw = " ".join(args)
        parts = [p.strip() for p in raw.split("/") if p.strip()]
        option_a = parts[0] if len(parts) >= 1 else "Вариант A"
        option_b = parts[1] if len(parts) >= 2 else "Вариант B"
    else:
        option_a = "Вариант A"
        option_b = "Вариант B"

    cards = random.sample(TAROT_DECK, k=3)
    card_a, card_b, advice_card = cards

    lines = [
        "⚖️ Расклад на выбор\n",
        f"{option_a}: {card_a['name']} — {card_a['general']}",
        f"{option_b}: {card_b['name']} — {card_b['general']}",
        "",
        f"Совет: {advice_card['name']} — {advice_card['advice']}",
    ]

    question = " ".join(args) if args else None
    log_spread("choice", update.effective_user, cards, question=question)
    await update.message.reply_text("\n".join(lines))


async def handle_keyboard_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()

    if text == "🃏 Карта дня" or "Карта дня" in text:
        await card(update, context)
    elif text == "🔮 Три карты" or "Три карты" in text:
        await three(update, context)
    elif text == "❤️ На любовь" or "любов" in text:
        await love(update, context)
    elif text == "💼 На работу" or "работ" in text:
        await work(update, context)
    elif text == "🗓 На месяц" or "месяц" in text:
        await month(update, context)
    elif text == "⚖️ Выбор" or "Выбор" in text or "выбор" in text:
        await choice(update, context)
