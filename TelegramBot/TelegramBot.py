import telegram.ext
import qrcode
import qrcode.image.svg
  

with open('TelegramBot/token.txt', 'r') as f:
    Token = f.read()


def start(update, context):
    update.message.reply_text("Hello! Welcome to Bot AtKit")
    
def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About Bot Atkit
    /contact -> Information About Contact 
    /picture -> Bot's Favourite Picture    
    /text_to_qr -> Convert Text To QR Code                  
    """)

def content(update, context):
    update.message.reply_text("We have a vedio over Bot AtKit and watch it!!!")
    
def contact(update, context):
    update.message.reply_text("mdataurlikhon00@gmail.com")
    
def picture(update, context):
    update.message.reply_photo(open('TelegramBot/general.png', 'rb'))
    
def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")

def text_to_qr(update, context):
    text_in = update.message.text 
    text_in = text_in[11:]   
    img = qrcode.make(text_in)
    img.save('Project_Misc/TelegramBot/bot.png')
    update.message.reply_photo(open('TelegramBot/bot.png', 'rb'))

updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("picture", picture))
disp.add_handler(telegram.ext.CommandHandler("text_to_qr", text_to_qr))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
