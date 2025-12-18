## TarotTelegramBot

A small Telegram bot in Python for drawing and interpreting Tarot cards.  
The bot helps draw a card of the day, perform a simple spread, and collect feedback.

The bot works via the `python-telegram-bot` library and runs locally.

---

## Bot Features

- **Card of the Day**
  - Command: `/card`
  - Button: **🃏 Card of the Day**
  - Draws a random card and shows its general meaning and advice.

- **Three-Card Spread**
  - Command: `/three`
  - Button: **🔮 Three Cards**
  - Provides a "Past / Present / Future" spread using three different cards.

- **Love Card**
  - Command: `/love`
  - Button: **❤️ For Love**
  - Draws one card and suggests viewing it through the lens of relationships, emotions, and partnership.

- **Work & Finance Card**
  - Command: `/work`
  - Button: **💼 For Work**
  - Draws one card and focuses the interpretation on career, projects, and money (with a separate emphasis on finances).

- **Monthly Spread**
  - Command: `/month`
  - Button: **🗓 For the Month**
  - Four cards: theme of the month, main challenge, support, result/outcome.

- **Situation Spread**
  - Command: `/situation` or `/situation your question`
  - Provides three cards: what is happening, root cause, advice.
  - The question can be added as text after the command—it will be logged.

- **Choice Spread**
  - Command: `/choice` or `/choice option A / option B`
  - Three cards: card for the first option, card for the second option, and an advice card.

- **Help**
  - Command: `/help`
  - Shows a list of all commands and briefly explains what they do.

- **Feedback**
  - Command: `/feedback your text`
  - Saves feedback to a file `feedbacks.txt` next to the bot (for the bot author).

---

## Project Structure

The project is organized into modules for better code organization:

```
TarotTelegramBot/
├── bot.py                 # Entry point, handler registration
├── config.py              # Configuration and token loading
├── data/
│   └── tarot_deck.py      # Tarot card deck and types
├── handlers/
│   ├── commands.py        # Command handlers (start, help, feedback)
│   └── spreads.py         # Card spread handlers
├── utils/
│   ├── keyboard.py        # Keyboard creation
│   └── logging.py         # Spread logging
├── .env-example           # Example environment variables file
├── .gitignore             # Git ignored files
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

- **`bot.py`** — Main file that starts the bot and registers all command handlers.
- **`config.py`** — Loads the bot token from environment variables (`.env` file).
- **`data/tarot_deck.py`** — Contains the Tarot card deck (`TAROT_DECK`) and `TarotCard` type.
- **`handlers/commands.py`** — Handlers for basic commands: `/start`, `/help`, `/feedback`.
- **`handlers/spreads.py`** — Handlers for all spreads: `/card`, `/three`, `/love`, `/work`, `/month`, `/situation`, `/choice`, as well as button press handling.
- **`utils/keyboard.py`** — `main_keyboard()` function for creating the bot's main keyboard.
- **`utils/logging.py`** — `log_spread()` function for logging spreads to `spreads.log` file.

---

## Installation and Setup

### 1. Install Python

- Download Python from the official website (`python.org`) and install it.
- Important: When installing on Windows, check the box "Add Python to PATH".

Check in terminal:

```bash
python --version
```

If it outputs a version (for example, `Python 3.11.x`)—everything is fine.

### 2. Clone or download the project

If the project is already on GitHub:

```bash
git clone https://github.com/your-username/TarotTelegramBot.git
cd TarotTelegramBot
```

Or download the archive and extract it to the desired folder.

### 3. Create a virtual environment (Windows, PowerShell)

In PowerShell from the project folder:

```powershell
cd "C:\Users\YourName\Desktop\TarotTelegramBot"
py -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

The beginning of the line should show `(.venv)`—this means the environment is activated.

### 4. Install dependencies

The `requirements.txt` file contains the necessary libraries (mainly `python-telegram-bot`).

In the activated environment:

```powershell
pip install -r requirements.txt
```

### 5. Create a bot in Telegram and get a token

1. Open the user `@BotFather` in Telegram.
2. Send him the command `/newbot`.
3. Come up with a readable bot name (can be in Russian).
4. Come up with a bot `username` that ends with `bot` (for example, `TarotForFriendBot`).
5. BotFather will send a token like `123456789:AA...`—this is the secret key.

### 6. Set up environment variables

Create a `.env` file in the project root (copy `.env-example`):

```env
BOT_TOKEN=your_token_from_BotFather
```

Or set the environment variable in PowerShell:

```powershell
$env:BOT_TOKEN="your_token_from_BotFather"
```

### 7. Start the bot

Still in the same PowerShell session:

```powershell
python bot.py
```

If everything is successful:

- The console will output that the bot has started and is listening for updates.
- In Telegram, you can find the bot by its `@username`, press **Start**, and try the commands and buttons.

---

## Card Data Structure

Each card in `TAROT_DECK` is a dictionary with fields:

- `name` — card name
- `general` — general meaning
- `love` — meaning in love and relationships
- `work` — meaning in work and self-realization
- `finance` — meaning in the financial sphere
- `advice` — general advice from the card

The structure is easy to expand by adding new cards to `data/tarot_deck.py`.

---

This project is created for educational purposes. Feel free to use it!
