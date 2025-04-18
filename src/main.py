"""
Telegram bot that uses a LLM to process messages.
"""

import logging
from typing import Any

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from settings import settings
from weather import get_weather
from data_storage import save_note_to_file
from chains.notes import category_chain
from chains.response import response_chain
from chains.weather import weather_chain

# from chains.daily_report import daily_chain
from chains.question import question_chain

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def make_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Any:
    """Make a note."""

    note = " ".join(context.args)
    if not note:
        return update.message.reply_text("Please provide a note.")

    notes = category_chain.invoke(note)
    if notes is None:
        return update.message.reply_text("Could not process the note.")
    else:
        save_note_to_file(notes)
        logger.info("Saved note to database.")
    response = response_chain.invoke(notes.model_dump_json())

    return context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Any:
    """Get the weather for a given zipcode."""
    if not context.args:
        return update.message.reply_text("Please provide a zipcode.")
    try:
        zipcode = int(context.args[0])
    except ValueError:
        return update.message.reply_text("Please provide a valid zipcode.")

    weather_report = get_weather(zipcode)
    weather_summary = weather_chain.invoke(weather_report)
    return context.bot.send_message(
        chat_id=update.effective_chat.id, text=weather_summary
    )


def question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Any:
    """Answer a question."""
    question = " ".join(context.args)
    if not question:
        return update.message.reply_text("Please provide a question.")

    answer = question_chain.invoke(question)
    return context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("note", make_note))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(CommandHandler("question", question))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
