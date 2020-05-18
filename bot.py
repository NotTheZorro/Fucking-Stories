# coding=UTF-8
from util import *


def main():
    updater = Updater(bot = bot, workers = 20, use_context = True)
    dispatch = updater.dispatcher
    try:
        dispatch.add_handler(MessageHandler(Filters.update.channel_post, add_post))
        updater.start_polling(clean = False)
        check_delete()
        updater.idle()
    except Exception as e:
        log.exception(f'Exception while running, {e}, {e.args}')
    finally:
        dispatch.stop()


while True:
    main()
    time.sleep(5)
