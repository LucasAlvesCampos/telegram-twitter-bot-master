import common

from telegram.ext import Updater, CommandHandler

#command handlers
def subscribe(bot, update):
	if update.message.chat_id not in common.subscribers:
		common.subscribers.append(update.message.chat_id)
		bot.sendMessage(update.message.chat_id, text='Subscribed!')
		common.saveSubscribers(common.subscribers)
	else:
		bot.sendMessage(update.message.chat_id, text='Already Subscribed!')


def unsubscribe(bot, update):
	if update.message.chat_id in common.subscribers:
		common.subscribers.remove(update.message.chat_id)
		bot.sendMessage(update.message.chat_id, text='Unsubscribed!')
		common.saveSubscribers(common.subscribers)
	else:
		bot.sendMessage(update.message.chat_id, text='You need to subscribe first!')

def bot_main(bot_token=""):
	# Create the EventHandler and pass it your bot's token.
	updater = Updater(token="813504010:AAF6By3udXz6r5dKKieb7Ixrc7eu7WNyYFY")

	common.bot = updater.bot

	# Get the dispatcher to register handlers
	dispatcher = updater.dispatcher

	# on different commands - answer in Telegram
	subscribe_handler = CommandHandler("subscribe", subscribe)
	dispatcher.add_handler(subscribe_handler)
	unsubscribe_handler = CommandHandler("unsubscribe", unsubscribe)
	dispatcher.add_handler(unsubscribe_handler)

	# Start the Bot
	updater.start_polling(timeout=5)

	# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT
	updater.idle()