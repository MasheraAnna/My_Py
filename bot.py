from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Привет!')

def talk_to_me(bot, update):
	bot.sendMessage(update.message.chat_id, text='Как интересно! Скажи что-нибудь еще :)')	
	print('Пришло сообщение', update.message.text)

def run_bot():
	updater = Updater ('279757366:AAGUtJn40HUudqOoLe-geB4UpLDMFaEQPoY')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	run_bot()