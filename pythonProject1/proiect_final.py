# proiect final
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7126876409:AAGgRwDAgj34AX8D5noB-OgMokA6J3QJgds'
BOT_USERNAME: Final = '@musicc_suggest_bot    '
async def start_command(update: Update, context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text('Hello! Want to listen to some music?')

async def help_command(update: Update, context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text('Please tell me what music you want to listen to?')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'pop' in processed:
        return 'Here are some options! \n Olivia Rodrigo \n Billie Eilish \n Melanie Martinez \n Harry Styles'
    if 'metal' in processed:
        return 'Here are some options! \n Metallica \n Iron maiden \n Slipknot \n Black Sabbath'
    if 'country' in processed:
        return 'Here are some options! \n Taylor Swift \n Carrie Underwood \n Garth Brooks'
    if 'rock' in processed:
        return 'Here are some options! \n AC/DC \n The Beatles \n Nirvana'

    return 'I dont understand what you wrote:('
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    print(f'Update {update} caused error {context.error}')

if __name__ := '_main_':
    print('Starting bot...')
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