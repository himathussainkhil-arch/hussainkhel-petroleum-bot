# Telegram Echo Bot

A small Telegram bot built with Python and `pyTelegramBotAPI`.

## What it does

- Responds to `/start` with a welcome message
- Responds to `/help` with the available commands
- Echoes regular text messages back to the sender

## Run it

1. Create a bot with [@BotFather](https://t.me/BotFather) and rotate any token that was shared publicly.
2. Add the new token to Replit Secrets with the key `TELEGRAM_BOT_TOKEN`.
3. Start the **Telegram Bot** workflow, or run:

   ```bash
   python3 main.py
   ```

The bot uses long polling, so keep the process running while you want it online.