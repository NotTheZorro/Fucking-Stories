# coding=UTF-8
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.utils.request import Request
from telegram.ext.dispatcher import run_async
import toml
import time
import datetime
import logging

bot = telegram.Bot('TOKEN', request = Request(con_pool_size = 24, connect_timeout = 120))
# noinspection PyArgumentList
logging.basicConfig(handlers = [logging.FileHandler('errors.log', 'w', 'utf-8')],
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.ERROR)
log = logging.getLogger(__name__)
try:
    posts = toml.load('posts.toml')
except:
    posts = dict()
    toml.dump(posts, open('posts.toml', 'w'))


@run_async
def check_delete():
    while True:
        try:
            for post in posts:
                if posts[post] < datetime.datetime.now():
                    bot.delete_message(posts[post][0], post)
        except Exception as e:
            log.error(e)
        time.sleep(60)


@run_async
def add_post(u, ctx):
    posts[str(u.message.message_id)] = [u.message.chat.id, u.message.date + datetime.timedelta(1)]
    toml.dump(posts, open('posts.toml', 'w'))
