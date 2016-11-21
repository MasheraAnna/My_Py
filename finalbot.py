# -*- coding: utf-8 -*-
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardHide)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import re
import logging
import WordsCounter
import ephem
import datetime
import Calculator
import WCalculator

# Enable logging
LOG_FILENAME = 'finalbot.log'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename = LOG_FILENAME,
                    level=logging.INFO)

logger = logging.getLogger(__name__)


state = 'choice'

def start(bot, update):
    reply_keyboard = [['Калькулятор', 'Словарный калькулятор', 'Посчитать слова', 'Предсказать полнолуние', 'Поболтать']]
    update.message.reply_text(
        'Привет! Я Learn Python бот. Умею делать массу вещей.\n'
        'Выбери, пожалуйста, чем бы тебе хотелось заняться:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

def show_menue(bot, update):
    reply_keyboard = [['Калькулятор', 'Словарный калькулятор', 'Посчитать слова', 'Предсказать полнолуние', 'Поболтать']]
    update.message.reply_text(
        "Что будем делать дальше?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

# посчитать слова

def get_message(bot, update):
	global state
	state = "count_words"
	update.message.reply_text('Напиши фразу, в которой нужно посчитать слова в кавычках')

def count_words(bot, update):
	wordsCounter = WordsCounter.WordsCounter()
	state = wordsCounter.check_input(update.message.text)
	if state == True:
		result = wordsCounter.count()
		text = result + ". \n Напиши новую фразу (не забудь кавычки) или выбери /menue, чтобы вызвать меню"
		update.message.reply_text(text)
	else:
		text = wordsCounter.reply
		update.message.reply_text(text)

# словарный калькулятор

def words_calc(bot, update):
	update.message.reply_text('Это словарный калькулятор. Если ты напишешь числа и действия словами, я посчитаю результат.')

def user_check(bot, update):
	wCalc = WCalculator.WordCalc()
	global wMessage
	wMessage = update.message.text
	user_check = wCalc.user_check(update.message.text)
	update.message.reply_text(user_check)

def check(bot, update):
	global wMessage
	wCalc = WCalculator.WordCalc()
	if update.message.text == "да":
		check = wCalc.check(wMessage)
		global check
		check = True
	else:
		check = "Тогда введи текст заново"
		global check
		check = False
	update.message.reply_text(check)


# калькулятор

def calc(bot, update):
	global state
	state = "calc"
	update.message.reply_text('Это калькулятор. Напиши то, что хочешь посчитать, поставь равно и отправь сообщение')

def count (bot, update):
	calculator = Calculator.Calculator()
	result = str(calculator.count(update.message.text))

	if bool(re.search('\d', result)) == True :
		message = 'Ответ: ' + result + "\n Напиши новое задание для вычисления или выбери /menue, чтобы вернуться в меню"
		update.message.reply_text(message)
		global state
		state = "choice"
	else :
		message = result
		update.message.reply_text(message)
		state = "choice"


# полнолуние

def full_moon(bot, update):
	reply_keyboard = [['Калькулятор', 'Словарный калькулятор', 'Посчитать слова', 'Предсказать полнолуние', 'Поболтать']]
	date = datetime.date.today()
	text = "Следующее полнолуние " + str(ephem.next_full_moon(date)) + "\n" + "Давай сделаем что-нибудь еще:"
	update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

# поболтать

def talk_to_me(bot, update):
	update.message.reply_text('Давай поболтаем')



def main():
	# Create the EventHandler and pass it your bot's token.
	updater = Updater("294103086:AAFs0SVAbrYtjRkvMRfJ2keX2ffSd8R5mLo")
	# Get the dispatcher to register handlers
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('menue', show_menue)) 
	dp.add_handler(RegexHandler('^(Посчитать слова)$', get_message))
	# функции
	dp.add_handler(RegexHandler('^(Словарный калькулятор)$', words_calc))
	dp.add_handler(RegexHandler('^(Калькулятор)$', calc))
	dp.add_handler(RegexHandler('^(Предсказать полнолуние)$', full_moon))
	dp.add_handler(RegexHandler('^(Поболтать)$', talk_to_me))

	# dp.add_handler(MessageHandler(Filters.text, count))
	# dp.add_handler(MessageHandler(Filters.text, count_words))
	dp.add_handler(MessageHandler(Filters.text, user_check))

	# Start the Bot
	updater.start_polling()

	# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__=='__main__':
	main()


"""

тз:
1) поздороваться, т.е. вывести текст сообщения-приветствия,
предложить клавиатуру для ответа (отформатировать клавиатуру):
	а) посчитать число свлов во фразе
	б) обычный числовой калькулятор
	в) словарный калькулятор
	г) просто поболтать
	д) определить полнолуние

2) в зависимости от ответа пользователя выбрать дальнейший сценарий работы.
3) сценарии:
	а) посчитать число свлов во фразе
		1. попросить ввести фразу
		2. посчитать и вывести ответ
	б) обычный числовой калькулятор
	в) словарный калькулятор
	г) просто поболтать
	д) определить полнолуние

4) спросить не хочет ли пользователь чего-то еще, если да - пройти цикл сначала, если нет - перейти к прощанию
5) попрощаться
6) обработать ошибки

что делаем:
1) создаем класс, который выполняет различные сценарии в зависимости от ответа пользователя
	этот класс должен принимать в себя:
	а) стартовую функцию 
	б) список ответов
	в) список функций, которые он выполняет в зависимости от списка ответов
	он должен записывать ответы в логи тоже

2) создаем другой класс, который выполняет последовательность функций и записывает ответы в логи
	он принимает в себя
	а) массив с этими функциями

вопросики:

из файла conversationbot
спросить у Миши, что это такое? что делает эта функци? создает список? тогда как на него посмотреть?
зачем они делаю список, который нельзя вызвать?

"""