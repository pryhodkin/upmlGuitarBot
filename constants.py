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



["Сплин","Моё сердце",
"""Мы не знали друг друга до этого лета
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



["The Cranberries","Zombie",
 """Another head hangs lowly
Child is slowly taken
And the violence caused such silence
Who are we mistaken

But you see it's not me
It's not my family
In your head, in your
Head they are fighting
With their tanks and their bombs
And their bombs and their guns
In your head,
In your head they are cryin'

In your head, in your head
Zombie, zombie, zombie
Hey, hey
What's in your head, in your head
Zombie, zombie, zombie
Hey, hey, hey, oh
Dou, dou, dou, dou
Dou, dou, dou, dou
Dou, dou, dou, dou
Dou, dou, dou, dou

Another mother's breakin'
Heart is taking over
When the violence causes silence
We must be mistaken

It's the same old theme since nineteen-sixteen
In your head,
In your head they're still fightin'
With their tanks and their bombs
And their bombs and their guns
In your head, in your head they are dyin'

In your head, in your head
Zombie, zombie, zombie
Hey, hey
What's in your head, in your head
Zombie, zombie, zombie
Hey, hey, hey
Oh, oh, oh, oh, oh, oh, oh
Hey, oh, ya, ya-a"""],



["Jeff Buckley","Hallelujah",
 """Well, I heard there was a secret chord
That David played and it pleased the Lord
But you don't really care for music, do you?
Well it goes like this:
The fourth, the fifth, the minor fall and the major lift
The baffled king composing Hallelujah

Hallelujah, Hallelujah, Hallelujah, Hallelujah...

Well your faith was strong but you needed proof
You saw her bathing on the roof
Her beauty and the moonlight overthrew ya
She tied you to her kitchen chair
She broke your throne and she cut your hair
And from your lips she drew the Hallelujah

Hallelujah, Hallelujah, Hallelujah, Hallelujah...

Well, baby, I've been here before
I've seen this room and I've walked this floor (you know)
I used to live alone before I knew ya
And I've seen your flag on the marble arch
And love is not a victory march
It's a cold and it's a broken Hallelujah

Hallelujah, Hallelujah, Hallelujah, Hallelujah...

Well, there was a time when you let me know
What's really going on below
But now you never show that to me, do ya?
But remember when I moved in you
And the holy dove was moving too
And every breath we drew was Hallelujah

Hallelujah, Hallelujah, Hallelujah, Hallelujah...

Maybe there's a God above
But all I've ever learned from love
Was how to shoot somebody who outdrew ya
And it's not a cry that you hear at night
It's not somebody who's seen the light
It's a cold and it's a broken Hallelujah

Hallelujah, hallelujah, hallelujah, hallelujah...
Hallelujah, hallelujah, hallelujah, hallelujah...
Hallelujah, hallelujah, hallelujah
Hallelujah, hallelujah"""],



["The Beatles","Yesterday",
 """Yesterday all my troubles seemed so far away.
Now it looks as though they're here to stay.
Oh, I believe in yesterday.

Suddenly, I'm not half the man I used to be.
There's a shadow hanging over me.
Oh, yesterday came suddenly.

Why she had to go?
I don't know, she wouldn't say.
I said something wrong.
Now I long for yesterday.

Yesterday love was such an easy game to play.
Now I need a place to hide away.
Oh, I believe in yesterday.

Why she had to go?
I don't know, she wouldn't say.
I said something wrong.
Now I long for yesterday.

Yesterday love was such an easy game to play.
Now I need a place to hide away.
Oh, I believe in yesterday.

Mm mm mm mm mm mm mm."""],



["The Beatles","Hey Jude",
 """Hey, Jude, don't make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better

Hey, Jude, don't be afraid
You were made to go out and get her
The minute you let her under your skin
Then you begin to make it better

And anytime you feel the pain,
Hey, Jude, refrain
Don't carry the world upon your shoulders
For well you know that it's a fool
Who plays it cool
By making his world a little colder

Nah, nah nah, nah nah, nah nah, nah nah

Hey, Jude, don't let me down
You have found her, now go and get her
Remember to let her into your heart
Then you can start to make it better

So let it out and let it in,
Hey, Jude, begin
You're waiting for someone to perform with
And don't you know that it's just you,
Hey, Jude, you'll do
The movement you need is on your shoulder

Nah, nah nah, nah nah, nah nah, nah nah yeah

Hey, Jude, don't make it bad
Take a sad song and make it better
Remember to let her under your skin
Then you'll begin to make it better, better, better, better, better... oh!

Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (yeah, yeah, yeah)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (don't make it bad, Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (take a sad song and make it better)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (oh, Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (Jude, hey, Jude, whoa)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (ooh)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude [fade out]"""],



["Звери","Районы кварталы",
 """Больше нечего ловить - все, что надо я поймал,
Надо сразу уходить, чтоб никто не привыкал.
Ярко-желтые очки, два сердечка на брелке,
Развеселые зрачки, твое имя на руке.

Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.
Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.

У тебя все будет класс, будут ближе облака,
Я хочу как в первый раз и поэтому пока.
Ярко-желтые очки, два сердечка на брелке,
Развеселые зрачки, я шагаю налегке.

Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.
Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.

Вот и все никто не ждет и никто не в дураках,
Кто-то любит, кто-то врет и летает в облаках.
Ярко-желтые очки, два сердечка на брелке,
Развеселые зрачки, я шагаю налегке.

Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.
Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.

Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво.
Районы, кварталы, жилые массивы,
Я ухожу, ухожу красиво."""],



["Imagine Dragons","Believer",
 """First things first
I'mma say all the words inside my head
I'm fired up and tired of the way that things have been, oh ooh
The way that things have been, oh ooh

Second things second
Don't you tell me what you think that I could be
I'm the one at the sail, I'm the master of my sea, oh ooh
The master of my sea, oh ooh

I was broken from a young age
Taking my sulking to the masses
Writing my poems for the few
That look at me, took to me, shook to me, feeling me
Singing from heartache from the pain
Taking my message from the veins
Speaking my lesson from the brain
Seeing the beauty through the...

Pain!
You made me a, you made me a believer, believer
Pain!
You break me down, you build me up, believer, believer
Pain!
Oh let the bullets fly, oh let them rain
My life, my love, my drive, it came from...
Pain!
You made me a, you made me a believer, believer

Third things third
Send a prayer to the ones up above
All the hate that you've heard has turned your spirit to a dove, oh ooh
Your spirit up above, oh ooh

I was choking in the crowd
Building my rain up in the cloud
Falling like ashes to the ground
Hoping my feelings, they would drown
But they never did, ever lived, ebbing and flowing
Inhibited, limited
Till it broke open and rained down
And rained down, like...

Pain!
You made me a, you made me a believer, believer
Pain!
You break me down, you build me up, believer, believer
Pain!
Oh let the bullets fly, oh let them rain
My life, my love, my drive, it came from...
Pain!
You made me a, you made me a believer, believer

Last things last
By the grace of the fire and the flames
You're the face of the future, the blood in my veins, oh ooh
The blood in my veins, oh ooh
But they never did, ever lived, ebbing and flowing
Inhibited, limited
Till it broke open and rained down
And rained down, like...

Pain!
You made me a, you made me a believer, believer
Pain!
You break me down, you build me up, believer, believer
Pain!
Oh let the bullets fly, oh let them rain
My life, my love, my drive, it came from...
Pain!
You made me a, you made me a believer, believer"""],



["Океан Ельзи","Без бою",
 """Що ж це я
Що ж це я не зумів
Зупинитися вчасно
Все ясно
Зі мною тепер і назавжди
Пізно не йди
Не йди від мене
Я налию собі, я налию тобі вина
А хочеш із медом

Приспів:
Хто ти є? Ти взяла моє життя
І не віддала
Хто ти є? Ти випила мою кров
І п’яною впала
Твої очі кличуть, хочуть мене,
Ведуть за собою
Хто ти є? І ким би не була ти,
Я не здамся без бою! (2)

Шо ж це я
Шо ж це я не зумів
Зупинити себе, тебе
Сьогодні
Сьогодні так дує
Без тебе сумую
Сумую без тебе
Накинь щось на себе
Я налию собі, я налию тобі вина
А хочеш із медом

Приспів

Я налию собі, я налию тобі вина
А хочеш із медом

Приспів

Я не здамся без бою!"""],



["Плач Єремії","Вона",
 """Завтра прийде до кімнати
Твоїх друзів небагато,
Вип'єте холодного вина.

Хтось принесе білі айстри,
Скаже хтось — життя прекрасне,
Так, життя прекрасне, а вона...

Припев:
А вона, а вона сидітиме сумна,
Буде пити — не п'яніти від дешевого вина.
Я співатиму для неї, аж бринітиме кришталь,
Та хіба зуміє голос подолати цю печаль.

Так вже в світі повелося —
Я люблю її волосся,
Я люблю її тонкі уста.

Та невдовзі прийде осінь,
Ми усі розбіжимося
По русифікованих містах.

Припев:
Лиш вона, лиш вона сидітиме сумна,
Буде пити — не п'яніти від дешевого вина.
Моя дівчинко печальна, моя доле золота,
Я продовжую кричати... ніч безмежна і пуста."""],



["Latexfauna","Космос",
 """Між кораблями – стиковочки
Нові космонавти – нові космонавточки
Нас сюди вела наукова практика
Вєлком – в нову галактику.
Вєлком – в нову галактику.

На, трьох, гейзерних планетах,
Зводять котеджі з пахучої сосни,
Всі окрім мене покинули ракету
А мене цікавлять тільки космос,
І еротичні сни.

Моя путь лежить крізь сузір'я лебедя,
Безмовно і чиста, вродє би будто я
І я досліджую всі недосліджені кратери,
Мій перший телескоп – молоко матері
Мій перший телескоп – молоко матері

На, трьох, гейзерних планетах,
Мене чекають молоді ліси.
Далі, по лунах, летить моя ракета,
Но мене цікавлять тільки космос,
І еротичні сни.

Но мене цікавлять тільки космос, і еротичні сни."""],



["Green Day","Boulevard of broken dreams(Музыкант вещает cover)",
 """Дорога за спиной
Не сможет дать сейчас ответ простой:
Кто твою мечту
Превратил в кошмар и пустоту?

На улице пустой
Эхом слёз - "Бульвар разбитых грёз",
В городе покой
Но ты один идешь по мостовой...

идешь один...навстречу...

И тень скользит неслышно по асфальту,
Пустое сердце продолжает биться,
Твой призрак - жив, поставил всё на карту,
Чтобы найти её...

И где же эта грань,
За которой ты не встретишь ложь?
Лишь шагнув на край
Ты её увидишь и поймёшь

Читаю между строк
Рухнувших надежд и сладких грёз:
Сорванный цветок
В глубине души твоей - живёт...

идешь один...навстречу...

И тень скользит неслышно по асфальту,
Пустое сердце продолжает биться,
Твой призрак - жив, поставил всё на карту,
Чтобы найти любовь...

(а-а а-а а-а а-а)

идешь один...навстречу...

И тень скользит неслышно по асфальту,
Пустое сердце продолжает биться,
Твой призрак - жив, поставил всё на карту,
Чтобы найти любовь..."""],



["Bon Jovi","It's my life",
 """This ain't a song for the broken-hearted
No silent prayer for the faith-departed
I ain't gonna be just a face in the crowd
You're gonna hear my voice
When I shout it out loud

It's my life
It's now or never
I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said,
"I did it my way."
I just wanna live while I'm alive
It's my life

This is for the ones who stood their ground
For Tommy and Gina who never backed down
Tomorrow's getting harder make no mistake
Luck ain't even lucky
Got to make your own breaks

It's my life
And it's now or never
I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said,
"I did it my way."
I just want to live while I'm alive
'Cause it's my life

Better stand tall when they're calling you out
Don't bend, don't break, baby, don't back down

It's my life
And it's now or never
'Cause I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said,
"I did it my way."
I just want to live while I'm alive

It's my life
And it's now or never
'Cause I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said,
"I did it my way."
I just want to live while I'm alive
'Cause it's my life!"""],



["Градусы","Режиссёр",
 """Я закрою за собою, ты сказала "я не стою"
Я подброшу на удачу, докурю и пойду дальше
Не дождётесь, не заплачу, если что любовь получит сдачи
Я в этом фильме главный актёр, я - сценарист в нём, я - режиссёр.
Припев:
Враг мой бойся меня, друг мой не отрекайся от меня
Нелюбимая, прости меня, любимая - люби меня.
(2 раза)

На минуту замечтаюсь, не летаю, но пытаюсь
Упаду и поднимаюсь, всё в порядке, оклемаюсь
Не дождётесь, не заплачу, если что любовь получит сдачи
Я в этом фильме главный актёр, я - сценарист в нём, я - режиссёр.

Припев.

Третий куплет на языке растафари (лично от DJ Baks):

It's only raf becoz we make our memo on
We shoulda be adaut discussing love
N get it raf in Babylon/И получать её раф в Вавилоне
It's only raf becoz to me come eire mammy
We shoulda be about discussing love
And get it raf abaut it, sweet
Com on ey yo yo lirigorri knoh
Swing by di rushes
Terapce means Babylon
Rastafariyah
Well prepapay!
Wit it 1, 2, 3, 4

Припев."""],



["Виктор Цой","Пачка Сигарет",
 """Я сижу и смотрю в чужое небо из чужого окна
И не вижу ни одной знакомой звезды.
Я ходил по всем дорогам и туда, и сюда, 
Обернулся - и не смог разглядеть следы.

Припев:
Но если есть в кармане пачка сигарет, 
Значит все не так уж плохо на сегодняшний день.
И билет на самолет с серебристым крылом, 
Что, взлетая, оставляет земле лишь тень.

И никто не хотел быть виноватым без вина, 
И никто не хотел руками жар загребать,
А без музыки на миру смерть не красна, 
А без музыки не хочется пропадать.

Припев:
Но если есть в кармане пачка сигарет, 
Значит все не так уж плохо на сегодняшний день.
И билет на самолет с серебристым крылом, 
Что, взлетая, оставляет земле лишь тень.

Но если есть в кармане пачка сигарет, 
Значит все не так уж плохо на сегодняшний день.
И билет на самолет с серебристым крылом, 
Что, взлетая, оставляет земле лишь тень.
"""],



["Linkin Park","Numb(Radio Tapok cover)",
 """Я устал быть другим для себя
Утратив веру, и свой потеряв путь
Что мне сделать еще для тебя?
Я словно под прессом, и на краю стою
(Да я попал в капкан, я снова попал в капкан)
В каждом следующем шаге - найдешь лишь вину мою
(Да я попал в капкан, я снова попал в капкан)

Я застрял в себе, и всё свёл на нет,
Но я нашел, где-то там ответ
Выходя из тьмы, просто став собой, 
Перестав быть тем, кем я был с тобой
 
Ты же видишь, что душишь меня
Крепко держа, боясь потерять контроль
Да, я знаю, что это любя
Стать тем, кем ты хочешь, но на краю стою
(Да я попал в капкан, я снова попал в капкан)
Даже в следующем шаге найдешь лишь вину мою
(Да я попал в капкан, я снова попал в капкан)
Тратя время на то, что меня разорвёт

Я застрял в себе, и всё свёл на нет,
Но я нашел, где то там ответ
Выходя из тьмы, просто став собой, 
Перестав быть тем, кем я был с тобой

И я знал, 
Что мог стать тем, кем хотел
Но я знал, также, что тебя кто-то в свое время тоже терпел

Я застрял в себе, и всё свёл на нет,
Но я нашел, где то там ответ
Выходя из тьмы, просто став собой, 
Перестав быть тем, кем я был с тобой

Я застрял в себе, и всё свёл на нет
(Я устал быть другим для себя)
 Я застрял в себе, и всё свёл на нет
(Я устал быть другим для себя)"""],



["System Of A Down","Lonely day",
 """Such a lonely day
And it's mine
The most loneliest day of my life

Such a lonely day
Should be banned
It's a day that I can't stand

The most loneliest day of my life
The most loneliest day of my life

Such a lonely day
Shouldn't exist
It's a day that I'll never miss
Such a lonely day
And it's mine
The most loneliest day of my life

And if you go, I wanna go with you
And if you die, I wanna die with you

Take your hand and walk away

The most loneliest day of my life
The most loneliest day of my life
The most loneliest day of my life
Life

Such a lonely day
And it's mine
It's a day that I'm glad I survived"""],



["System Of A Down","Lonely Day(Radio Tapok cover)",
 """Одинокий день
И он мой
Самый печальный день, что был со мной

Одинокий день
Он настал
Господи, как я устал

Самый печальный день, что был со мной
Самый печальный день, что был со мной

Одинокий день
Уходи
Нет, я не буду грустить

Одинокий день
И он мой
Самый печальный день, что был со мной

Если уйдешь, то я уйду с тобой
Если умрешь, то я умру с тобой
Обниму и выйдем прочь

Самый печальный день, что был со мной
Самый печальный день, что был со мной
Самый печальный день, что был со мной

Одинокий день
И он мой
В этот день, я остался живой.
"""],



["Imagine Dragons","Demons",
 """When the days are cold
And the cards all fold
And the saints we see
Are all made of gold

When your dreams all fail
And the ones we hail
Are the worst of all
And the blood's run stale

I wanna hide the truth
I wanna shelter you
But with the beast inside
There's nowhere we can hide

No matter what we breed
We still are made of greed
This is my kingdom come
This is my kingdom come

When you feel my heat
Look into my eyes
It's where my demons hide
It's where my demons hide
Don't get too close
It's dark inside
It's where my demons hide
It's where my demons hide

At the curtain's call
It's the last of all
When the lights fade out
All the sinners crawl

So they dug your grave
And the masquerade
Will come calling out
At the mess you made

Don't wanna let you down
But I am hell bound
Though this is all for you
Don't wanna hide the truth

No matter what we breed
We still are made of greed
This is my kingdom come
This is my kingdom come

When you feel my heat
Look into my eyes
It's where my demons hide
It's where my demons hide
Don't get too close
It's dark inside
It's where my demons hide
It's where my demons hide

They say it's what you make
I say it's up to fate
It's woven in my soul
I need to let you go

Your eyes, they shine so bright
I wanna save that light
I can't escape this now
Unless you show me how

When you feel my heat
Look into my eyes
It's where my demons hide
It's where my demons hide
Don't get too close
It's dark inside
It's where my demons hide
It's where my demons hide"""],



["Nirvana","Smells like teen spirit",
 """Load up on guns, bring your friends
It's fun to lose and to pretend
She's over bored and self assured
Oh no, I know a dirty word

Hello, hello, hello, how low? [x3]
Hello, hello, hello!

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto
An albino
A mosquito
My libido
Yeah, hey, yay

I'm worse at what I do best
And for this gift I feel blessed
Our little group has always been
And always will until the end

Hello, hello, hello, how low? [x3]
Hello, hello, hello!

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto
An albino
A mosquito
My libido
Yeah, hey, yay

And I forget just why I taste
Oh yeah, I guess it makes me smile
I found it hard, it's hard to find
Oh well, whatever, never mind

Hello, hello, hello, how low? [x3]
Hello, hello, hello!

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto
An albino
A mosquito
My libido

A denial! [x9]"""],



["Nirvana","Smells like teen spirit(Музыкант вещает cover)",
 """Возьми ружьё,
Зови друзей,
На виски денег не жалей,
И приходи сегодня к нам пришла пора напиться в хлам,

Припев*
Привет привет,
Лови момент,
Привет привет,
Лови момент , 
Привет привет, 
Лови момент ,
Привет привет привет...

В темноте нам - интересней,
Звон стаканов-станет песней ,
Эта глупасть- так заразна ,
Развлекай нас- что не ясно??
Бьем посуду ,телевизор,
А потом со-седей снизу 

(Еее--------хей-----------------хей-----------)
(Маленький проигрыш)

2 куплет .
Из лучших худших-это я ,
И эти пьяные друзья,
У нас профессия -дебош
Компаний лучше не найдешь

Припев.

3 куплет
Я забывают что к чему ,
Мой ум купается в дыму
Нас утром будет не поднять но нам на это наплевать,

Припев )2 раза

Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаюсь!
Отрекаююююююююссссссьььь!!!!!"""],



["Народ","Житомир",
 """А це було в сільскому клубі,
де вишивали чуваки,
дівчата лускали насіння,
а хлопці гнули матюки.

Ми познайомились на танцях,
а ти була в рожевих штанцях,
тебе я сразу покохав,
бо в тебе лівчик виглядав.

А ми їбалися на криші,
в 40-градусний мороз,
твоя пізда покрилась льодом,
мій хуй встрічав дід мороз.

А ми лежим на купі гною,
а я милуюся тобою,
на тобі пляттячко рябе,
мабуть я виїбу тебе.

О-о-о, Житомир, це не місто не село,
О-о-о, Житомир, куди нас нахуй занесло.

А на Житомирськом вокзалі,
обвалився потолок,
Бабу Нюру придавило, 
аж з пізди пішов димок.

А на Житомирськом вокзалі,
кугути автобус ждали,
хто з лопатой, хто з мішком,
усі попиздили пішком.

А це було біля вокзалу,
де пролітав аероплан,
усі їбальніки задерли,
а я спиздив чемодан.

А це було біля вокзалу,
де задавили мурав'я,
цілий місяць м'ясо їли,
да ще осталось дохуя.

О-о-о, Житомир, це не місто не село,
О-о-о, Житомир, куди нас нахуй занесло.

А очеретом хата вкрита,
а до двере пизда прибита,
а хто і їде, хто і йде,
туди копіючку кладе.

А ішов батько, ішов я,
да не поклали ніхуя,
батько прямо, а я в бік,
батька пиздять, а я втік.

А я біжу по кукурузі,
а качани по яйцям б'ють,
а зупинитися не можу,
бо доженуть, пизди дадуть

О-о-о, Житомир, це не місто не село,
О-о-о, Житомир, куди нас нахуй занесло.

А тётя Рая, тётя Рая,
а вам посилка із Шанхая,
а в посилке три китайця,
і дружно дєржуться за ящик.

А на рєкє качався буй,
к нему пливёт какой-то дядя,
дядя-дядя не валуй,
а то дєльфін откусит ногу.

А то ведь вовсе был не буй,
а то ведь вовсе был не буй,
а то ведь вовсе был не буй,
а от кита огромный хвост.

На бэрегу лежат 2 трупа,
на бэрегу лежат 2 трупа,
у одного из-под улупа,
лежит огромная... Збер-книжка.

Себя от голода страхуя,
зашли в кабак 4 дяди,
у одного из-под улупа,
торчала конская... Узда.

А хрестьянин торжествуя,
б'ёт коня за кончик... Уха.
ему на встречу идёт старуха,
ведёт быка за тоже ухо.

Пошёл в аптеку Дед Антон,
что бы купить себе... Таблетки,
а у него из-под улупа,
торчала красная... Рубашка.

Какой-то маленький вассал,
все стенки замка обошёл,
но нечего там не нашёл,
он к секретарше подошёл.

А тётя Валя, тётя мать,
ведь вы порядочная... Тётя,
вы мне скажите где живёте,
и я приййду к вам ночевать

О-о-о, Житомир, це не місто не село,
О-о-о, Житомир, куди нас нахуй занесло."""],



["Скрябін","Старі фотографії",
 """Здається, шо то було так давно,
Коли в руках тримаю цей альбом,
Нам було абсолютно все одно
Немаючи нічого мати всьо,
За гроші не купити тільки час,
Він всіх нас методично поділив,
Когось він опустив, когось підняв,
А є на кого взагалі забив.

Приспів:
Старі фотографії на стіл розклади,
Дитячі історії смішні розкажи
І справжнім друзям не забудь, подзвони
Бо добре чи зле, з тобою завжди вони

Дешеве пиво і сухе вино,
Робили нас щасливими людьми,
І ніби чудо польське радіо,
Нам відкривало той незнаний світ

Ми жили всі так ніби, то був сон
І можна бути вічно молодим,
А залишився тільки цей альбом,
А мрії розлетілися, як дим.

Приспів.

Ми грали примітивну музику,
Так чесно, що пробила би до сліз
Чекали, що прийде такий момент
Коли під ноги впаде цілий світ
Годинник вперто роки рахував,
І кожен так як міг так і зробив
І тільки у альбомі всі підряд
Ми будемо такими, як тоді

Приспів (2)"""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]



#["","",""""""]
]

