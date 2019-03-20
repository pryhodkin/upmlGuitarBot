import telebot

import constants
import functions


bot = telebot.TeleBot(constants.token)

hide_markup = telebot.types.ReplyKeyboardRemove()

SongsFile = open('DataBase/SongsFile.txt', 'rt', encoding = 'utf_8')

songs = []

functions.ArrayAward(songs, functions.ReadSongs(SongsFile))

SongsFile.close()

functions.SortMusic(songs)

CheckAdd = False

CheckAddArtist = False

CheckAddSong = False

CheckAddConfirm = False

NewSong = ['', '', '']

Admins = functions.ReadAdmins('DataBase/Admins.txt')


"""
user_markup_artists.row('✖')
user_markup_artists.row('ДДТ','The White Stripes','Imagine Dragons', 'Radio Tapok')
"""

@bot.message_handler(commands = ['lyrics'])

def handle_lyrics(message):

    functions.ArrayAward(songs, functions.Shaker(songs, 1))

    user_markup = functions.SongsMarkup(songs)

    functions.SortMusic(songs)

    bot.send_message(message.from_user.id, "Вот всё что есть", reply_markup = user_markup)


@bot.message_handler(commands = ['addadmin'])

def handle_addadmin(message):

    if message.from_user.id == 371404061:

        keys = open('DataBase/ActiveAdminKeys.txt', 'at', encoding = 'utf_8')

        key = str(functions.GetKey())

        keys.write(key + '\n')

        bot.send_message(message.from_user.id, 'Вот ключ: \n' + key + '\n Передай его тому кого надо добавить к списку админов.')

    else:

        bot.send_message(message.from_user.id,'Сорри, но добавить админа может только моя мать')



@bot.message_handler(commands = ['remove'])

def handle_remove(message):

    if functions.Check(Admins, str(message.from_user.id)):

        functions.ArrayAward(songs, functions.Shaker(songs, 1))

        user_markup = functions.SongsMarkup(songs)

        functions.SortMusic(songs)

        constants.CheckRemoveSong = True

        bot.send_message(message.from_user.id, 'Какую песню хочешь удолить?', reply_markup = user_markup)

    else:

        bot.send_message(message.from_user.id, "Сорри за мат конечно, но песни могут удолять только админы.")



@bot.message_handler(commands = ['add'])

def handle_add(message):

    if functions.Check(Admins, str(message.from_user.id)):

        bot.send_message(message.from_user.id, "Чью песню хочешь добавить?")

        constants.CheckAdd = True

    else:

        bot.send_message(message.from_user.id, "Сорри за мат конечно, но песни могут добавлять только админы.")





@bot.message_handler(commands = ['help', 'start'])

def handle_help(message):

    if functions.Check(Admins, str(message.from_user.id)):

        bot.send_message(message.chat.id, "Вот что я умею:" + "\n" +
                         "/help - список всех моих сверхспособностей" + "\n" +
                         "/lyrics - найти текст песни" + "\n" +
                         "/start - запустить меня" + "\n" +
                         "/artist - искать по исполнителю" +"\n\n"+
                         "А вот админские фичи (ты избранный!):" + "\n" +
                         "/adminhelp - все фичи админов" + "\n" +
                         "/add - добавить песню" + "\n" +
                         "/remove - удолить песню")

    else:

        bot.send_message(message.chat.id, "Вот что я умею:" + "\n" +
                     "/help - список всех моих сверхспособностей" + "\n" +
                     "/lyrics - найти текст песни" + "\n" +
                     "/start - запустить меня" + "\n" +
                     "/artist - искать по исполнителю")

@bot.message_handler(commands = ['adminhelp'])

def handle_adminhelp(message):

    if functions.Check(Admins, str(message.from_user.id)):

        bot.send_message(message.from_user.id, "А вот админские фичи (ты избранный!):" + "\n" +
                         "/adminhelp - все фичи админов" + "\n" +
                         "/add - добавить песню" + "\n" +
                         "/remove - удолить песню")

    else:

        bot.send_message(message.from_user.id, "Сорри за мат конечно, но ты не админ")






@bot.message_handler(commands = ['artist'])

def handle_artist(messege):

    user_markup = functions.SetMarkupArtists(functions.Artists(songs))

    bot.send_message(messege.from_user.id, 'Чья песня?', reply_markup = user_markup)




@bot.message_handler(content_types = ['text'])

def handle_text(message):

    if constants.CheckAdd and message.text != 'Всё, хуйня':

        NewSong[0] = message.text

        bot.send_message(message.from_user.id, "Ок, Теперь название")

        constants.CheckAdd = False

        constants.CheckAddArtist = True

    elif constants.CheckAddArtist and message.text != 'Всё, хуйня':

        NewSong[1] = message.text

        bot.send_message(message.from_user.id, "Теперь текст")

        constants.CheckAddArtist = False

        constants.CheckAddSong = True

    elif constants.CheckAddSong and message.text != 'Всё, хуйня':

        NewSong[2] = message.text

        user_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True)

        user_markup.row('Всё, хуйня')

        user_markup.row('#Confirm', 'Я ошипся')

        bot.send_message(message.from_user.id, NewSong[0] + ' - ' + NewSong[1] + '\n' + NewSong[2] + '\n' + 'Если всё ок жми #Confirm', reply_markup = user_markup)

        constants.CheckAddSong = False

        constants.CheckAddConfirm = True




    elif constants.CheckAddConfirm  and message.text != 'Всё, хуйня':

        if message.text == '#Confirm':

            SongsFile = open('DataBase/SongsFile.txt', 'at', encoding = 'utf_8')

            functions.WriteSong(SongsFile, NewSong[0], NewSong[1], NewSong[2])

            SongsFile.close()

            SongsFile = open('DataBase/SongsFile.txt', 'rt', encoding = 'utf_8')

            functions.ArrayAward(songs, functions.ReadSongs(SongsFile))

            functions.SortMusic(songs)

            SongsFile.close()

            constants.CheckAddConfirm = False

            bot.send_message(message.from_user.id, 'Всё добавил, чекай', reply_markup = hide_markup)

        elif message.text == 'Я ошипся':

            constants.CheckAddConfirm = False

            constants.CheckAdd = True

            bot.send_message(message.from_user.id, 'Ну что поделаешь \n повторим \n Кто говоришь исполняет?', reply_markup = hide_markup)

    elif message.text == 'Всё, хуйня':

        constants.CheckAddArtist = False

        constants.CheckAdd = False

        constants.CheckAddConfirm = False

        constants.CheckAddSong = False

        bot.send_message(message.from_user.id, 'Ну ок, нафиг нам нада эта новая песня?', reply_markup = hide_markup)


    else:

        user_text = message.text

        if message.text == "В глубь нашей родины":

            bot.send_message(message.chat.id, "Идёт нациский марш")

        if message.text == '✖':

            bot.send_message(message.from_user.id,'Скрываю клаву', reply_markup = hide_markup)

        if message.text == 'Исполнители':

            user_markup = functions.SetMarkupArtists(functions.Artists(songs))

            bot.send_message(message.from_user.id, 'Чья песня?', reply_markup = user_markup)

        if functions.Check(user_text, '-'):

            user_text = functions.Sub(user_text)[1]

        if constants.CheckRemoveSong:

            i = 1

            while i < functions.Count(songs):

                if songs[i][1] == user_text:

                    functions.DelSong(functions.Sub(message.text)[0], functions.Sub(message.text)[1])

                    bot.send_message(message.from_user.id, 'Всё, удолил песню: \n' + functions.Sub(message.text)[0] + ' - ' + functions.Sub(message.text)[1])

                    SongsFile = open('DataBase/SongsFile.txt', 'rt', encoding='utf_8')

                    functions.ArrayAward(songs, functions.ReadSongs(SongsFile))

                    functions.SortMusic(songs)

                    SongsFile.close()

                i += 1

            constants.CheckRemoveSong = False

        else:

            i = 1

            while i < functions.Count(songs):

                if songs[i][1] == user_text:

                    bot.send_message(message.from_user.id, songs[i][2])

                i += 1

            i = 0

            while i < functions.Count(functions.Artists(songs)):

                if functions.Artists(songs)[i] == user_text:

                    user_markup = functions.SetMarkup(songs, user_text)

                    bot.send_message(message.from_user.id, 'Выбирай', reply_markup = user_markup)

                i += 1

            if functions.Check(functions.ReadKeys('DataBase/ActiveAdminKeys.txt'), message.text):

                if functions.Check(Admins, str(message.from_user.id)):

                    functions.DelKey('DataBase/ActiveAdminKeys.txt', message.text)

                    bot.send_message(message.from_user.id, 'Чувак, твой ключ конечно правильный, но ты и так Админ')

                else:

                    functions.AddAdmin(message.from_user.username, message.from_user.id)

                    functions.DelKey('DataBase/ActiveAdminKeys.txt', message.text)

                    functions.ArrayAward(Admins, functions.ReadAdmins('DataBase/Admins.txt'))

                    bot.send_message(message.from_user.id, 'Теперь ты тоже, Твоё величество, Админ')







bot.polling(none_stop = True, interval = 0)