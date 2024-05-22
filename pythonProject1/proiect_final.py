# proiect final
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7126876409:AAGgRwDAgj34AX8D5noB-OgMokA6J3QJgds'
BOT_USERNAME: Final = '@musicc_suggest_bot    '
async def start_command(update: Update, context: ContextTypes. DEFAULT_TYPE) :
    await update.message.reply_text('Hello! Want to listen to some music?')

async def help_command(update: Update, context: ContextTypes. DEFAULT_TYPE) :
    await update.message.reply_text('Please tell me what music you want to listen to?')

def handle_response(text: str):
    processed: str = text.lower()

    if 'pop' in text:
        return 'Here are some options!' /next('Olivia Rodrigo') /next('Billie Eilish') /next('Melanie Martinez') /next('Harry Styles')

    if 'metal' in text:
        return 'Here are some options!' /next('Metallica') /next('Iron maiden') /next('Slipknot') /next('Black Sabbath')

    if 'country' in text:
        return 'Here are some options!' /next('Taylor Swift') /next('Carrie Underwood') /next('Garth Brooks')

    return 'I dont understand what you wrote:('
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type

    text: str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    print(f'Update {update} caused error {context.error}')

if _name_ := '_main_':
    print( 'Starting bot...')
    app = Application.builder().token(TOKEN).build()
# Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
# Messages
    app.add_handler(MessageHandler (filters. TEXT, handle_message))
# Errors
    app.add_error_handler(error)

# Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)