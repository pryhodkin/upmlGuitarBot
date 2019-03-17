import telebot

import constants
import functions


bot = telebot.TeleBot(constants.token)

functions.SortMusic(constants.music_array)

hide_markup = telebot.types.ReplyKeyboardRemove()

artist_markups = functions.SetMarkupArtists(functions.Artists(constants.music_array))

songs = []

functions.ArrayAward(songs, functions.Shaker(constants.music_array, 1))

functions.SortMusic(constants.music_array)


"""
user_markup_artists.row('✖')
user_markup_artists.row('ДДТ','The White Stripes','Imagine Dragons', 'Radio Tapok')
"""

@bot.message_handler(commands = ['lyrics'])

def handle_lyrics(message):

    user_markup = functions.SongsMarkup(songs)

    bot.send_message(message.from_user.id, "Вот всё что есть", reply_markup = user_markup)





@bot.message_handler(commands = ['help', 'start'])

def handle_help(message):

    bot.send_message(message.chat.id, "Вот что я умею:" + "\n" +
                     "/help - список всех моих сверхспособностей" + "\n" +
                     "/lyrics - найти текст песни" + "\n" +
                     "/start - запустить меня" + "\n" +
                     "/artist - искать по исполнителю")






@bot.message_handler(commands = ['artist'])

def handle_artist(messege):

    user_markup = functions.SetMarkupArtists(functions.Artists(constants.music_array))

    bot.send_message(messege.from_user.id, 'Чья песня?', reply_markup = user_markup)




@bot.message_handler(content_types = ['text'])

def handle_text(message):

    user_text = message.text

    if message.text == "В глубь нашей родины":

        bot.send_message(message.chat.id, "Идёт нациский марш")

    if message.text == '✖':

        bot.send_message(message.from_user.id,'Скрываю клаву', reply_markup = hide_markup)

    if message.text == 'Исполнители':

        user_markup = functions.SetMarkupArtists(functions.Artists(constants.music_array))

        bot.send_message(message.from_user.id, 'Чья песня?', reply_markup = user_markup)

    if functions.Check(user_text, '-'):

        user_text = functions.Sub(user_text)[1]

    i = 1

    while i < functions.Count(constants.music_array):

        if constants.music_array[i][1] == user_text:

            bot.send_message(message.from_user.id, constants.music_array[i][2])

        i += 1

    i = 0

    while i < functions.Count(functions.Artists(constants.music_array)):

        if functions.Artists(constants.music_array)[i] == user_text:

            user_markup = functions.SetMarkup(constants.music_array, user_text)

            bot.send_message(message.from_user.id, 'Выбирай', reply_markup = user_markup)

        i += 1






bot.polling(none_stop = True, interval = 0)