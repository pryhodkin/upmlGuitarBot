import array
import telebot
import functions

token = "643099655:AAGu_a3CK89pYH1SWmZzHJeg2BJExho17FY"

music_array = [['author', 'song', 'lyrics'],



['The White Stripes', 'Seven nation army',
"""I'm gonna fight 'em all
A seven nation army couldn't hold me back
They're gonna rip it off
Taking their time right behind my back

And I'm talking to myself at night
Because I can't forget
Back and forth through my mind
Behind a cigarette
And the message coming from my eyes
Says leave it alone

Don't want to hear about it
Every single one's got a story to tell
Everyone knows about it
From the Queen of England to the hounds of hell

And if I catch it coming back my way
I'm gonna serve it to you
And that ain't what you want to hear
But that's what I'll do
And the feeling coming from my bones
Says find a home

I'm going to Wichita
Far from this opera for evermore
I'm gonna work the straw
Make the sweat drip out of every pore
And I'm bleeding, and I'm bleeding, and I'm bleeding
Right before the lord
All the words are gonna bleed from me
And I will sing no more
And the stains coming from my blood
Tell me go back home"""],



['The White Stripes', 'Little Cream Soda',
""" One, two, three, four

Well, every highway that I go down seems to be longer
Than the last one that I knew about, oh, well
And every girl that I walk around seems to be more of an illusion
Than the last one that I found, oh, well

And this old man in front of me wearing canes and ruby rings
Is like containing an explosion when he sings
And with every chance to set himself on fire
He just ends up doin' the same thing

Well, each beautiful thing I come across tells me
To stop moving and shake this riddle off, oh, well
And there was a time when all I wanted was my ice cream colder
And a little cream soda, oh, well, oh, well

And a wooden box and an alley full
of rocks was all I had to care about
Oh, well, oh, well, oh, well
Now my mind is filled with rubber tires and forest fires

And whether I'm a liar
And lots of other situations where I don't know what to do
At which time God screams to me
"There's nothing left for me to tell you."

Nothing left for me to tell you
Nothing left
Oh, well, oh, well, oh, well, oh, well
Oh, well, oh, well, oh, well, oh, well"""],



["Imagine Dragons", "Radioactive",
"""Whoa, oh, oh
Whoa, oh, oh
Whoa, oh, oh
Whoa

I'm waking up to ash and dust
I wipe my brow and I sweat my rust
I'm breathing in the chemicals

I'm breaking in, shaping up, then checking out on the prison bus
This is it, the apocalypse
Whoa

I'm waking up, I feel it in my bones
Enough to make my systems blow
Welcome to the new age, to the new age
Welcome to the new age, to the new age

Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive
Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive

I raise my flags, don my clothes
It's a revolution, I suppose
We'll paint it red to fit right in
Whoa

I'm breaking in, shaping up, then checking out on the prison bus
This is it, the apocalypse
Whoa

I'm waking up, I feel it in my bones
Enough to make my systems blow
Welcome to the new age, to the new age
Welcome to the new age, to the new age

Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive
Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive

All systems go, the sun hasn't died
Deep in my bones, straight from inside

I'm waking up, I feel it in my bones
Enough to make my systems blow
Welcome to the new age, to the new age
Welcome to the new age, to the new age

Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive
Whoa, oh, oh, oh, oh, whoa, oh, oh, oh, I'm radioactive, radioactive"""],



["Green Day", "Boulevard of broken dreams",
 """I walk a lonely road
 The only one that I have ever known
 Don't know where it goes
 But it's only me, and I walk alone
 
 I walk this empty street
 On the boulevard of broken dreams
 Where the city sleeps
 And I'm the only one, and I walk alone
 
 I walk alone, I walk alone
 I walk alone and I walk a
 
 My shadow's the only one that walks beside me
 My shallow heart's the only thing that's beating
 Sometimes I wish someone out there will find me
 Till then I walk alone
 
 Ah ah ah ah ah
 Ah ah ah ah ah
 
 I'm walking down the line
 That divides me somewhere in my mind
 On the border line of the edge
 And where I walk alone
 
 Read between the lines
 What's fucked up and every thing's all right
 Check my vital signs to know I'm still alive
 And I walk alone
 
 I walk alone, I walk alone
 I walk alone and I walk a
 
 My shadow's the only one that walks beside me
 My shallow heart's the only thing that's beating
 Sometimes I wish someone out there will find me
 Till then I walk alone
 
 Ah ah ah ah ah
 Ah ah ah ah ah
 I walk alone, I walk a
 
 I walk this empty street
 On the boulevard of broken dreams
 Where the city sleeps
 And I'm the only one, and I walk alone
 
 My shadow's the only one that walks beside me
 My shallow heart's the only thing that's beating
 Sometimes I wish someone out there will find me
 Till then I walk alone"""],




["Жуки","Батарейка",
 """Холодный ветер с дождём усилился стократно
Все говорит об одном, что нет пути обратно
Что ты не мой лопушок, а я не твой Андрейка
Что у любви у нашей села батарейка

О-оу-и-я-и-ё! Батарейка!
О-оу-и-я-и-ё! Батарейка!

Я тосковал по тебе в минуты расставания
Ты возвращалась ко мне сквозь сны и расстояния
Но несмотря ни на что, пришла судьба-злодейка
И у любви у нашей села батарейка

О-оу-и-я-и-ё! Батарейка!
О-оу-и-я-и-ё! Батарейка!

И вроде все как всегда: все те же чашки-ложки
Все та же в кране вода, все тот же стул без ножки
И все о том же с утра щебечет канарейка
Лишь у любви у нашей села батарейка

О-оу-и-я-и-ё! Батарейка!
О-оу-и-я-и-ё! Батарейка!"""],



["ДДТ","Что такое осень",
"""Что такое осень - это небо.
Плачущее небо под ногами.
В лужах разлетаются птицы с облаками.
Осень - я давно с тобою не был.
В лужах разлетаются птицы с облаками.
Осень - я давно с тобою не был.

refrain:
Осень, в небе жгут корабли.
Осень, мне бы прочь от земли.
Там, где в море тонет печаль
Осень темная даль.

Что такое осень - это камни.
Верность над чернеющей Невою.
Осень вновь напомнила душе о самом главном,
Осень, я опять лишен покоя.
Осень вновь напомнила душе о самом главном,
Осень, я опять лишен покоя.

refrain

Что такое осень - это ветер.
Вновь играет рваными цепями.
Осень - доползем ли, долетим ли до ответа:
Что же будет с родиной и с нами?
Осень - доползем ли, долетим ли до рассвета,
Осень, что же будет с завтра с нами?

refrain (2x)

Тает стаей город во мгле,
Осень, что я знал о тебе?
Сколько будет рваться листва,
Осень вечно права."""],



["Сплин","Выхода нет",
"""Сколько лет прошло, всё о том же гудят провода
Всё того же ждут самолёты
Девочка с глазами из самого синего льда
Тает под огнём пулемёта
Должен же растаять хоть кто-то

Скоро рассвет, выхода нет
Ключ поверни и полетели
Нужно писать в чью-то тетрадь
Кровью, как в метрополитене
Выхода нет, выхода нет

Где-то мы расстались, не помню в каких городах
Словно это было в похмелье
Через мои песни идут и идут поезда
Исчезая в тёмном тоннеле
Лишь бы мы проснулись в одной постели

Скоро рассвет, выхода нет
Ключ поверни и полетели
Нужно писать в чью-то тетрадь
Кровью, как в метрополитене
Выхода нет, выхода нет

Сколько лет пройдёт, всё о том же гудеть проводам
Всё того же ждать самолётам
Девочка с глазами из самого синего льда
Тает под огнём пулемёта
Лишь бы мы проснулись с тобой в одной постели

Скоро рассвет, выхода нет
Ключ поверни и полетели
Нужно писать в чью-то тетрадь
Кровью, как в метрополитене
Выхода нет, выхода нет
Выхода нет, выхода нет"""],



["Сплин","Моё сердце","""Мы не знали друг друга до этого лета
Мы болтались по свету в земле и воде
И совершенно случайно мы взяли билеты
Hа соседние кресла на большой высоте

И моё сердце остановилось
Моё сердце замерло
Моё сердце остановилось
Моё сердце замерло

И ровно тысячу лет мы просыпаемся вместе
Даже если уснули в разных местах
Мы идём ставить кофе под Элвиса Пресли
Кофе сбежал под Propellerheads, ах

И моё сердце остановилось
Моё сердце замерло
Моё сердце остановилось
Моё сердце замерло

И может быть ты не стала звездой в Голливуде
Hе выходишь на подиум в нижнем белье
У тебя не берут автографы люди
И поёшь ты чуть тише, чем Монсеррат Кабалье

Hу так и я, слава Богу, ни Рикки ни Мартин
Hе выдвигался на Оскар, французам не забивал
Моим именем не назван город на карте
Hо задёрнуты шторы и разложен диван

И моё сердце остановилось
Моё сердце замерло
Моё сердце остановилось
Моё сердце замерло

Я наяву вижу то, что многим даже не снилось
Hе являлось под кайфом, не стучалось в стекло
Моё сердце остановилось, отдышалось немного
И снова пошло

Моё сердце остановилось
Моё сердце замерло
Моё сердце остановилось
Моё сердце замерло

И моё сердце ¡Hasta la vista!
Моё сердце замерло
И моё сердце остановилось
Моё сердце замерло"""],



["Люмен","А мы не ангелы, парень",
 """Ты открывал ночь
Все что могли позволить 
Маски срывал прочь
Душу держал в неволе.
Пусть на щеке кровь
Ты свалишь на помаду.
Черту барьер слов.
Ангелу слов не надо.

Припев:
А мы не ангелы, парень!
Нет, мы не ангелы.
Темные твари, и сорваны планки нам.
Если нас спросят
Чего мы хотели бы?
Мы бы взлетели
Мы бы взлетели...
Мы не ангелы парень!
Нет, мы не ангелы.

Там на пожаре
Утратили ранги мы.
Нету к таким
Ни любви ни доверия.
Люди глядят
на наличие перьев.
Мы не ангелы парень!

Сотни чужих крыш
Что ты искал там парень?
Ты так давно спишь..
Слишком давно для твари.
Может пора вниз?
Там где ты дышишь телом.
Брось свой пустой лист.
Твари не ходят в белом.

Припев."""],



["Океан Ельзи","Обійми",
 """Коли настане день,
Закінчиться війна,
Там загубив себе,
Побачив аж до дна.

Приспів:
Обійми мене, обійми мене, обійми
Так лагідно і не пускай.
Обійми мене, обійми мене, обійми
Твоя весна прийде нехай.

І от моя душа
Складає зброю вниз,
Невже таки вона
Так хоче теплих сліз?

Приспів

Обійми... Обійми мене.

Приспів:
Обійми мене, обійми мене, обійми
І більше так не відпускай.
Обійми мене, обійми мене, обійми
Твоя весна прийде нехай."""],



["Виктор Цой","Когда твоя девушка больна",
 """День как день
Только ты почему-то грустишь
И вокруг все поют
Только ты один молчишь
Потерял аппетит
И не хочешь сходить в кино
Ты идешь в магазин
Чтобы купить вино

Солнце светит, и растет трава
Но тебе она не нужна
Все не так, и все не то
Когда твоя девушка больна
Когда больна...

Ты идешь в магазин
Головою поник
Как будто иссяк
Чистый горный родник
Она где-то лежит
Ест мед и пьет аспирин
И вот ты идешь
На вечеринку один

Солнце светит, и растет трава
Но тебе она не нужна
Все не так, и все не то
Когда твоя девушка больна
На вечеринку один
Когда твоя девушка больна
"""],



["Виктор Цой","Кукушка",
 """Песен ещё не написанных сколько?
Скажи кукушка, пропой
В городе мне жить или на выселках?
Камнем лежать, или гореть звездой? Звездой?

Солнце моё, взгляни на меня
Моя ладонь превратилась в кулак
И если есть порох, дай огня!
Вот так!

Кто пойдёт по следу одинокому
Сильные да смелые головы сложили в поле, в бою
Мало кто остался в светлой памяти
В трезвом уме, да с твёрдой рукой в строю, в строю

Солнце моё, взгляни на меня
Моя ладонь превратилась в кулак
И если есть порох, дай огня!
Вот так!

Где же ты теперь, воля вольная?
С кем же ты сейчас ласковый рассвет встречаешь? Ответь!
Хорошо с тобой, но плохо без тебя
Голову на плечи, терпеливые под плеть, под плеть

Ты, солнце моё, взгляни на меня
Моя ладонь превратилась в кулак
И если есть порох, дай огня!
Вот так!"""],



["Виктор Цой","Перемен",
 """Вместо тепла - зелень стекла
Вместо огня - дым
Из сетки календаря выхвачен день

Красное солнце сгорает дотла
День догорает с ним
На пылающий город падает тень

Перемен!
Требуют наши сердца
Перемен!
Требуют наши глаза

В нашем смехе и в наших слезах и в пульсации вен
Перемен!
Мы ждём перемен!

Электрический свет продолжает наш день
И коробка от спичек пуста
Но на кухне синим цветком горит газ

Сигареты в руках, чай на столе
Эта схема проста
И больше нет ничего
Всё находится в нас

Перемен!
Требуют наши сердца
Перемен!
Требуют наши глаза

В нашем смехе и в наших слезах и в пульсации вен
Перемен!
Мы ждём перемен!

Мы не можем похвастаться мудростью глаз
И умелыми жестами рук
Нам не нужно всё это, чтобы друг друга понять

Сигареты в руках, чай на столе
Так замыкается круг
И вдруг нам становится страшно что-то менять

Перемен! - требуют наши сердца
Перемен! - требуют наши глаза

В нашем смехе и в наших слезах и в пульсации вен
Перемен!
Мы ждём перемен!

Перемен!
Требуют наши сердца
Перемен!
Требуют наши глаза

В нашем смехе и в наших слезах и в пульсации вен
Перемен!
Мы ждём перемен!"""],



["Виктор Цой","Звезда по имени Солнце",
 """Белый снег, серый лед
На растрескавшейся земле
Одеялом лоскутным на ней
Город в дорожной петле

А над городом плывут облака
Закрывая небесный свет
А над городом желтый дым
Городу две тысячи лет
Прожитых под светом звезды по имени Солнце

И две тысячи лет война -
Война без особых причин
Война - дело молодых
Лекарство против морщин

Красная-красная кровь
Через час уже просто земля
Через два на ней цветы и трава
Через три она снова жива
И согрета лучами звезды по имени Солнце

И мы знаем, что так было всегда
Что судьбою был больше любим, -
Кто живет по законам другим
И кому умирать молодым

Он не помнит слова "Да" и слова "Нет"
Он не помнит ни чинов ни имен
И способен дотянуться до звезд
Не считая что это сон
И упасть опаленный звездой по имени Солнце"""],



["5'nizza","Солдат",
 """[Интро]
У-е
У-е
У-е

[Куплет 1]
Я солдат
Я не спал пять лет и у меня под глазами мешки
Я сам не видел, но мне так сказали
Я солдат
И у меня нет башки
Мне отбили её сапогами
Ё-ё-ё комбат орёт
Разорванный рот у комбата
Потому что граната
Белая вата, красная вата
Hе лечит солдата

[Припев]
Я солдат
Недоношенный ребёнок войны
Я солдат
Мама залечи мои раны
Я солдат
Солдат забытой Богом страны
Я герой
Скажите мне, какого романа

[Проигрыш]
О-о-о-о-о-о-о
У-е
У-е-е
О-о-о-о-о-о-о

[Куплет 2]
Я солдат
Мне обидно, когда остаётся один патрон
Только я или он
Последний вагон
Самогон
Нас таких миллион
В ОООН
Я солдат
И я знаю своё дело
Моё дело - стрелять
Чтобы пуля попала
В тело врага
Это рагга для тебя мама - война, теперь ты довольна

[Припев]
Я солдат
Недоношенный ребёнок войны
Я солдат
Мама залечи мои раны
Я солдат
Солдат забытой Богом страны
Я герой
Скажите мне, какого романа

[Проигрыш]
О-о-о-о-о-о-о
У-е
У-е-е
О-о-о-о-о-о-о

[Бридж]
I'm a soldier
I'm a soldier
I'm a soldier
I'm a soldier
I'm a soldier
Soldier
Soldier
I'm a soldier
I'm a soldier
I'm a soldier
I'm a soldier
I'm a soldier
Soldier
Soldier

[Припев]
Я солдат
Недоношенный ребёнок войны
Я солдат
Мама залечи мои раны
Я солдат
Солдат забытой Богом страны
Я герой
Скажите мне, какого романа

[Проигрыш]
О-о-о-о-о-о-о
У-е
У-е-е
О-о-о-о-о-о-о"""],



["Гражданская Оборона","Всё идет по плану",
 """Границы ключ переломлен пополам
А наш батюшка Ленин совсем усоп
Он разложился на плесень и на липовый мёд
А перестройка всё идёт и идёт по плану
И вся грязь превратилась в серый лед
И всё идет по плану
И всё идет по плану

А моя судьба захотела на покой
Я обещал ей не участвовать в военной игре
Но на фуражке на моей серп и молот, и звезда
Как это трогательно: серп и молот, и звезда
Лихой фонарь ожидания мотается
И всё идет по плану
И всё идет по плану

А моей женой накормили толпу
Мировым кулаком растоптали ей грудь
Всенародной свободой растерзали ей плоть
Так закопайте её во Христе
Ведь всё идёт по плану

Ведь всё идёт по плану

Ведь один дедушка Ленин хороший был вождь
А все другие остальные такое дерьмо
А все другие враги и такие дураки
Над родною над отчизной бесноватый снег шел
Я купил журнал "Корея", там тоже хорошо
Там товарищ Ким Ир Сен, там тоже, что у нас
Я уверен, что у них то же самое
И всё идёт по плану
И всё идёт по плану

А при коммунизме всё будет заебись
Он наступит скоро, нужно только подождать
Там всё будет бесплатно, там все будет в кайф
Там, наверное, вообще не надо будет умирать
Я проснулся среди ночи и понял
Что всё идёт по плану
Что всё идёт по плану"""],



["Народ","Дед Максим",
 """Вот и помер дед Максим
Да и хуй остался с ним
Положили его в гроб
Хуй уперся в потолок

Он здоровенный был мужик
Он на хую вертел шашлык
Хуем грядки он капал
Хуем грядки поливал

А соседку тетю Зину
Он ебал через корзину
А соседа дядю Гришу
Хуем кинул через крышу

А в гражданскую войну
Он спас дивизию одну
Немцы наших окружили
Немцы наших перебили

А дед ширинку расстегнул
И хуй над речкой протянул
Наши по хую пошли
Наши наших пронесли

А за ними немцы вспять
Стали на хуй наступать
Дед залупой колыхнул
Намцев в реку окунул

А тех, кто плавал по воде
Он бил залупой по голове
После боя генерал
Ему залупу целовал

Едет поезд на ВАИ
В нем сидят одни хуи
Молчите бляди я святой
Я святой!"""],



["Виктор Цой","Группа крови",
 """Тёплое место
На улице ждут отпечатков наших ног
Звёздная пыль на сапогах
Мягкое кресло клетчатый плед
Не нажатый вовремя курок
Солнечный день в ослепительных снах

Группа крови на рукаве
Мой порядковый номер на рукаве
Пожелай мне удачи в бою
Пожелай мне
Не остаться в этой траве

Не остаться в этой траве
Пожелай мне удачи
Пожелай мне удачи

И есть чем платить
Но я не хочу победы любой ценой
Я никому не хочу ставить ногу на грудь
Я хотел бы остаться с тобой
Просто остаться с тобой
Но высокая в небе звезда зовёт меня в путь."""],



["Синяя Птица","Там где клён шумит",
 """Там, где клен шумит над речной волной,
Говорили мы о любви с тобой,
Опустел тот клен, в поле бродит мгла,
А любовь, как сон, стороной прошла.
А любовь, как сон, а любовь, как сон,
А любовь, как сон, стороной прошла.

Сердцу очень жаль, что случилось так,
Гонит осень вдаль журавлей косяк.
Четырем ветрам грусть-печаль раздам,
Не вернется вновь это лето к нам.
Не вернется вновь, не вернётся вновь,
Не вернется вновь это лето к нам.

Ни к чему теперь за тобой ходить,
Ни к чему теперь мне цветы дарить,
Ты любви моей не смогла сберечь,
Поросло травой место наших встреч.
Поросло травой, поросло травой,
Поросло травой место наших встреч."""],



["Валентин Стрыкало","Наше лето",
 """Тихо лужи покрывает лед, помнишь мы с тобою
Целовались ночи напролет под шум прибоя
Это лето не вернуть уже я знаю 
Но когда печаль в моей душе я вспоминаю: 

Припев:
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены.
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены. 

Но расстаться нам с тобой пришлось кончилась путевка
И вагон плацкартный меня нес в Новую Каховку 
Не забуду ночи при луне и твою улыбку
Ты открытку подарила мне, а на той открытке:

Припев:
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены.
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены.

Проигрыш.

Припев:
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены.
Яхта, парус, в это мире только мы одни.
Ялта, август и мы с тобою влюблены."""],



["Любэ","Конь",
 """Выйду ночью в поле с конём,
Ночкой тёмной тихо пойдём.
Мы пойдём с конём,
По полю вдвоём,
Мы пойдём с конём по полю вдвоём(х3)

Ночью в поле звёзд благодать,
В поле никого не видать,
Только мы с конём,
По полю идём(х2)

Сяду я верхом на коня,
Ты неси по полю меня.
По бескрайнему,полю моему(х2)

Дай ка я разок посмотрю,
Где рождает поле зарю.
Ай брусничный свет,алый да рассвет,
Али есть то место,али его нет.(х2)

Полюшко моё,родники.
Дальних деревень огоньки.
Золотая рожь,да кудрявый лён,
Я влюблён в тебя Россия,влюблён.(х2)

Будет добрым год,выбор он
Было всяко,всяко пройдёт.
Пой златая рожь,пой кудрявый лён,
Пой о том как я в Россию влюблён.
Пой златая рожь,пой кудрявый лён,
Мы идём с конём вдвоём!
"""],



["Звери","До скорой встречи",
 """Вчерашний вечер из подворотни на всё согласен
Спасаться нечем и я охотник и я опасен
И очень скоро, ещё минута и доверяю
И мухоморы, конечно круто, но тоже вряд ли

припев:
До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

Тычинка-пестик, любовь научит совсем непошло
Когда мы вместе никто не круче, но это в прошлом
И я не знаю и я теряю вчерашний вечер
Моя смешная, моя сквозная, до скорой встречи

припев:
До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

Моя love story короче ночи, смотрю на время
И беспонтово мотает счётчик такси на север
И я не знаю и я теряю вчерашний вечер
Моя смешная, моя родная, до скорой встречи

припев:
До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи

До скорой встречи
До скорой встречи
Моя любоь к тебе навечно
До скорой встречи
До скорой встречи"""],



["Советские","Постой, паравоз",
 """Постой, паровоз, не стучите, колёса,
Кондуктор, нажми на тормоза.
Я к маменьке родной
С последним приветом
Спешу показаться на глаза.
Я к маменьке родной
С последним приветом
Спешу показаться на глаза.

Не жди меня, мама, хорошего сына.
Твой сын не такой, как был вчера.
Меня засосала
Опасная трясина,
И жизнь моя - вечная игра.

Постой, паровоз, не стучите, колёса.
Есть время взглянуть судьбе в глаза.
Пока ещё не поздно
Нам сделать остановку,
Кондуктор, нажми на тормоза.
Пока ещё не поздно
Нам сделать остановку,
Кондуктор, нажми на тормоза.

Постой, паровоз, не стучите, колёса,
Кондуктор, нажми на тормоза.
Я к маменьке родной
С последним приветом
Спешу показаться на глаза.
Я к маменьке родной
С последним приветом
Спешу показаться на глаза.

Спешу показаться на глаза.

Спешу показаться на глаза."""],



["Сплин","Романс",
 """И лампа не горит и врут календари
И если ты давно хотела что-то мне сказать, то говори
Любой обманчив звук, страшнее тишина
Когда в самый разгар веселья падает из рук бокал вина

И чёрный кабинет, и ждёт в стволе патрон
Так тихо, что я слышу, как идёт на глубине вагон метро
На площади полки, темно в конце строки
И в телефонной трубке эти много лет спустя одни гудки

И где-то хлопнет дверь и дрогнут провода
Привет! Мы будем счастливы теперь
И навсегда
Привет! Мы будем счастливы теперь
И навсегда
"""],



["Ольга Зарубина","На теплоходе музыка играет",
 """Теплоходный гудок разбудил городок
На причале толпится народ
Все волнуются ждут только десять минут
На причале стоит теплоход
На причале стоит теплоход
На теплоходе музыка играет
А я одна стою на берегу
Машу рукой а сердце замирает
И ничего поделать не могу
Ты приехал сюда и казалось тогда
Что ты мне предназначен судьбой
А потом целый год я ждала теплоход
Чтобы вновь повстречаться с тобой
Чтобы вновь повстречаться с тобой
На теплоходе музыка играет
А я одна стою на берегу
Машу рукой а сердце замирает
И ничего поделать не могу
На теплоходе музыка играет
А я одна стою на берегу
Машу рукой а сердце замирает
И ничего поделать не могу
Вот опять теплоход убавляет свой ход
Я того что не сбудется жду
Первый снег в городке первый лед на реке
Я к тебе по нему не дойду
Я к тебе по нему не дойду
На теплоходе музыка играет
А я одна стою на берегу
Машу рукой а сердце замирает
И ничего поделать не могу
На теплоходе музыка играет
А я одна стою на берегу
Машу рукой а сердце замирает
И ничего поделать не могу"""],



["Мираж","Музыка нас связала",
 """Позабудь об этом дне, спор не нужен никому
Не читай нотаций мне, мама, это ни к чему
Снова к друзьям я своим убегаю
Что меня тянет туда, я не знаю
Без музыки мне оставаться надолго нельзя

Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!
Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!

Я забыла все, чему нас учили столько лет
Неужели я сама не найду на все ответ?
Снова к друзьям я своим убегаю
Что меня тянет туда, я не знаю
Без музыки мне оставаться надолго нельзя

Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!
Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!

Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!
Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!

Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!
Музыка нас связала, тайною нашей стала
Всем уговорам твержу я в ответ
Нас не разлучат - нет!
"""],



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]
]

