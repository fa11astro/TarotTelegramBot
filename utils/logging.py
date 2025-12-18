from datetime import datetime
from typing import List

from data.tarot_deck import TarotCard


def log_spread(spread_type: str, user, cards: List[TarotCard], question: str | None = None) -> None:
    username = f"@{user.username}" if user and user.username else "без username"
    user_id = user.id if user else "unknown"
    card_names = ", ".join(card["name"] for card in cards)

    line = (
        f"[{datetime.utcnow().isoformat()}] "
        f"type={spread_type}; user_id={user_id}, {username}; "
        f"cards=[{card_names}]"
    )
    if question:
        line += f"; question={question}"
    line += "\n"

    try:
        with open("spreads.log", "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass
