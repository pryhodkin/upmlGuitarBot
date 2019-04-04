import psycopg2
import telebot
import random


class Database:

    def __init__(self, connection):

        self.connection = connection

        cursor = connection.cursor()

        cursor.execute("""
        
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema NOT IN ('information_schema','pg_catalog');
                
                """)
        tables = []

        for table in cursor:

            tables.append(table[0])

        cursor.close()

        self.tables = tables

    def ToStringValue(self, list):

        result = ''

        i = 0

        while i < len(list):

            if type(list[i]) == type(str(list[i])):

                list[i] = self.ToSQLString(str(list[i]))

                result += "'" + str(list[i]) + "'"

            elif list[i] == None:

                result += 'None'

            else:

                result += str(list[i])

            if i != len(list) - 1:

                result += ','

            i += 1

        return result

    def ToStringColumns(self, list):

        result = ''

        i = 0

        while i < len(list):

            result += str(list[i])

            if i != len(list) - 1:

                result += ','

            i += 1

        return result

    def ToSQLString(self, string):

        result = ''

        i = 0

        while i < len(string):

            if string[i] == "'":

                result += "'"

            result += string[i]

            i += 1

        return result

    def CleanTable(self, table):

        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM {0};".format(table))

        self.connection.commit()

        cursor.close()

    def ColumnsList(self, table):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT column_name
                FROM information_schema.columns
                WHERE information_schema.columns.table_name='{0}';

        """.format(table))

        columns = []

        for column in cursor:

            columns.append(column[0])

        cursor.close()

        return columns

    def AddToTable(self, table, row):

        cursor = self.connection.cursor()

        columns = self.ToStringColumns(self.ColumnsList(table))

        row = self.ToStringValue(row)

        cursor.execute("""

            INSERT INTO {table}({columns})
            VALUES({row});

            """.format(table=table, columns=columns, row=row))

        self.connection.commit()

        cursor.close()

    def DeleteFromTable(self, table, id):

        cursor = self.connection.cursor()

        cursor.execute("""

                DELETE FROM {table}
                WHERE Id = {id};

        """.format(table=table, id=id))

        self.connection.commit()

        cursor.close()

    def ToListCursor(self, cursor):

        result = []

        for row in cursor:

            result.append(row)

        return result

    def CheckExistUser(self, id):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT id
                FROM Users
                WHERE id = {id};

        """.format(id=id))

        n = 0

        for row in cursor:

            n += 1

        cursor.close()

        if n == 0:

            return False

        else:

            return True

    def User(self, id):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                SELECT id, First_Name, Last_Name, Username, Admin, Creator, Condition
                FROM users
                WHERE id = {id};
        
        """.format(id = id))

        user = self.ToListCursor(cursor)

        cursor.close()

        result = User(user[0][0], user[0][1], user[0][2], user[0][3], user[0][6], user[0][4], user[0][5])

        return result

    def ChangeCondition(self, id, condition):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                UPDATE users
                SET condition = '{condition}'
                WHERE id = {id};
        
        """.format(condition = condition, id = id))

        self.connection.commit()

        cursor.close()

    def CheckKey(self, key):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                SELECT *
                FROM adminkeys;
        
        """)

        for row in cursor:

            if str(row[0]) == key:

                cursor.close()

                return True

        cursor.close()

        return False

    def DeleteKey(self, key):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                DELETE FROM adminkeys
                WHERE key = {key};
        
        """.format(key = key))

        self.connection.commit()

        cursor.close()

    def AddAdmin(self, id):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                UPDATE users
                SET Admin = TRUE
                WHERE id = {id};
        
        """.format(id = id))

        self.connection.commit()

        cursor.close()

    def FindSong(self, table, artist, song):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                SELECT *
                FROM {table}
                WHERE artist = '{artist}' AND song = '{song}';
        
        """.format(table = table, artist = artist, song = song))

        song_list = self.ToListCursor(cursor)

        return song_list[0][2]

    def SongExist(self, artist, song, table):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT *
                FROM {table}
                WHERE artist = '{artist}' AND song = '{song}';

        """.format(table = table, artist = artist, song = song))

        for row in cursor:

            return True

        cursor.close()

        return False

    def RequestsNumber(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                SELECT count(*)
                FROM adminrequests
                WHERE answered = False;
                
        """)

        result = self.ToListCursor(cursor)[0][0]

        cursor.close()

        return result

    def RequestExist(self, id):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                SELECT *
                FROM adminrequests
                WHERE id = {id};
        
        """.format(id = id))

        if len(self.ToListCursor(cursor)) == 0:

            cursor.close()

            return False

        else:

            cursor.close()

            return True
        
    def Requests(self):
        
        cursor = self.connection.cursor()
        
        cursor.execute("""
        
                SELECT *
                FROM users
                WHERE id IN (SELECT id FROM adminrequests WHERE answered = False)
        
        """)
        
        result = [ '', [] ]

        users_list = self.ToListCursor(cursor)

        cursor.close()

        users = []

        for user in users_list:

            users.append(self.User(user[0]))

        n = 0

        for user in users:

            n += 1

            result[0] +=  "#Номер: {n}\n"\
                       "#Имя: {first_name}\n"\
                       "#Фамилия: {last_name}\n"\
                       "#Username: {username}\n"\
                       "#Id: {id}\n\n".format(n = n, first_name = user.first_name, last_name = user.last_name, username = user.username, id = user.id)

            result[1].append(user.id)

        return result

    def RequestAnswer(self, id, answer):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT *
                FROM adminrequests
                WHERE answered = False AND id = {id};

        """.format(id = id))

        requests = self.ToListCursor(cursor)

        for row in requests:

            cursor.execute("""
                
                    UPDATE adminrequests
                    SET answered = True, answer = {answer}
                    WHERE id = {id};
                
            """.format(answer = answer, id = row[0]))

            if answer:

                self.AddAdmin(row[0])

        self.connection.commit()

        cursor.close()

    def ChangeSong(self, table, artist, song, content):

        cursor = self.connection.cursor()

        artist = self.ToSQLString(artist)
        song = self.ToSQLString(song)
        content = self.ToSQLString(content)

        cursor.execute("""
        
                UPDATE {table}
                SET {table} = '{content}'
                WHERE artist = '{artist}' AND song = '{song}';
        
        """.format(table = table, artist = artist, song = song, content = content))

        self.connection.commit()

        cursor.close()

    def RemoveSong(self, table, artist, song):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                DELETE FROM {table}
                WHERE artist = '{artist}' AND song = '{song}';
        
        """.format(table = table, artist = artist, song = song))

        self.connection.commit()

        cursor.close()

    def AdminList(self):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT id
                FROM users
                WHERE admin = True

        """)

        result = ['', []]

        users_list = self.ToListCursor(cursor)

        cursor.close()

        users = []

        for user in users_list:

            users.append(self.User(user[0]))

        n = 0

        for user in users:

            n += 1

            result[0] += "#Номер: {n}\n" \
                         "#Имя: {first_name}\n" \
                         "#Фамилия: {last_name}\n" \
                         "#Username: {username}\n" \
                         "#Id: {id}\n\n".format(n=n, first_name=user.first_name, last_name=user.last_name,
                                                username=user.username, id=user.id)

            result[1].append(user.id)

        return result

    def UserList(self):

        cursor = self.connection.cursor()

        cursor.execute("""

                SELECT id
                FROM users

        """)

        result = ''

        users_list = self.ToListCursor(cursor)

        cursor.close()

        users = []

        for user in users_list:

            users.append(self.User(user[0]))

        for user in users:

            result +=    "#Имя: {first_name}\n" \
                         "#Фамилия: {last_name}\n" \
                         "#Username: {username}\n" \
                         "#Id: {id}\n\n".format(first_name = user.first_name, last_name = user.last_name,
                                                username = user.username, id = user.id)

        return result

    def RemoveAdmin(self, id):

        cursor = self.connection.cursor()

        cursor.execute("""
        
                UPDATE users
                SET admin = False
                WHERE id = {id};
        
        """.format(id = id))

        self.connection.commit()

        cursor.close()






class Markup:

    def __init__(self):

        pass

    def Songs(self, database, table):

        markup = telebot.types.ReplyKeyboardMarkup(True, False)

        cursor = database.connection.cursor()

        cursor.execute("""

                SELECT DISTINCT Artist, Song
                FROM {table}
                ORDER BY Song, Artist;

        """.format(table=table))

        songs_list = database.ToListCursor(cursor)

        cursor.close()

        markup.row('Исполнители', '/close')

        for row in songs_list:

            markup.row(row[0] + ' — ' + row[1])

        return markup

    def Artists(self, database, table):

        markup = telebot.types.ReplyKeyboardMarkup(True, False)

        cursor = database.connection.cursor()

        cursor.execute("""

                SELECT DISTINCT Artist
                FROM {table}
                ORDER BY Artist;

        """.format(table=table))

        artists_list = database.ToListCursor(cursor)

        markup.row('/close')

        for row in artists_list:
            markup.row(row[0])

        cursor.close()

        return markup

    def Artist(self, database, table, artist):

        markup = telebot.types.ReplyKeyboardMarkup(True, True)

        cursor = database.connection.cursor()

        cursor.execute("""

                SELECT DISTINCT Song FROM {table}
                WHERE Artist = '{artist}'
                ORDER BY Song;

        """.format(table=table, artist=artist))

        i = 0

        markup.row('Исполнители', '/close')

        artist_list = database.ToListCursor(cursor)

        while i < len(artist_list):

            if i + 1 < len(artist_list):

                markup.row(artist_list[i][0], artist_list[i + 1][0])

            else:

                markup.row(artist_list[i][0])

            i += 2

        return markup

    def Confirm(self):

        markup = telebot.types.ReplyKeyboardMarkup(True, False)

        markup.row('Выйти')

        markup.row('Ввести заново', '#Подтвердить')

        return markup

    def Users(self, database):

        markup = telebot.types.ReplyKeyboardMarkup(True, True)

        cursor = database.connection.cursor()

        cursor.execute("""

                SELECT id, First_Name, Last_Name, Username, Admin
                FROM Users

        """)

        users_list = database.ToListCursor(cursor)

        for row in users_list:
            markup.row("#Имя: {first_name}\n"
                       "#Фамилия: {last_name}\n"
                       "#Username: {username}\n"
                       "#Id: {id}\n".format(first_name=row[1], last_name=row[2], username=row[3], id=row[0]))

        cursor.close()

        return markup

    def YesNo(self, No, Yes):

        markup = telebot.types.ReplyKeyboardMarkup(True, True)

        markup.row(No, Yes)

        return markup

    def AdminRequest(self, id):

        markup = telebot.types.ReplyKeyboardMarkup()

        markup.row('{id} — быть админом', '{id} — недостоен')

    def AdminRequests(self, database):

        markup = telebot.types.ReplyKeyboardMarkup()

        cursor = database.connection.cursor()

        cursor.execute("""
        
                SELECT *
                FROM users
                WHERE id IN (SELECT id FROM adminrequests WHERE answered = False)
        
        """)

        users_list = database.ToListCursor(cursor)

        cursor.close()

        users = []

        for user in users_list:

            users.append(database.User(user[0]))

        for user in users:

            markup.row("#Имя: {first_name}\n"
                       "#Фамилия: {last_name}\n"
                       "#Username: {username}\n"
                       "#Id: {id}\n".format(first_name=user.first_name, last_name=user.last_name, username=user.username, id=user.id))


        return markup

    def RequestAnswer(self):

        markup = telebot.types.ReplyKeyboardMarkup(True, True)

        markup.row('Принять запрос','Отклонить запрос')

        return markup

    def Numbers(self, n):

        markup = telebot.types.ReplyKeyboardMarkup(True)

        i = 1

        while i <= n:

            if i + 2 <= n:

                markup.row(str(i), str(i + 1), str(i + 2))

            elif i + 1 <= n:

                markup.row(str(i), str(i + 1))

            else:

                markup.row(str(i))

            i += 3

        return markup

    def RemoveSong(self, database, table):

        markup = telebot.types.ReplyKeyboardMarkup(True, False)

        cursor = database.connection.cursor()

        cursor.execute("""

                SELECT DISTINCT Artist, Song
                FROM {table}
                ORDER BY Song, Artist;

        """.format(table=table))

        songs_list = database.ToListCursor(cursor)

        cursor.close()

        markup.row('Всё, выбрал')

        for row in songs_list:

            markup.row(row[0] + ' — ' + row[1])

        return markup

    def ConfirmRemoveAdmin(self):

        markup = telebot.types.ReplyKeyboardMarkup(True, True)

        markup.row('Выйти')

        markup.row('Выбрать заново', 'Баааааннннннн')

        return markup




class User:

    def __init__(self, id, first_name, last_name, username, condition, admin = False, creator = False):

        self.username = username
        self.first_name = first_name
        self.last_name= last_name
        self.id = id
        self.condition = condition
        self.admin = admin
        self.creator = creator



def GetKey():

    return round(random.random(), 15)


def ArtistSong(text):

    def Substring(str, i, n):

        substring = ''

        j = 0

        while j + i < n and j + i < len(str):

            substring += str[j + i]

            j += 1

        return substring

    i = 0

    sub = ['', '']

    while i < len(text) and text[i] != '—':

        i += 1

    sub[0] = Substring(text, 0, i - 1)

    sub[1] = Substring(text, i + 2, len(text))

    return sub