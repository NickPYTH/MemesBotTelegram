import json
import os
import random

import cv2
import numpy as np
import requests
import telebot
from telebot import types
from textwrap3 import wrap

import config
import memes

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["all", "start"])
def show_all_collection_prices(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Создать свой мемасик", "Кнопочка")
    user_markup.row("Случайный мем")
    bot.send_message(message.chat.id, "Телеграмный генератор мемов")
    bot.send_photo(
        message.chat.id,
        photo=open("./hello.jpeg", "rb"),
        caption="Прssиветствую!",
        reply_markup=user_markup,
    )


@bot.message_handler(content_types=["text"])
def msg_receiver(message):
    if message.text == "Случайный мем":
        bot.send_photo(
            message.chat.id,
            photo=open(
                os.path.join(
                    config.RANDOM_MEMES_FOLDER, "{0}.jpeg".format(random.randint(1, 15))
                ),
                "rb",
            ),
            caption="{0}".format(
                config.EMOTIONS[random.randint(1, len(config.EMOTIONS)) - 1]
            ),
        )
    elif message.text == "В главное меню":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Создать свой мемасик", "Кнопочка")
        user_markup.row("Случайный мем")
        bot.send_message(message.chat.id, "Телеграмный генератор мемов")
        bot.send_message(
            message.chat.id,
            "Главное меню",
            reply_markup=user_markup,
        )
    elif message.text == "Создать свой мемасик":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Мем с Дрейком")
        user_markup.row("Мем с сильным и слабым доге")
        user_markup.row("Мем со сквидвардом")
        user_markup.row("Мем сверхразум")
        user_markup.row("Мем <иди работай!>")
        user_markup.row("В главное меню")
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в конструктор",
            reply_markup=user_markup,
        )
    elif message.text == "Мем с Дрейком":
        bot.send_photo(
            message.chat.id,
            photo=open(config.MEMES_URL.get("drake"), "rb"),
            caption=config.MEMES_DESCRIPTION.get("drake"),
        ),
    elif message.text == "Мем с сильным и слабым доге":
        bot.send_photo(
            message.chat.id,
            photo=open(config.MEMES_URL.get("doge"), "rb"),
            caption=config.MEMES_DESCRIPTION.get("doge"),
        ),
    elif message.text == "Мем со сквидвардом":
        bot.send_photo(
            message.chat.id,
            photo=open(config.MEMES_URL.get("sqrt"), "rb"),
            caption=config.MEMES_DESCRIPTION.get("sqrt"),
        ),
    elif message.text == "Мем сверхразум":
        bot.send_photo(
            message.chat.id,
            photo=open(config.MEMES_URL.get("supermind"), "rb"),
            caption=config.MEMES_DESCRIPTION.get("supermind"),
        ),
    elif message.text == "Мем <иди работай!>":
        bot.send_photo(
            message.chat.id,
            photo=open(config.MEMES_URL.get("lazy"), "rb"),
            caption=config.MEMES_DESCRIPTION.get("lazy"),
        ),
    elif message.text[:15] == "#sqrtmemecreate":
        msg = message.text[15:]
        rip_msg = ""
        doge_counter = 0
        for i, chr in enumerate(msg):
            if i == 0:
                if msg[0] != "@":
                    bot.send_message(message.chat.id, config.ERRORS.get("sqrt_error_1"))
                    break
            if chr == "@":
                doge_counter += 1
                if doge_counter > 1:
                    bot.send_message(message.chat.id, config.ERRORS.get("sqrt_error_2"))
                    break
            if doge_counter == 1 and chr != "@":
                rip_msg += chr
        if doge_counter < 1:
            bot.send_message(message.chat.id, config.ERRORS.get("sqrt_error_1"))
        else:
            if rip_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Пустая надпись!",
                )
            else:
                img_name = memes.create_sqrt_meme(rip_msg)
                bot.send_photo(
                    message.chat.id,
                    photo=open(
                        os.path.join(config.CREATED_MEMES_FOLDER, img_name), "rb"
                    ),
                    caption="Ваш мем готов",
                ),
    elif message.text[:15] == "#dogememecreate":
        msg = message.text[15:]
        top_msg = ""
        bottom_msg = ""
        doge_counter = 0
        for i, chr in enumerate(msg):
            if i == 0:
                if msg[0] != "@":
                    bot.send_message(message.chat.id, config.ERRORS.get("doge_error_1"))
                    break
            if chr == "@":
                doge_counter += 1
                if doge_counter > 2:
                    bot.send_message(message.chat.id, config.ERRORS.get("doge_error_3"))
                    break
            if doge_counter == 1 and chr != "@":
                top_msg += chr
            if doge_counter == 2 and chr != "@":
                bottom_msg += chr
        if doge_counter < 2:
            bot.send_message(message.chat.id, config.ERRORS.get("doge_error_2"))
        else:
            if top_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Первое значение пустое!",
                )
            elif bottom_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Второе значение пустое!",
                )
            else:
                img_name = memes.create_doge_meme(top_msg, bottom_msg)
                bot.send_photo(
                    message.chat.id,
                    photo=open(
                        os.path.join(config.CREATED_MEMES_FOLDER, img_name), "rb"
                    ),
                    caption="Ваш мем готов",
                ),
    elif message.text[:16] == "#drakememecreate":
        msg = message.text[16:]
        top_msg = ""
        bottom_msg = ""
        doge_counter = 0
        for i, chr in enumerate(msg):
            if i == 0:
                if msg[0] != "@":
                    bot.send_message(
                        message.chat.id,
                        config.ERRORS.get("drake_error_1"),
                    )
                    break
            if chr == "@":
                doge_counter += 1
                if doge_counter > 2:
                    bot.send_message(
                        message.chat.id,
                        config.ERRORS.get("drake_error_3"),
                    )
                    break
            if doge_counter == 1 and chr != "@":
                top_msg += chr
            if doge_counter == 2 and chr != "@":
                bottom_msg += chr
        if doge_counter < 2:
            bot.send_message(
                message.chat.id,
                config.ERRORS.get("drake_error_2"),
            )
        else:
            if top_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Первое значение пустое!",
                )
            elif bottom_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Второе значение пустое!",
                )
            else:
                img_name = memes.create_drake_meme(top_msg, bottom_msg)
                bot.send_photo(
                    message.chat.id,
                    photo=open(
                        os.path.join(config.CREATED_MEMES_FOLDER, img_name), "rb"
                    ),
                    caption="Ваш мем готов",
                ),
    elif message.text[:20] == "#supermindmemecreate":
        msg = message.text[20:]
        first_msg = ""
        second_msg = ""
        third_msg = ""
        four_msg = ""
        doge_counter = 0
        for i, chr in enumerate(msg):
            if i == 0:
                if msg[0] != "@":
                    bot.send_message(
                        message.chat.id,
                        config.ERRORS.get("drake_error_1"),
                    )
                    break
            if chr == "@":
                doge_counter += 1
                if doge_counter > 4:
                    bot.send_message(
                        message.chat.id,
                        config.ERRORS.get("drake_error_3"),
                    )
                    break
            if doge_counter == 1 and chr != "@":
                first_msg += chr
            if doge_counter == 2 and chr != "@":
                second_msg += chr
            if doge_counter == 3 and chr != "@":
                third_msg += chr
            if doge_counter == 4 and chr != "@":
                four_msg += chr
        if doge_counter < 4:
            bot.send_message(
                message.chat.id,
                config.ERRORS.get("drake_error_2"),
            )
        else:
            if (
                first_msg.strip() == ""
                or second_msg.strip() == ""
                or third_msg.strip() == ""
                or four_msg.strip() == ""
            ):
                bot.send_message(
                    message.chat.id,
                    "Одно из значений пустое!",
                )
            else:
                img_name = memes.create_supermind_meme(
                    first_msg, second_msg, third_msg, four_msg
                )
                bot.send_photo(
                    message.chat.id,
                    photo=open(
                        os.path.join(config.CREATED_MEMES_FOLDER, img_name), "rb"
                    ),
                    caption="Ваш мем готов",
                ),
    elif message.text[:15] == "#lazymemecreate":
        msg = message.text[15:]
        lazy_msg = ""
        doge_counter = 0
        for i, chr in enumerate(msg):
            if i == 0:
                if msg[0] != "@":
                    bot.send_message(message.chat.id, config.ERRORS.get("lazy_error_1"))
                    break
            if chr == "@":
                doge_counter += 1
                if doge_counter > 1:
                    bot.send_message(message.chat.id, config.ERRORS.get("lazy_error_2"))
                    break
            if doge_counter == 1 and chr != "@":
                lazy_msg += chr
        if doge_counter < 1:
            bot.send_message(message.chat.id, config.ERRORS.get("lazy_error_1"))
        else:
            if lazy_msg.strip() == "":
                bot.send_message(
                    message.chat.id,
                    "Пустая надпись!",
                )
            else:
                img_name = memes.create_lazy_meme(lazy_msg)
                bot.send_photo(
                    message.chat.id,
                    photo=open(
                        os.path.join(config.CREATED_MEMES_FOLDER, img_name), "rb"
                    ),
                    caption="Ваш мем готов",
                ),


bot.polling()
