from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Привет! Я бот, умею считать слова во фразе.')

# написать небольшой смол-ток: 
# на привет - говорить "привет", на вопрос "как дела" - как дела?
# на все остальные фразы - предлагать посчитать слова во фразе, причем попростиь пользователя написать фразу,
# в котоной нужно посчитать слова в кавычках
# как-то нужно обрезать весь текст внутри кавычек и пробелы в начале и в конце фразы (S.strip([chars]))
# дальше псчитать число пробелов, число слов будет равно число пробелов + 1.
# ответить пользователю: в этой фразе 3 слова (тут еще написать словарик для числительных)

def help(bot, update):
    update.message.reply_text('Я рад помочь!')

def talk_to_me(bot, update):
	bot.sendMessage(update.message.chat_id, update.message.text)	
	print('Пришло сообщение', update.message.text)

def run_bot():
	updater = Updater ('279757366:AAGUtJn40HUudqOoLe-geB4UpLDMFaEQPoY')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler(['Help!'], help))
#	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	run_bot()