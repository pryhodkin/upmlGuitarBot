import telebot
import psycopg2
import constants
import functions

bot = telebot.TeleBot(constants.token)

connection = psycopg2.connect(
    host = constants.host,
    database = constants.database,
    user = constants.user,
    password = constants.password
)

database = functions.Database(connection)

markup = functions.Markup()

user_markup = telebot.types.ReplyKeyboardMarkup()

hide_markup = telebot.types.ReplyKeyboardRemove()

requests = ['', []]

admin_list = ['', []]

add = {}

remove = {}

remove_admin = 0


@bot.message_handler(commands = ['start'])

def handle_start(message):

    if not database.CheckExistUser(message.from_user.id):

        user = [message.from_user.id,
                message.from_user.first_name,
                message.from_user.last_name,
                message.from_user.username,
                False,
                False,
                'first_question']

        database.AddToTable('users', user)

        user_markup = markup.YesNo('Есть', 'Нету')

        bot.send_message(message.from_user.id, constants._start['new'], reply_markup = user_markup)

    else:

        bot.send_message(message.from_user.id, constants._start['old'], hide_markup)


@bot.message_handler(commands = ['help'])

def handle_help(message):

    user = database.User(message.from_user.id)

    if user.creator:

        bot.send_message(user.id, constants._help['creator'])

    elif user.admin:

        bot.send_message(user.id, constants._help['admin'])

    else:

        bot.send_message(user.id, constants._help['user'])



@bot.message_handler(commands = ['lyrics'])

def handle_lyrics(message):

    user = database.User(message.from_user.id)

    database.ChangeCondition(user.id, 'lyrics_search')

    user_markup = markup.Songs(database, 'Lyrics')

    bot.send_message(user.id, constants._lyrics['lyrics_search'], reply_markup = user_markup)



@bot.message_handler(commands = ['close'])

def handle_close(message):

    user = database.User(message.from_user.id)

    database.ChangeCondition(user.id, 'None')

    if user.admin:

        bot.send_message(user.id, constants._close['admin'], reply_markup = hide_markup)

    else:

        bot.send_message(user.id, constants._close['user'], reply_markup = hide_markup)



@bot.message_handler(commands = ['inputkey'])

def handle_inputkey(message):

    user = database.User(message.from_user.id)

    database.ChangeCondition(user.id, 'input_key')

    bot.send_message(user.id, constants._inputkey['input_key'], hide_markup)



@bot.message_handler(commands = ['adminrequest'])

def handle_adminrequest(message):

    user = database.User(message.from_user.id)

    if user.creator:

        database.ChangeCondition(user.id, 'answer_requests')

        user_markup = markup.RequestAnswer()

        bot.send_message(user.id, constants._adminrequest['creator_requests'], reply_markup = user_markup)

    elif not user.admin:

        if not database.RequestExist(user.id):

            database.AddToTable('adminrequests', [user.id, False, False])

            bot.send_message(constants.Creator_id, constants._adminrequest['creator_request'].format(n = database.RequestsNumber()))

            bot.send_message(user.id, constants._adminrequest['user'])

        else:

            bot.send_message(user.id, constants._adminrequest['already_sent'])

    else:

        bot.send_message(user.id, constants._adminrequest['already_admin'])



@bot.message_handler(commands = ['addlyrics'])

def handle_addlyrics(message):

    user = database.User(message.from_user.id)

    if user.admin:

        database.ChangeCondition(user.id, 'addlyrics_artist')

        bot.send_message(user.id, constants._addlyrics['artist'], reply_markup = hide_markup)



@bot.message_handler(commands = ['removelyrics'])

def handle_removelyrics(message):

    user = database.User(message.from_user.id)

    if user.admin:

        remove[user.id] = []

        user_markup = markup.RemoveSong(database, 'lyrics')

        database.ChangeCondition(user.id, 'removelyrics_choose')

        bot.send_message(user.id, constants._removelyrics['choice'], reply_markup = user_markup)



@bot.message_handler(commands = ['adminlist'])

def handle_adminlist(message):

    user = database.User(message.from_user.id)

    global admin_list

    if user.admin:

        admin_list = database.AdminList()

        answer = admin_list[0]

        bot.send_message(user.id, answer)



@bot.message_handler(commands = ['addadmin'])

def handle_addadmin(message):

    user = database.User(message.from_user.id)

    if user.creator:

        key = functions.GetKey()

        database.AddToTable('adminkeys', [key])

        bot.send_message(user.id, constants._addadmin['key'].format(key = str(key)))



@bot.message_handler(commands = ['removeadmin'])

def handle_removeadmin(message):

    global admin_list

    admin_list = database.AdminList()

    user = database.User(message.from_user.id)

    if user.creator:

        database.ChangeCondition(user.id, 'removeadmin_who')

        user_markup = markup.Numbers(len(admin_list[1]))

        bot.send_message(user.id, admin_list[0] + constants._removeadmin['removeadmin_who'], reply_markup = user_markup)



@bot.message_handler(commands = ['userslist'])

def handle_userslist(message):

    user = database.User(message.from_user.id)

    if user.creator:

        answer = database.UserList()

        bot.send_message(user.id, answer)



@bot.message_handler(commands = ['delete'])

def handle_delete(message):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE id =" + str(message.from_user.id))
    bot.send_message(message.from_user.id, "удалил")


@bot.message_handler(content_types = ['text'])

def handle_text(message):

    global add

    global remove_admin

    user = database.User(message.from_user.id)

    if user.condition == 'first_question':

        if message.text == 'Да':

            database.ChangeCondition(user.id, 'input_key')

            bot.send_message(user.id, constants._start['first_question_yes'], reply_markup = hide_markup)

        else:

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._start['first_question_no'], reply_markup = hide_markup)

    elif user.condition == 'input_key':

        if database.CheckKey(message.text):

            database.DeleteKey(message.text)

            if user.admin:

                bot.send_message(user.id, constants._inputkey['already'])

            else:

                database.AddAdmin(user.id)

                bot.send_message(user.id, constants._inputkey['new_admin'])

        else:

            bot.send_message(user.id, constants._inputkey['false'])

        database.ChangeCondition(user.id, 'None')

    elif user.condition == 'lyrics_search':

        if message.text == 'Исполнители':

            database.ChangeCondition(user.id, 'lyrics_search_by_artist')

            user_markup = markup.Artists(database, 'Lyrics')

            bot.send_message(user.id, constants._lyrics['by_artist'], reply_markup = user_markup)

        else:

            artist_song = functions.ArtistSong(message.text)

            lyrics = database.FindSong('Lyrics', artist_song[0], artist_song[1])

            bot.send_message(user.id, lyrics)

    elif user.condition == 'lyrics_search_by_artist':

        database.ChangeCondition(user.id, 'lyrics_search_by_artist_ — ' + message.text)

        user_markup = markup.Artist(database, 'Lyrics', message.text)

        bot.send_message(user.id, constants._lyrics['artist_songs'], reply_markup = user_markup)

    elif functions.ArtistSong(user.condition)[0] == 'lyrics_search_by_artist_':

        if message.text == 'Исполнители':

            database.ChangeCondition(user.id, 'lyrics_search_by_artist')

            user_markup = markup.Artists(database, 'Lyrics')

            bot.send_message(user.id, constants._lyrics['by_artist'], reply_markup = user_markup)

        else:

            lyrics = database.FindSong('Lyrics', functions.ArtistSong(user.condition)[1], message.text)

            bot.send_message(user.id, lyrics)

    elif user.condition == 'answer_requests':

        global requests

        requests = database.Requests()

        user_markup = markup.Numbers(len(requests[1]))

        if message.text == 'Принять запрос':

            database.ChangeCondition(user.id, 'request_allow')

            bot.send_message(user.id, requests[0] + constants._adminrequest['creator_requests_yes'], reply_markup = user_markup)

        elif message.text == 'Отклонить запрос':

            database.ChangeCondition(user.id, 'request_disallow')

            bot.send_message(user.id, requests[0] + constants._adminrequest['creator_requests_no'], reply_markup = user_markup)

    elif user.condition == 'request_allow':

        n = int(message.text)

        id = requests[1][n - 1]

        database.RequestAnswer(id, True)

        bot.send_message(user.id, constants._adminrequest['confirm_creator'])

        bot.send_message(id, constants._adminrequest['confirm_user'])

    elif user.condition == 'request_disallow':

        n = int(message.text)

        id = requests[1][n - 1]

        database.RequestAnswer(id, False)

        bot.send_message(user.id, constants._adminrequest['unconfirm_creator'])

        bot.send_message(id, constants._adminrequest['unconfirm_user'])

    elif user.condition == 'addlyrics_artist':

        database.ChangeCondition(user.id, 'addlyrics_song')

        add[user.id] = [message.text,'','']

        bot.send_message(user.id, constants._addlyrics['song'])

    elif user.condition == 'addlyrics_song':

        database.ChangeCondition(user.id, 'addlyrics_lyrics')

        add[user.id][1] = message.text

        if database.SongExist(add[user.id][0], add[user.id][1], 'lyrics'):

            database.ChangeCondition(user.id, 'addlyrics_exists')

            user_markup = markup.YesNo('Оставить всё как было', 'Да, не годится, давай по новой')

            bot.send_message(user.id, constants._addlyrics['already'].format(lyrics = database.FindSong('lyrics', add[user.id][0], add[user.id][1])), reply_markup = user_markup)

        else:

            bot.send_message(user.id, constants._addlyrics['lyrics'])

    elif user.condition == 'addlyrics_exists':

        if message.text == 'Оставить всё как было':

            database.ChangeCondition(user.id, 'addlyrics_onemore')

            user_markup = markup.YesNo('Не, я всё, выходи', 'Ну давай ещё по одной')

            bot.send_message(user.id, constants._addlyrics['break'], reply_markup = user_markup)

        elif message.text == 'Да, не годится, давай по новой':

            database.ChangeCondition(user.id, 'addlyrics_lyrics')

            bot.send_message(user.id, constants._addlyrics['continue'])

    elif user.condition == 'addlyrics_lyrics':

        database.ChangeCondition(user.id, 'addlyrics_confirm')

        user_markup = markup.Confirm()

        add[user.id][2] = message.text

        bot.send_message(user.id, constants._addlyrics['confirm'].format(lyrics = add[user.id][2]), reply_markup = user_markup)

    elif user.condition == 'addlyrics_confirm':

        if message.text == '#Подтвердить':

            if database.SongExist(add[user.id][0], add[user.id][1], 'lyrics'):

                database.ChangeSong('lyrics', add[user.id][0], add[user.id][1], add[user.id][2])

            else:

                database.AddToTable('lyrics', add[user.id])

            database.ChangeCondition(user.id, 'addlyrics_onemore')

            user_markup = markup.YesNo('Не, я всё, выходи', 'Ну давай ещё по одной')

            bot.send_message(user.id, constants._addlyrics['add'], reply_markup = user_markup)

        elif message.text == 'Ввести заново':

            database.ChangeCondition(user.id, 'addlyrics_artist')

            bot.send_message(user.id, constants._addlyrics['restart'], reply_markup = hide_markup)

        elif message.text == 'Выйти':

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._addlyrics['exit'], reply_markup = hide_markup)

    elif user.condition == 'addlyrics_onemore':

        if message.text == 'Ну давай ещё по одной':

            database.ChangeCondition(user.id, 'addlyrics_artist')

            bot.send_message(user.id, constants._addlyrics['onemore'], reply_markup = hide_markup)

        elif message.text == 'Не, я всё, выходи':

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._addlyrics['exit'], reply_markup = hide_markup)

    elif user.condition == 'removelyrics_choose':

        if message.text == 'Всё, выбрал':

            database.ChangeCondition(user.id, 'removelyrics_confirm')

            user_markup = markup.Confirm()

            answer = constants._removelyrics['confirm']

            for song in remove[user.id]:

                answer += '\n' + song[0] + ' — ' + song[1]

            bot.send_message(user.id, answer, reply_markup = user_markup)

        else:

            artist_song = functions.ArtistSong(message.text)

            remove[user.id].append((artist_song[0], artist_song[1]))

            bot.send_message(user.id, constants._removelyrics['onemore'])

    elif user.condition == 'removelyrics_confirm':

        if message.text == '#Подтвердить':

            for song in remove[user.id]:

                database.RemoveSong('lyrics', song[0], song[1])

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._removelyrics['exit'], reply_markup = hide_markup)

        elif message.text == 'Ввести заново':

            database.ChangeCondition(user.id, 'removelyrics_choose')

            remove[user.id] = []

            user_markup = markup.RemoveSong(database, 'lyrics')

            bot.send_message(user.id, constants._removelyrics['restart'], reply_markup = user_markup)

        elif message.text == 'Выйти':

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._removelyrics['exit'], reply_markup = hide_markup)

    elif user.condition == 'removeadmin_who':

        n = int(message.text)

        remove_admin = admin_list[1][n - 1]

        database.ChangeCondition(user.id, 'removeadmin_confirm')

        user_markup = markup.ConfirmRemoveAdmin()

        bot.send_message(user.id, constants._removeadmin['removeadmin_confirm'].format(n = n), reply_markup = user_markup)

    elif user.condition == 'removeadmin_confirm':

        if message.text == 'Баааааннннннн':

            database.ChangeCondition(user.id, 'None')

            database.RemoveAdmin(remove_admin)

            bot.send_message(user.id, constants._removeadmin['exit'], reply_markup = hide_markup)

        elif message.text == 'Выбрать заново':

            database.ChangeCondition(user.id, 'removeadmin_who')

            user_markup = markup.Numbers(len(admin_list[1]))

            bot.send_message(user.id, constants._removelyrics['restart'], reply_markup = user_markup)

        elif message.text == 'Выйти':

            database.ChangeCondition(user.id, 'None')

            bot.send_message(user.id, constants._removelyrics['exit'], reply_markup = hide_markup)




















bot.polling(none_stop = True, interval = 0)
