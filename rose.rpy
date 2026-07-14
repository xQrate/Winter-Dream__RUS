label roseroutestart:

    scene bg bedroom with fade

    show velda nervous with dissolve
    v "Почему бы тебе не встать, прежде чем я выброшу тебя вместе с остальным мусором?"
    c "Твой босс будет в порядке от этого?"
    show velda frown with dissolve
    v "Наверное, нет, но мне всё равно."
    c "Что ж, я встаю."
    c "Но мне не нужна ты здесь."
    c "Мне было бы неловко, если бы кто-то смотрел, как я раздеваюсь."
    show velda nervous with dissolve
    v "Ни один нормальный человек не захотел бы смотреть, как ты раздеваешься."
    c "Угу..."
    hide velda nervous with dissolve
##################################################################

    play music normalday
    scene bg park 2 day with fade

    x "Я быстро перекусываю и иду в парк."
    x "Как я и ожидал, Роуз там."
    x "Она сидит на скамейке и кормит птиц."
    x "Поговорить с ней?"

menu:

    "Поговорить с Роуз":
        jump talktoroseday4

    "Не разговаривать с ней":
        jump notalktoroseday4

label talktoroseday4:

    $ rosepoints += 1
    x "Раз уж я здесь, могу и поговорить."
    x "Подхожу к ней."
    c "Привет."
    show rose normal with dissolve
    r "Привет."
    jump roseparkday4

label notalktoroseday4:

    $ rosebad += 1
    x "Э, не стоит."
    x "Она замечает меня и машет рукой."
    x "Не думая, я подхожу к ней."
    jump roseparkday4

label roseparkday4:

    show rose smile with dissolve
    r "Ты довольно рано вышел."
    c "Это рано или ты тут уже давно и потеряла счёт времени?"
    show rose normal with dissolve
    r "Любое возможно, на самом деле."
    x "Роуз просто смеётся."
    c "Так ты кормишь птиц."
    show rose smile with dissolve
    r "Ага."
    c "Почему?"
    show rose normal with dissolve
    r "А почему нет?"
    c "Просто подумал, что это милое занятие, да?"
    show rose smile with dissolve
    r "Ага!"
    c "Понятно."
    show rose normal with dissolve
    r "Хочешь покормить их тоже?"
    c "Я пас."
    show rose nervous with dissolve
    r "О, ладно."
    x "Она продолжает бросать кусочки хлеба, которые птицы продолжают клевать."
    show rose normal with dissolve
    r "Ах, у меня почти закончились."
    x "Затем она бросает остатки на землю."
    show rose smile with dissolve
    r "Думаю, я закончила здесь."
    c "Закончила?"
    show rose normal with dissolve
    r "Ага!"
    show rose nervous with dissolve
    r "Мне теперь нужно быть в другом месте."
    c "Куда?"
    show rose normal with dissolve
    r "В больницу."
    c "Зачем?"
    c "Что-то случилось?"
    show rose smile with dissolve
    r "О, нет."
    show rose normal with dissolve
    r "Я просто жертвую кое-какие вещи."
    c "Какие?"
    show rose smile with dissolve
    r "Игрушки для детей, немного денег на оборудование, которое им понадобится... такое."
    show rose normal with dissolve
    r "Раз ты здесь, почему бы тебе не пойти со мной?"

menu:

    "Пойти с Роуз":
        jump gowithrosetohospital

    "Не идти с Роуз":
        jump nogowithrosetohospital

label gowithrosetohospital:

    $ rosepoints += 1
    c "Да, конечно."
    c "Я пойду."
    hide rose normal with dissolve
    stop music fadeout 1.0
##################################################################

    play music happydays
    scene bg hospital waiting with fade
    x "Мы вдвоём в больнице."
    w "Спасибо, что снова это делаешь."
    show rose smile with dissolve
    r "Без проблем."
    w "Как нам тебя отблагодарить за доброту?"
    show rose normal with dissolve
    r "Не нужно."
    show rose smile with dissolve
    r "Я делаю это, потому что хочу."
    show rose normal with dissolve
    r "Мне ничего не нужно взамен."
    w "Понятно."
    x "Затем женщина оставляет нас вдвоём."
    c "Ты правда очень добрый человек, да?"
    show rose shock with dissolve
    r "Ты так думаешь?"
    c "Ну, тебе нравится делать что-то для других, не получая ничего взамен."
    show rose normal with dissolve
    r "Это потому что мне ничего не нужно."
    c "Я знаю."
    c "Почему ты такая добрая?"
    show rose nervous with dissolve
    r "Что ты имеешь в виду?"
    show rose normal with dissolve
    r "Просто я такая."
    c "Прости, что спросил."
    show rose smile with dissolve
    r "Не извиняйся за это."
    show rose normal with dissolve
    r "В-В общем, спасибо, что пошёл со мной."
    c "А, без проблем."
    show rose smile with dissolve
    r "Что ж, я пойду домой."
    show rose normal with dissolve
    r "Увидимся завтра."
    c "А, да."
    hide rose normal with dissolve
    jump roseday4over

label nogowithrosetohospital:

    $ rosebad += 1
    c "Нет, спасибо."
    c "Развлекайся."
    show rose nervous with dissolve
    r "Ладно."
    stop music fadeout 1.0
    hide rose nervous with dissolve
##################################################################

    play music snowydays
    scene bg restaurant with fade
    x "Я возвращаюсь в ресторан."
    show velda nervous with dissolve
    v "Что ты делал всё утро?"
    c "Не вижу, почему это твоё дело."
    show velda frown with dissolve
    v "Раз уж ты здесь, почему бы не взяться за работу?"
    c "Да, ладно."
    hide velda frown with dissolve
    x "Делаю, как она говорит, и берусь за работу."
    x "Место не такое уж загруженное, так что она бы справилась и без меня."
    x "Но всё же, вдвоём, всё проходит довольно гладко."
    x "Хотя Вельда продолжает жаловаться на ошибки, которые я делаю."
    x "Думаю, она из тех, кого никогда не удовлетворишь..."
    jump roseday4over
##################################################################
label roseday4over:

    stop music fadeout 1.0
    scene bg bedroom with fade
    x "Роуз — один из самых добрых людей, которых я встречал."
    x "Пугает, насколько она добрая."
    x "Есть ли у неё скрытая сторона?"
    x "Я просто не знаю."
    x "Но если она правда такая добрая, я должен радоваться, что такие люди существуют."
    x "Пока я думаю о ней, я засыпаю."
##################################################################

    # День 5 #

    play music veldatheme
    scene bg bedroom with fade
    show velda angry with dissolve
    v "Почему ты всё ещё спишь?"
    c "Почему ты всё ещё играешь роль моего будильника?"
    show velda smile with dissolve
    v "Твой дядя сказал мне следить, чтобы ты проснулся."
    c "Что ж, теперь я не сплю."
    show velda nervous with dissolve
    v "Что ж, не засыпай обратно."
    c "И не собирался."
    show velda smile with dissolve
    v "Хорошо."
    show velda frown with dissolve
    v "Я бы убила тебя, если бы ты заснул."
    c "Угу."
    show velda angry with dissolve
    v "Вставай."
    show velda normal with dissolve
    v "Потом оденься."
    show velda frown with dissolve
    v "А потом проваливай с глаз моих."
    c "Как насчёт того, чтобы ты провалила с моих, чтобы я мог одеться?"
    show velda nervous with dissolve
    v "Конечно, я уйду, чтобы ты мог это сделать!"
    show velda angry with dissolve
    v "Ты что, думаешь, я из тех людей!?"
    c "Из раздражающих?"
    play sound slap
    c "Ой."
    show velda nervous with dissolve
    v "Ты это заслужил и сам это знаешь!"
    c "Может, и так..."
    c "Так... ты уйдёшь сейчас?"
    c "Я бы хотел одеться."
    show velda frown with dissolve
    v "Тьфу."
    stop music fadeout 1.0
    hide velda frown with dissolve
##################################################################
    scene bg restaurant with fade
    play music morningactivity
    d "Доброе утро."
    g "У тебя красное пятно на лице."
    c "Правда?"
    g "Ага."
    d "О, что случилось?"
    c "Будильник, который ты мне дал, слишком жестокий."
    d "О, это Вельда..."
    d "Ну, зато эффективно, не так ли?"
    c "Я бы предпочёл, чтобы «эффективно» и «больно» не стояли в одном предложении."
    show velda nervous with dissolve
    v "Вы двое закончили?"
    hide velda nervous with dissolve
    show gwen frown with dissolve
    g "Прости."
    show gwen nervous with dissolve
    g "Я буду тихой."
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Не ты."
    hide velda normal with dissolve
    show gwen normal with dissolve
    g "О."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Но, пожалуйста, не поощряй их."
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Х-Хорошо."
    d "Собираешься за работу?"
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Д-да, сэр."
    d "Что касается тебя, Карон..."
    c "Да?"
    d "Ты будешь работать сегодня после обеда."
    c "Понял."
    stop music fadeout 1.0
    hide velda normal with dissolve
##################################################################

    play music rosetheme
    scene bg park 2 day with fade
    show rose shock with dissolve
    r "У тебя ярко-красное пятно на лице."
    c "Знаю."
    c "Это подарок от моего будильника."
    show rose frown with dissolve
    r "Я никогда не слышала о будильнике, который причиняет боль."
    c "Это Вельда."
    show rose nervous with dissolve
    r "..."
    c "Что?"
    show rose frown with dissolve
    r "Это значит...?"
    c "Что?"
    show rose shock with dissolve
    r "Вы двое спите вместе?"
    c "Нет, нет, нет!"
    c "Откуда ты вообще взяла ЭТУ идею?"
    show rose normal with dissolve
    r "От тебя."
    show rose smile with dissolve
    r "Только что."
    c "Но я такого не говорил..."
    show rose normal with dissolve
    r "Но ты только что сказал, что она твой будильник..."
    c "Да, но я не говорил, что мы спим вместе!"
    c "Мой дядя просто посылает её в мою комнату каждое утро, чтобы разбудить меня."
    show rose nervous with dissolve
    r "О."
    show rose normal with dissolve
    r "Это всё?"
    c "Это всё."
    show rose nervous with dissolve
    r "Я на секунду испугалась."
    c "Я не из тех парней, которые думают о сексе всё время."
    c "Честно говоря, предпочитаю не думать."
    show rose normal with dissolve
    r "Секс — это, честно говоря, отвратительно."
    c "А, да, вроде согласен."
    c "Но именно так появляются дети..."
    c "Довольно мерзко думать о том, как мы все здесь оказались."
    show rose nervous with dissolve
    r "Да..."
    c "Давай не будем об этом!"
    x "Это не тот разговор, который я должен вести с девушкой!"
    x "Если подумать, какой вообще разговор стоит вести с девушкой?"

    stop music fadeout 1.0
    play sound womancry
    x "Прежде чем я успеваю придумать, как сменить тему, мы слышим что-то."
    stop sound fadeout 1.0
    x "Похоже на плач ребёнка."

menu:

    "Проверить":
        jump checkoutcrying

    "Не обращать внимания":
        jump ignorethecrying

    "Спросить Роуз, что делать":
        jump askrosewhattodo

label checkoutcrying:
    $ rosepoints += 1
    $ achievement.grant("Good_Human")
    c "Давай посмотрим, что случилось."
    show rose normal with dissolve
    r "Я как раз собиралась предложить то же самое."
    c "Я знал, что ты захочешь так сделать."
    c "Ты бы не проигнорировала такое."
    show rose smile with dissolve
    r "Верно."
    jump roseseeswhatiswrong

label ignorethecrying:
    $ rosebad += 1
    x "Э, не моя проблема."
    x "Кто-нибудь другой разберётся."
    $ achievement.grant("Horrible_Human")
    show rose normal with dissolve
    r "Я пойду посмотрю, что случилось."
    x "Похоже, Роуз пойдёт."
    show rose nervous with dissolve
    r "Пойдём."
    c "Х-Хорошо."
    jump roseseeswhatiswrong

label askrosewhattodo:
    c "Эм..."
    c "Нам стоит что-то сделать?"
    show rose normal with dissolve
    r "Ну, я не могу просто стоять и ничего не делать."
    show rose nervous with dissolve
    r "Я пойду посмотрю, что случилось."
    c "Тогда я пойду с тобой."
    jump roseseeswhatiswrong

label roseseeswhatiswrong:

    play music bittersweet

    x "Мы подходим к ребёнку."
    ug "Мама..."
    show rose normal with dissolve
    r "Привет."
    ug "...!"
    show rose nervous with dissolve
    r "Что случилось?"
    ug "Я играла... а потом теперь я... Мама и Папа... я не могу их найти!"
    show rose normal with dissolve
    r "Ты потерялась?"
    ug "Я не потерялась!"
    ug "Мама и Папа просто слишком хорошо играют в прятки!"
    show rose smile with dissolve
    r "Тогда давай найдём их."
    x "Маленькая девочка шмыгает носом."
    ug "Ты... поможешь мне?"
    show rose normal with dissolve
    r "Ага."
    show rose smile with dissolve
    r "Правда, Карон?"

menu:

    "Да":
        jump helprosefindthem

    "Остаться":
        jump staybehindandnothelp

label helprosefindthem:
    $ rosepoints += 1
    c "Да."
    c "Я помогу."
    ug "С-Спасибо."
    hide rose smile with dissolve
##################################################################
    scene bg downtown day with fade
    x "Роуз и я ходим по всему городу в поисках родителей девочки."
    x "В конце концов мы их находим."
    w "Тебе нельзя уходить так далеко."
    ug "Я не потерялась!"
    ug "Вы просто слишком хорошо прячетесь!"
    w "Всё равно, рада, что ты вернулась."
    w "Спасибо вам двоим."
    ug "Да, спасибо!"
    show rose smile with dissolve
    r "Пожалуйста."
    c "Ага."
    stop music fadeout 1.0
    x "Девочка уходит с родителями."
    jump parentsfound

label staybehindandnothelp:
    $ rosebad += 1
    c "Вообще-то, я останусь здесь."
    show rose normal with dissolve
    r "О, хочешь разделиться?"
    show rose smile with dissolve
    r "Это может помочь!"
    c "Конечно..."
    x "На самом деле, я вру."
    hide rose smile with dissolve
    x "Роуз уходит с маленькой девочкой."
    stop music fadeout 1.0
    x "Через несколько минут я понимаю, что просто стою один, и ухожу."
##################################################################
    scene bg street day with fade
    play sound walkingoutside
    x "С руками в карманах я иду по району."
    x "На ходу я вижу знакомое лицо."
    stop sound fadeout 1.0
    show rose normal with dissolve
    r "А, Карон!"
    c "Итак, как всё прошло?"
    show rose smile with dissolve
    r "Мы их нашли!"
    c "Это хорошо."
    show rose normal with dissolve
    r "Ага!"
    hide rose normal with dissolve
    jump parentsfound

label parentsfound:

    scene bg street 2 day with fade
    c "Ты правда любишь помогать людям."
    show rose normal with dissolve
    r "Наверное..."
    show rose smile with dissolve
    r "Я... правда люблю детей."

    play music rosetheme

    show rose nervous with dissolve
    r "Так что мне не нравится видеть их грустными."
    x "Когда она это говорит, её глаза выглядят грустными."
    c "Эм... Роуз?"
    show rose normal with dissolve
    r "Да?"
    c "Ничего."
    c "Наверное, мне показалось."
    show rose nervous with dissolve
    r "О?"
    c "Ага."
    c "Не переживай об этом."
    show rose normal with dissolve
    r "Но теперь мне любопытно."
    c "Может, расскажу позже."
    show rose smile with dissolve
    r "Обещаешь?"
    c "Может быть."
    show rose nervous with dissolve
    r "..."
    c "Это даже не так важно."
    show rose normal with dissolve
    r "Тогда, думаю, это не имеет значения."
    stop music fadeout 1.0
    x "Я провожу с ней ещё немного времени, прежде чем идти домой."
    show rose normal with dissolve
##################################################################
    scene bg restaurant with fade
    show velda angry with dissolve
    v "Ты опоздал."
    c "Прости."
    c "Кое-что случилось."
    show velda nervous with dissolve
    v "Тьфу."
    show velda normal with dissolve
    v "Не то чтобы кто-то умер или что-то такое."
    c "Нет."
    show velda frown with dissolve
    v "За работу."
    c "Верно."
    c "Сделаю."
    hide velda frown with dissolve
##################################################################

    # День 6 #

    play music snowydays
    scene bg restaurant with fade
    c "Можно тебя кое-что спросить?"
    d "Что?"
    c "Можешь рассказать мне что-нибудь о Роуз?"
    d "Она правда добрая, да?"
    c "Э... да."
    d "Она всегда помогает всем в городе."
    d "Она часто жертвует деньги или игрушки для детей."
    d "Она даже помогала здесь, когда дела шли плохо."
    c "Понятно."
    show velda nervous with dissolve
    v "Ну, я её терпеть не могу."
    c "О?"
    show velda frown with dissolve
    v "Она тошнотворно милая."
    show velda angry with dissolve
    v "Нет ни единого шанса, что она показывает нам свою настоящую натуру."
    c "Думаешь, она что-то скрывает?"
    show velda frown with dissolve
    v "Просто не выношу людей, которые настолько добрые."
    c "Это потому что ты сама не такая?"
    play sound slap
    c "Ой."
    d "Ты сам напросился, Карон."
    c "Наверное..."
    c "Вы с Роуз поссорились?"
    show velda nervous with dissolve
    v "Нет."
    show velda frown with dissolve
    v "Но меня раздражает, когда она в той же комнате."
    c "О, ладно."
    hide velda frown with dissolve
    show gwen nervous with dissolve
    g "Тебе не нравится Роуз?"
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Нет."
    hide velda normal with dissolve
    show gwen frown with dissolve
    g "О."
    hide gwen frown with dissolve
    show velda nervous with dissolve
    v "Эй, не выгляди так разочарованно."
    c "Она была здесь всё это время?"
    show velda normal with dissolve
    v "Она приходит сюда каждое утро."
    show velda nervous with dissolve
    v "Где тебя черти носили?"
    d "Что ж, что ты о ней думаешь?"
    c "Т-Ты хочешь знать, что я думаю?"
    d "Ага."
    show velda frown with dissolve
    v "Мне плевать, что ты о ней думаешь."
    hide velda frown with dissolve
    show gwen smile with dissolve
    g "Я хочу знать..."
    c "Ты тоже?"
    c "Ну..."

menu:

    "Она мне нравится":
        jump caronlikesrose

    "Она хороший друг":
        jump roseisgoodfriend

    "Я согласен с Вельдой":
        jump agreewithvelda

    "Не уверен":
        jump notsureaboutrose

label caronlikesrose:
    $ rosepoints += 1
    $ admitlikerose = True
    c "Я... вроде как она мне нравится."
    show gwen normal with dissolve
    g "О..."
    d "Понятно."
    c "Пожалуйста, не делайте из этого большое событие..."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Тьфу."
    hide velda nervous with dissolve
    jump danasksaboutrose

label roseisgoodfriend:
    $ rosepoints += 1
    c "Она хороший друг."
    show gwen nervous with dissolve
    g "О."
    d "Хм."
    c "Не надо так разочарованно звучать."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Хмф."
    hide velda nervous with dissolve
    jump danasksaboutrose

label agreewithvelda:
    $ rosebad += 1
    c "Я на самом деле согласен с Вельдой."
    hide gwen smile with dissolve
    show velda normal with dissolve
    v "Так тебя она тоже раздражает..."
    hide velda normal with dissolve
    show gwen nervous with dissolve
    g "..."
    d "Хех."
    c "..."
    hide gwen nervous with dissolve
    jump danasksaboutrose

label notsureaboutrose:
    c "Я на самом деле не уверен."
    hide gwen smile with dissolve
    show velda nervous with dissolve
    v "Не уверен?"
    c "Ага, не знаю, что и чувствовать."
    c "Она мне не неприятна, но..."
    show velda normal with dissolve
    v "Да мне плевать."
    show velda nervous with dissolve
    v "Не важно."
    hide velda nervous with dissolve
    jump danasksaboutrose

label danasksaboutrose:
    c "Можем прекратить об этом?"
    d "Да, конечно."
    show gwen normal with dissolve
    g "Ладно."
    c "Это правда не ваше дело."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Я не спрашивала."
    c "Я знаю, что ТЕБЕ плевать, но остальные — другое дело."
    show velda frown with dissolve
    v "Просто заткнись и дай мне работать."
    c "Хорошо..."
    hide velda frown with dissolve
##################################################################
    # Карон прямо у ресторана
    scene bg street 2 day with fade
    play music calm
    show rose normal with dissolve
    r "О, я как раз тебя искала."
    c "Ты пришла меня увидеть?"
    show rose smile with dissolve
    r "Ага."
    c "Можно кое-что спросить?"
    show rose normal with dissolve
    r "Ты только что спросил."
    c "Я не это имел в виду."
    show rose smile with dissolve
    r "Какой у тебя вопрос?"
    c "Почему ты продолжаешь со мной разговаривать?"
    show rose nervous with dissolve
    r "Разве обычно не ты приходишь ко мне большую часть времени?"
    c "Наверное."
    c "Но ведь я не особенный, да?"
    show rose frown with dissolve
    r "Тебя раздражает, что я пришла тебя увидеть?"

menu:

    "Не особо":
        jump doesnotbothermerose

    "Ещё как":
        jump itsuredoesrose

label doesnotbothermerose:
    $ rosepoints += 1
    c "Нет, не особо раздражает."
    show rose smile with dissolve
    r "Хорошо."
    show rose normal with dissolve
    r "Не хотела бы тебя раздражать."
    c "Что ж, не раздражаешь."
    jump roseday6continues

label itsuredoesrose:
    $ rosebad += 1
    c "Ещё как."
    show rose frown with dissolve
    r "Карон?"
    show rose nervous with dissolve
    r "Прости."
    c "..."
    c "Да пофиг."
    c "Тебе что-то от меня было нужно?"

    if rosebad >= 6:
        jump roseday6badend
    else:
        jump roseday6continues

label roseday6badend:

    stop music fadeout 1.0

    show rose frown with dissolve
    r "Я хочу, чтобы ты перестал крутиться рядом со мной."
    c "Почему?"
    play music regrets
    show rose frown with dissolve
    r "Ты не кажешься очень приятным."
    show rose normal with dissolve
    r "Я была рядом с тобой достаточно долго, чтобы это заметить..."
    show rose frown with dissolve
    r "Просто не хочу, чтобы ты был со мной."
    c "Эм... ладно?"
    show rose nervous with dissolve
    r "Вот и всё, что я хотела сказать."
    c "Это всё?"
    show rose frown with dissolve
    r "Тебе вообще всё равно, да?"
    c "Не особо."
    show rose angry with dissolve
    r "Что с тобой не так?"
    c "Не знаю и мне плевать."
    show rose normal with dissolve
    r "Что ж, на этом всё."
    c "Ладно."
    x "Она разворачивается и уходит."
    hide rose normal with dissolve
    scene bg black with fade
    x "Это был последний раз, когда я её видел."
    x "Остаток моих каникул прошёл нормально."
    x "Ничего особенного не случилось."
    x "По крайней мере, я был рад, что не вляпался ни во что плохое."
    stop music fadeout 1.0
    $ achievement.grant("Caron_Dick")
    x "ПЛОХАЯ КОНЦОВКА — КАРОН КОЗЁЛ"
    # Титры нейтральной концовки
    $ renpy.movie_cutscene("video/NeutralCredits.webm", delay=100, loops=0, stop_music=True)
    return

label roseday6continues:

    stop music fadeout 1.0
    play music bittersweet
    show rose nervous with dissolve
    r "Обычно никто не остаётся рядом со мной."
    show rose frown with dissolve
    r "Им кажется, что то, что я делаю, скучно."
    show rose nervous with dissolve
    r "Просто у них нет интереса помогать другим."
    show rose smile with dissolve
    r "Но ты другой."
    c "Просто я такой."
    show rose normal with dissolve
    r "Так что ты думаешь о том, чтобы быть лучшими друзьями?"
    c "Эй, разве не рановато для этого?"
    r "Нет."
    x "Что я думаю?"

menu:

    "Звучит хорошо":
        jump soundsgoodrose

    "Можем быть кем-то большим?":
        jump canwebemorerose

    "Может быть...":
        jump mayberose

    "Нет":
        jump nojustnorose

label soundsgoodrose:
    $ rosepoints += 1
    $ rosebff = True
    c "Звучит хорошо."
    show rose smile with dissolve
    r "Ты серьёзно?"
    c "Ага."
    $ achievement.grant("BFF_Agree")
    c "Отныне мы лучшие друзья."
    x "Она выглядит счастливой."
    x "Честно говоря, я тоже счастлив."
    jump rosebffoffer

label canwebemorerose:
    $ rosepoints += 1
    $ confesstorose = True
    c "Я... на самом деле..."
    show rose nervous with dissolve
    r "Что?"

    if admitlikerose == True:
        jump roseconfession1
    else:
        jump roseconfession2

label roseconfession1:
    x "Я уже рассказал остальным."
    x "Думаю, сейчас подходящее время."
    c "Ты мне правда нравишься."
    jump roseconfessionover

label roseconfession2:
    c "Эм..."
    show rose smile with dissolve
    r "Выкладывай."
    c "Ты мне нравишься. Сильно."
    jump roseconfessionover

label roseconfessionover:
    show rose normal with dissolve
    $ achievement.grant("Rose_Confess")
    r "Я... тебе нравлюсь?"
    c "Да... в смысле, по-настоящему нравишься."
    show rose shock with dissolve
    r "..."
    show rose embarassed with dissolve
    r "А..."
    show rose nervous with dissolve
    r "Эм..."
    show rose normal with dissolve
    r "Я не знаю."
    c "..."
    show rose nervous with dissolve
    r "Прости."
    c "Ладно."
    show rose normal with dissolve
    r "Мы ведь всё ещё можем быть друзьями?"
    c "Ага."
    jump rosebffoffer

label mayberose:
    c "Может быть..."
    c "Не знаю."
    r "Ты не уверен?"
    show rose nervous with dissolve
    r "Почему?"
    c "Не знаю."
    show rose normal with dissolve
    r "Думаю, ты можешь быть прав."
    c "Нам не нужно беспокоиться об этом прямо сейчас."
    show rose smile with dissolve
    r "Ладно."
    jump rosebffoffer

label nojustnorose:
    $ rosebad += 1
    c "Нет."
    show rose frown with dissolve
    r "Не хочешь?"
    c "Нет."
    c "Прости."
    show rose nervous with dissolve
    r "Может, ты прав..."
    show rose normal with dissolve
    r "Рано?"
    c "Давай не будем об этом сейчас."
    show rose smile with dissolve
    r "Ладно."
    jump rosebffoffer

label rosebffoffer:
    show rose nervous with dissolve
    r "Так что нам делать?"
    c "Не знаю."
    show rose normal with dissolve
    r "Давай прогуляемся."
    c "Хорошо..."
    hide rose normal with dissolve
    stop music fadeout 1.0
##################################################################

    play music veldatheme
    scene bg restaurant with fade
    show velda normal with dissolve
    v "Похоже, ты поладил с этой девушкой."
    c "А, да, наверное..."
    show velda nervous with dissolve
    v "Хмф."
    c "Я думал, тебе плевать."
    show velda frown with dissolve
    v "Плевать."
    c "Тогда зачем говоришь об этом?"
    show velda angry with dissolve
    v "Заткнись."
    d "Так, так."
    d "Вам двоим не нужно ссориться прямо сейчас."
    d "За работу."
    show velda frown with dissolve
    v "Он начал."
    d "Я был здесь всё это время."
    d "Ты начала разговор."
    show velda nervous with dissolve
    v "Гррр..."
    hide velda nervous with dissolve
    d "Так..."
    c "Что?"
    d "Как всё прошло?"
    c "Как что прошло?"
    d "Ты и Роуз."
    c "Мы просто поговорили, вот и всё."
    d "О чём?"

    if confesstorose == True:
        jump telldanaboutconfession
    else:
        jump whatcarontalkedtoroseabout

label telldanaboutconfession:
    c "Я сказал ей, что она мне нравится."
    d "О, правда?"
    c "Она не приняла."
    d "О."
    c "Я буду в порядке."
    jump day6ending

label whatcarontalkedtoroseabout:
    c "Мы просто поговорили о нашей дружбе."
    d "Это всё?"
    c "Что?"
    c "Ты разочарован?"
    d "Нет..."
    c "Твой тон говорит об обратном..."
    jump day6ending

##################################################################

label day6ending:

    scene bg bedroom with fade
    stop music fadeout 1.0
    play music calm

    x "Что с моим дядей?"
    x "Ему не нужно знать вообще обо всём, не так ли?"
    x "Если я рядом с девушкой, он становится любопытным."
    x "Он, честно говоря, как мама."
    x "И Роуз..."
    x "Я определённо хочу проводить с ней больше времени."

    if confesstorose == True:
        jump caronlikesrose1
    elif admitlikerose == True:
        jump caronlikesrose2
    elif rosebff == True:
        jump bestfriendswithrosenow
    else:
        jump hangoutwithrosemore

label caronlikesrose1:
    x "Я сказал ей, что она мне нравится."
    x "Может, она тоже начнёт喜欢我, если я проведу с ней больше времени...?"
    jump day6totallyover

label caronlikesrose2:
    x "Она мне правда нравится."
    x "Если я проведу с ней больше времени, может, она тоже начнёт喜欢我?"
    jump day6totallyover

label bestfriendswithrosenow:
    x "Думаю, мы теперь лучшие друзья."
    x "Это определённо даёт мне повод."
    jump day6totallyover

label hangoutwithrosemore:
    x "Но будет ли это нормально?"
    x "Надеюсь, я её не раздражаю."
    jump day6totallyover

label day6totallyover:
    x "У нас полно времени."
    x "Мои каникулы не закончатся ещё долго."
    x "С нетерпением жду, что принесёт завтрашний день."

    stop music fadeout 1.0
##################################################################
    #День 7#
    play music veldatheme
    scene bg bedroom with fade

    show velda angry with dissolve
    v "ВСТАВАЙ!"
    x "Беру свои слова обратно."
    c "Чёрт возьми."
    show velda nervous with dissolve
    v "Тьфу."
    show velda smile with dissolve
    v "Ты должен быть благодарен, что кто-то будит тебя по утрам."
    c "Какими бы счастливыми ни были бы парни от того, что милая девушка будит их по утрам, у меня это не вызывает восторга."
    c "Особенно учитывая, что ты только две из этих вещей."
    show velda angry with dissolve
    v "Заткнись!"
    c "Да пофиг."
    c "Я бы хотел одеться."
    show velda nervous with dissolve
    v "Да, да."
    show velda normal with dissolve
    v "Не заставляй её ждать."
    c "А?"
    show velda nervous with dissolve
    v "Роуз пришла тебя увидеть."
    c "О..."
    show velda angry with dissolve
    v "Так что пошевеливайся!"
    c "Понял!"
    stop music fadeout 1.0
    hide velda angry with dissolve
##################################################################

    play music rosetheme
    scene bg restaurant with fade

    show rose smile with dissolve
    r "Доброе утро, Карон."
    c "Д-Утро."
    hide rose smile with dissolve
    show gwen normal with dissolve
    g "Вы двое идёте на свидание?"
    c "Нет."
    show gwen nervous with dissolve
    g "О."
    c "Тебе нравится здесь бывать, да?"
    show gwen smile with dissolve
    g "Ага, потому что я вижу Вельду."
    show gwen nervous with dissolve
    g "Подождите."
    show gwen shock with dissolve
    g "Мне не нужно было это говорить!"
    show gwen nervous with dissolve
    g "Я умру!?"
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Тьфу."
    show velda normal with dissolve
    v "Ты не умрёшь."
    show velda frown with dissolve
    v "Карон, прекрати её пугать."
    c "Но я ничего не делал."
    hide velda frown with dissolve
    show rose normal with dissolve
    r "Здесь точно оживлённо."
    c "Ага."
    show rose smile with dissolve
    r "В общем, я хочу, чтобы ты пошёл со мной."
    c "Куда мы идём?"
    show rose normal with dissolve
    r "В детдом."
    show rose smile with dissolve
    r "Дети хотят тебя увидеть."
    c "А?"
    show rose normal with dissolve
    r "Я рассказала им о тебе."
    c "А."
    show rose smile with dissolve
    r "Ну?"

menu:

    "Пойти с ней":
        jump gowithrosetoorphanage

    "Я не хочу никуда идти":
        jump donotwanttogoanywhere

label gowithrosetoorphanage:
    $ rosepoints += 1
    c "Да, ладно."
    c "Пойду."
    show rose normal with dissolve
    r "Хорошо."
    hide rose normal with dissolve
    show velda smile with dissolve
    v "Давай, проваливай отсюда."
    c "Да, иду."
    hide velda smile with dissolve
    show rose smile with dissolve
    r "Пойдём."
    hide rose smile with dissolve
    jump orphanagescene

label donotwanttogoanywhere:
    $ rosebad += 1
    c "Я не особо хочу куда-то идти."
    show rose frown with dissolve
    r "...О."
    hide rose frown with dissolve
    show velda angry with dissolve
    v "Просто иди."
    show velda nervous with dissolve
    v "Чем меньше ты рядом, тем лучше."
    c "Ладно."
    hide velda nervous with dissolve
    show rose normal with dissolve
    r "Так ты правда пойдёшь?"
    c "Ага."
    show rose smile with dissolve
    r "Спасибо!"
    jump orphanagescene

##################################################################

label orphanagescene:

    play music snowydays
    scene bg orphanage
    x "Мы в детдоме."
    x "Я не знаю, чего ожидал."
    x "По крайней мере, место выглядит приличным."
    ug "Ты вернулась!"
    ub "Ты мне что-нибудь принесла?"
    ug "Не всё крутится вокруг тебя!"
    ub "Ты всё ещё жива!"
    x "Что это было за последнее...?"
    show rose smile with dissolve
    r "Ага, я вернулась."

    if confesstorose == True or admitlikerose == True:
        jump iscaronherbf
    elif rosebff == True:
        jump iscaronherbff
    else:
        jump caronisaguest

label iscaronherbf:
    ub "Эм..."
    ub "Это твой парень?"
    show rose normal with dissolve
    r "Нет, он не мой парень."
    show rose smile with dissolve
    r "Он просто друг."
    ub "О."
    x "Он разочарован...?"
    ug "Это нормально."
    ug "Это значит, что никто не заберёт тебя у нас!"
    x "А кто-то явно с облегчением..."
    hide rose smile with dissolve
    jump orphanagecontinue

label iscaronherbff:
    ug "Я думала, ты приведёшь девушку."
    show rose nervous with dissolve
    r "Я это говорила?"
    ug "Ты сказала, что приведёшь своего лучшего друга."
    show rose normal with dissolve
    r "Кто сказал, что лучший друг — это девушка?"
    c "Кто знает?"
    c "Может, я на самом деле всегда была девушкой."
    ug "Правда?"
    c "Нет, я шучу."
    ug "О..."
    x "Почему она звучит разочарованно..."
    hide rose normal with dissolve
    jump orphanagecontinue

label caronisaguest:
    ug "Это тот человек, которого ты обещала привести?"
    ub "Он выглядит тупо."
    ug "Это невежливо!"
    ub "Но это правда."
    show rose nervous with dissolve
    r "Даже если ты так думаешь, не стоит такое говорить."
    c "Эм, да."
    c "Пожалуйста, не надо."
    c "Это ранит мои чувства."
    ub "Не будь нюней!"
    ug "Том!"
    ub "Прости."
    hide rose nervous with dissolve
    jump orphanagecontinue

##################################################################

label orphanagecontinue:

    scene bg orphanage with fade
    w "Спасибо вам обоим, что пришли навестить детей."
    c "А, не проблема."
    w "И Роуз, ты всегда помогаешь."
    show rose smile with dissolve
    r "Я делаю это, потому что хочу."
    w "Знаю."
    c "Так зачем я был нужен?"
    w "Ты здесь, чтобы развлечь детей."
    w "Думаешь, справишься?"
    c "Эм, наверное."
    w "Решай сам, что будешь делать."
    c "Эм... ладно..."

menu:

    "Рассказать шутки":
        jump telljokestothekids

    "Попробовать жонглировать":
        jump attemptjuggleforkids

    "Устроить спектакль":
        jump putonaplayforkids

    "Почитать им сказку":
        jump readstoryforkids

label telljokestothekids:
    c "Почему бы мне не рассказать им шутки?"
    c "Я довольно уверен в своём чувстве юмора."
    w "Ладно."
    hide rose smile with dissolve
    stop music fadeout 1.0
##################################################################

    play music energetickids
    scene bg orphanage with fade
    c "Итак... эм?"
    c "Хотите послушать историю?"
    ub "Почему бы тебе не сделать десять и не прыгнуть?"
    c "Эй, я тут шутки рассказываю."
    c "Так... ээ..."
    c "Почему курица перешла дорогу?"
    ub "Чтобы убраться от тебя?"
    ug "Перестань!"
    ug "Он старается..."
    ub "Ага, старается сосать!"
    c "Уф, это катастрофа."
    ub "Как и твоя личная жизнь!"
    ug "Прекрати!"
    x "Я с трудом рассказываю детям шутки."
    x "В конце концов все больше смеются над выходками мальчика."
    $ achievement.grant("Joke_Attempt")
    stop music fadeout 1.0
    jump entertainedkids

label attemptjuggleforkids:
    c "Я могу попробовать жонглировать."
    w "Ты умеешь жонглировать?"
    c "Я могу попробовать."
    w "Ну ладно..."
    stop music fadeout 1.0
##################################################################

    play music happyperson
    scene bg orphanage with fade
    c "Я собираюсь жонглировать."
    x "Подбрасываю мячи в воздух."
    x "Сначала всё идёт нормально."
    x "Но это длилось лишь несколько секунд."
    ub "Ты в этом ужасен!"
    c "Попробую ещё раз."
    x "Подбираю мячи и пробую снова."
    x "Роняю их."
    ub "Что за неудачник!"
    c "Я стараюсь."
    ub "Сосать?"
    ug "Не будь таким!"
    x "У меня плохо получается жонглировать."
    x "В конце концов все смеются над оскорблениями мальчика."
    $ achievement.grant("Juggle_Attempt")
    stop music fadeout 1.0
    jump entertainedkids

label putonaplayforkids:
    c "Давайте устроим спектакль."
    show rose normal with dissolve
    r "Ты умеешь играть?"
    c "Может быть?"
    w "Думаю, у нас не так много реквизита."
    c "Это нормально."
    hide rose normal with dissolve
    stop music fadeout 1.0
##################################################################

    play music timetowork

    x "Мы с Роуз устраиваем спектакль для детей."
    x "К сожалению, у нас не было много времени на репетиции."
    x "Это история о рыцаре и принцессе в приключении."
    x "Они на пути к победе над драконом, который украл сокровища из замка."
    x "Я бегаю по сцене как идиот."
    x "Роуз просто подыгрывает, но не думаю, что дети понимают, что происходит."
    x "Они, кажется, в замешательстве."
    x "В конце концов история завершается: мы побеждаем дракона, возвращаем сокровища, и дракон теперь добрый."
    ub "Это было отстойно!"
    ug "Что ты говоришь?"
    ug "Мне понравилось!"
    ub "Мне тоже не понравилось."
    $ achievement.grant("Play_Attempt")
    x "Спектакль получил неоднозначные отзывы."
    stop music fadeout 1.0
    jump entertainedkids

label readstoryforkids:
    c "Я могу почитать им сказку."
    w "У нас полно книг."
    c "Возьму что-нибудь интересное."
    stop music fadeout 1.0
##################################################################

    play music thingsareokay
    scene bg orphanage with fade
    x "Я взял книгу про пиратов."
    x "Они встретили принцессу в приключении."
    x "Однако они столкнулись с её стражей, которые решили, что пираты её похитили."
    x "В итоге они убегают, забрав принцессу с собой."
    x "Принцесса пыталась объяснить недоразумение, но они не слушали."
    x "Из-за этого она путешествует по миру с пиратами."
    x "Её родители отправляют героя на её поиски, который в итоге сражается с пиратами."
    x "Она пытается объяснить недоразумение, и в конце концов он узнаёт о настоящих намерениях пиратов."
    x "В итоге принцесса влюбляется в главного пирата, и они живут долго и счастливо."
    ub "Фу! У пирата теперь заразы!"
    ug "Это была хорошая история..."
    ub "Целоваться — это мерзко."
    ug "Мне не нравятся пираты."
    x "Похоже, не всем понравилось."
    $ achievement.grant("Story_Attempt")
    x "Половине детей понравилось, другой половине — нет."
    stop music fadeout 1.0
    jump entertainedkids

##################################################################

label entertainedkids:

    play music normalday
    scene bg orphanage with fade
    w "Спасибо, что развлёк их."
    c "Без проблем."
    c "Правда, всё прошло не так, как хотелось бы."
    show rose nervous with dissolve
    r "Не будь к себе так строг."
    show rose normal with dissolve
    r "Ничто не идеально."
    c "Верно."
    w "Ещё раз спасибо за всё."
    show rose smile with dissolve
    r "Без проблем."
    show rose normal with dissolve
    r "Я всегда рада помочь."
    w "И Карон, можешь приходить в любое время."
    c "Я учту."
    w "Уже поздно, так что вам двоим лучше идти домой."
    c "Ладно."
    hide rose normal with dissolve
##################################################################
    scene bg street evening with fade
    show rose normal with dissolve
    r "Ты хорошо провёл время?"
    c "Настолько хорошо, насколько можно, когда дети меня оскорбляют."
    show rose smile with dissolve
    r "Не все так делали."
    c "Знаю."
    stop music fadeout 1.0
    show rose nervous with dissolve
    r "Можно тебе кое-что рассказать?"
    c "Что?"

    play music sadpast

    show rose frown with dissolve
    r "Это о... моём прошлом."
    show rose normal with dissolve
    r "У меня есть младшая сестра."
    show rose nervous with dissolve
    r "Или, наверное, правильнее сказать... была?"
    c "Была?"
    c "Она...?"
    show rose smile with dissolve
    r "Она всё ещё жива."
    c "Тогда что случилось?"
    show rose nervous with dissolve
    r "Когда мы были маленькими, мою сестру и меня отдали в систему опеки."
    show rose frown with dissolve
    r "Но по какой-то причине они никогда не позволяли нам быть вместе."
    show rose nervous with dissolve
    r "Несмотря на то, что мы сёстры, нас разлучили."
    show rose normal with dissolve
    r "Однажды меня удочерили."
    show rose nervous with dissolve
    r "Но... взяли только меня."
    show rose frown with dissolve
    r "Мне пришлось оставить сестру."
    c "Они знали?"
    x "Роуз покачала головой."
    show rose nervous with dissolve
    r "Нас к тому моменту уже разлучили."
    c "Понятно."
    show rose normal with dissolve
    r "Конечно, мне было грустно, но я ничего не могла поделать."
    show rose nervous with dissolve
    r "Последний раз, когда я слышала, моя сестра всё ещё была в системе опеки."
    show rose frown with dissolve
    r "Я... не знаю, что с ней случилось."
    show rose nervous with dissolve
    r "Возможно, я никогда её больше не увижу."
    c "Что ж, это печально."
    show rose frown with dissolve
    r "Я скучаю по ней."
    show rose normal with dissolve
    r "Однако она, наверное, меня не помнит."
    show rose nervous with dissolve
    r "Она ещё была младенцем, когда я видела её в последний раз."
    c "Так ты намного старше."
    show rose normal with dissolve
    r "Да..."
    c "Зачем ты мне всё это рассказала?"

    if rosebff == True:
        jump becausewearebestfriendsrose
    else:
        jump becausewearefriends

label becausewearebestfriendsrose:
    show rose smile with dissolve
    r "Потому что ты мой лучший друг."
    show rose normal with dissolve
    r "Ты имеешь право знать."
    jump roseanswerscaron

label becausewearefriends:
    show rose smile with dissolve
    r "Потому что мы друзья."
    show rose normal with dissolve
    r "Друзья разговаривают о таких вещах."
    jump roseanswerscaron

label roseanswerscaron:
    c "Понятно."
    stop music fadeout 1.0
    show rose smile with dissolve
    r "Что ж, я пойду домой."
    c "А, да."
    c "Увидимся позже."
    hide rose smile with dissolve
##################################################################

# День 8 #

    scene bg bedroom with fade
    c "Ты занята?"
    r "Ага, прости."
    r "Поговорим позже, ладно?"
    x "Она вешает трубку, и я кладу телефон."
    c "Значит, она занята, да?"

##################################################################

    play music neverendingproblems
    scene bg restaurant with fade
    show velda nervous with dissolve
    v "Что это за выражение лица?"
    c "Роуз не хочет гулять."
    show velda smile with dissolve
    v "Может, ты ей больше не нравишься..."
    c "Она сказала, что занята."
    hide velda smile with dissolve
    show gwen normal with dissolve
    g "Наверное, так и есть."
    c "Ты здесь?"
    show gwen smile with dissolve
    g "Я всегда здесь."
    show gwen normal with dissolve
    g "Обычно."
    hide gwen normarl with dissolve
    show velda normal with dissolve
    v "Так почему нас это должно волновать?"
    c "Что мне делать сегодня?"
    show velda nervous with dissolve
    v "Мне плевать."
    d "Ты мог бы поработать..."
    c "Я думал, начинаю только после обеда...?"
    d "Ты всегда можешь прийти пораньше..."
    c "Наверное."
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Ты переживаешь за неё?"
    c "Может быть..."
    show gwen normal with dissolve
    g "Что ж, почему бы тебе не сходить в места, где она обычно бывает?"
    c "На самом деле, неплохая идея."
    hide gwen normal with dissolve
    show velda angry with dissolve
    v "Тогда проваливай отсюда!"
    c "Верно."
    hide velda angry with dissolve

menu:

    "Пойти в больницу":
        jump hospitalday8

    "Пойти в детдом":
        jump orphanageday8

label hospitalday8:
    $ checkhospital = True
    x "Попробую больницу."
##################################################################

    scene bg hospital waiting with fade
    c "Роуз... здесь?"
    w "Она ушла какое-то время назад."
    c "Чёрт."
    c "Ты не знаешь, куда она пошла?"
    w "Нет."
    c "Ладно."
    c "Прости, что отнял время."
    w "Не переживай."

    if checkhospital and checkorphanage == True:
        jump checkedbothplaces
    else:
        jump orphanageday8

label orphanageday8:
    $ checkorphanage = True
    x "Может, она в детдоме..."
##################################################################
    scene bg orphanage with fade
    c "Роуз сегодня заходила?"
    w "Ты только что её пропустил."
    c "Чёрт."
    c "Она не говорила, куда идёт?"
    w "Нет."
    c "Понятно."
    c "Прости, что побеспокоил."
    w "Всё в порядке."

    if checkhospital and checkorphanage == True:
        jump checkedbothplaces
    else:
        jump hospitalday8

##################################################################

label checkedbothplaces:

    stop music fadeout 1.0
    scene bg restaurant with fade
    d "Не смог её найти?"
    c "Нет."
    d "Понятно."
    c "Я бы хотел начать работать сейчас."
    d "Ладно."
##################################################################
    scene bg restaurant with fade
    x "Время закрытия."
    c "Я пойду ненадолго."
    d "Не задерживайся допоздна."
    c "Не буду."
##################################################################
    scene bg park 2 night with fade
    x "С руками в карманах, я иду в сторону парка."
    x "Что-то привлекает моё внимание."
    x "Это Роуз, и она собирает мусор."
    play sound running
    x "Я быстро подбегаю к ней."
    stop sound fadeout 1.0
    play music discomfort
    show rose nervous with dissolve
    r "Карон?"
    c "Я искал тебя повсюду."
    show rose normal with dissolve
    r "Правда?"
    show rose nervous with dissolve
    r "Я же говорила, что буду занята сегодня, нет?"
    c "Да, но... я мог бы помочь..."
    show rose normal with dissolve
    r "У тебя же есть ресторан дяди, разве нет?"
    c "Ну, да, но..."
    show rose smile with dissolve
    r "Я просто не хочу взваливать на тебя ещё больше."

menu:

    "Не будь идиоткой":
        jump dontbeidiotrose

    "Я переживал за тебя":
        jump worryaboutrose

    "Как дела?":
        jump howisitgoing

label dontbeidiotrose:
    $ rosebad += 1
    c "Не будь идиоткой."
    show rose frown with dissolve
    r "Карон?"
    c "Я хочу помочь тебе."
    show rose normal with dissolve
    r "Спасибо... но я не хочу просить у тебя слишком многого."
    c "Это не было бы слишком много!"
    c "Это правда так, или ты просто думаешь, что я не справлюсь?!"
    show rose nervous with dissolve
    r "Я этого не говорила..."
    show rose frown with dissolve
    r "Ты злишься, да?"
    c "Ещё как."
    show rose nervous with dissolve
    r "Прости..."
    c "Да пофиг."
    jump roseparkday8scene

label worryaboutrose:
    $ rosepoints += 1
    c "Я переживал за тебя."
    show rose normal with dissolve
    r "Ты переживал за меня?"

    if rosebff == True:
        jump worryaboutrosebff
    elif confesstorose == True:
        jump worryaboutrosecrush
    else:
        jump worryaboutrosefriend

label worryaboutrosebff:
    c "Конечно, я бы переживал за своего лучшего друга."
    show rose smile with dissolve
    r "Карон..."
    jump worryaboutrose2

label worryaboutrosecrush:
    c "Почему бы мне не переживать за девушку, которая мне нравится?"
    show rose embarassed with dissolve
    r "К-Карон..."
    jump worryaboutrose2

label worryaboutrosefriend:
    c "Мы друзья."
    c "Конечно, я бы переживал за тебя."
    jump worryaboutrose2

label worryaboutrose2:
    show rose smile with dissolve
    r "Эм... спасибо."
    show rose nervous with dissolve
    r "Я рада, что тебе не всё равно."
    c "Пожалуйста, не делай так больше."
    c "Ты всегда можешь попросить у меня помощь."
    show rose normal with dissolve
    r "Ага."
    show rose smile with dissolve
    r "В следующий раз так и сделаю."
    c "Хорошо."
    jump roseparkday8scene

label howisitgoing:
    c "Так как твоя работа?"
    show rose normal with dissolve
    r "Всё идёт нормально."
    c "Понятно."
    c "Не перетруждайся."
    show rose smile with dissolve
    r "Я буду в порядке."
    c "Помни, ты всегда можешь попросить у меня помощь."
    show rose nervous with dissolve
    r "Я знаю..."
    c "Пожалуйста, попроси в следующий раз."
    show rose normal with dissolve
    r "Х-Хорошо."
    show rose smile with dissolve
    r "Спасибо, что проверил."
    c "Без проблем."
    jump roseparkday8scene

label roseparkday8scene:

    stop music fadeout 1.0

    show rose normal with dissolve
    r "..."
    c "Роуз?"
    play sound thudhard
    hide rose normal with dissolve
    x "Она упала!"
    c "Роуз!"
    x "Чёрт."
    x "Я подбегаю, чтобы подхватить её."
    x "Она без сознания."
##################################################################

# День 9 #

    scene bg hospital waiting with dissolve
    x "Вчера Роуз перетрудилась."
    x "Истощение привело к обмороку."
    x "Сейчас я в больнице, жду, чтобы её увидеть."
    do "Карон?"
    c "Это я."
    do "Она хочет тебя видеть."
    c "Хорошо."
#################################################################

    play music worryaboutyou
    scene bg hospital room day with fade
    c "После того, что случилось вчера, я РЕАЛЬНО не хочу, чтобы ты снова так делала."
    show rose nervous with dissolve
    r "Думаешь, я перестаралась?"
    c "Учитывая, что ты упала в обморок — да."
    show rose frown with dissolve
    r "Прости."
    c "Я буду очень расстроен, если ты снова такое выкинешь."
    show rose nervous with dissolve
    r "Я уже сказала, что прости."
    c "П-Прости."
    show rose normal with dissolve
    r "Теперь уже ТЫ извиняешься."
    c "Прости, что переживал за тебя!"
    show rose nervous with dissolve
    r "Эм..."
    show rose nervous with dissolve
    r "Можешь успокоиться?"
    c "Я СПОКОЕН!"
    do "Пациент за стеной жалуется на шум."
    hide rose nervous with dissolve
    show gwen nervous with dissolve
    g "Можете потише? Мой брат-"
    show gwen shock with dissolve
    g "Карон?"
    c "Что ТЫ тут делаешь?"
    show gwen normal with dissolve
    g "Навещаю кое-кого."
    hide gwen normal with dissolve
    show rose normal with dissolve
    r "Привет."
    hide rose normal with dissolve
    show gwen normal with dissolve
    g "Что случилось?"
    hide gwen normal with dissolve
    show rose nervous with dissolve
    r "Вчера, наверное, слишком перетрудилась."
    hide rose nervous with dissolve
    show gwen nervous with dissolve
    g "Знаешь, тебе стоит иногда отдыхать, да?"
    hide gwen nervous with dissolve
    show rose normal with dissolve
    r "Да, наверное, стоит."
    hide rose normal with dissolve
    c "Я... пойду на улицу."
    show gwen normal with dissolve
    g "О."
    hide gwen normal with dissolve
#################################################################

    stop music fadeout 1.0
    scene bg park 2 day with fade
    x "Я снова в том парке."
    x "Мне нравится это место или что?"
    x "Я вздыхаю."

menu:

    "Мне стоит успокоиться":
        jump shouldcalmdown

    "Я всё ещё злюсь":
        jump amstillpissed

label shouldcalmdown:
    x "Мне правда стоит успокоиться."
    jump parkday9scene

label amstillpissed:
    $ rosebad += 1
    x "Я всё ещё злюсь."
    jump parkday9scene

label parkday9scene:
    x "Я снова вздыхаю."
    ug "Привет."
    c "А?"
    play music struggletomoveon
    ug "Что ты делаешь один, дяденька?"
    c "О, я немного расстроился."
    c "Думал, прийти сюда поможет мне успокоиться."
    c "Не очень-то работает."
    x "Эта девочка выглядит знакомо."
    ug "Я хотела поблагодарить тебя и ту добрую тётю."
    ug "Ты её потерял?"
    c "А, не совсем."
    ug "А, хорошо."
    ug "Грустно, когда теряешь кого-то."
    c "Ты когда-нибудь теряла кого-то?"
    ug "Ага."
    ug "У меня была сестра."
    ug "Но... злые люди разлучили нас."
    ug "Однажды мою сестру удочерили, и я её больше не видела."
    ug "Мне пришлось долго ждать своей очереди."
    x "Подожди-ка."
    x "Это звучит очень знакомо."
    x "Это точно совпадение, да?"
    c "О."
    c "Что ж, я скажу Роуз, что ты хотела её увидеть."
    ug "Ладно."
    ug "О чём-то думаешь?"
    ug "О чём ты думаешь?"
    c "О, Роуз говорила, что её тоже удочерили."
    c "Ты просто напомнила мне об этом."
    ug "О..."
    ug "Что ж, передай ей от меня привет."

    stop music fadeout 1.0

    x "После этого девочка убегает."
    x "Я снова вздыхаю."
    x "Это невозможно..."
    x "Такое совпадение было бы слишком идеальным, не так ли?"
#################################################################
    scene bg restaurant with fade
    c "Я готов работать."
    show velda normal with dissolve
    v "Это редкость."
    c "Не груби."
    hide velda normal with dissolve
    d "Ты немного рано."
    c "Да, ну..."
    c "Я просто возьмусь за работу."
#################################################################

# День 10 #

    if rosebad >= 7:
        jump rosebadendingday10
    else:
        jump rosenormalday10

label rosebadendingday10:
    scene bg bedroom with fade
    show velda nervous with dissolve
    v "..."
    c "Что?"
    show velda frown with dissolve
    v "..."
    c "ЧТО?!"
    play music badfeeling
    show velda nervous with dissolve
    v "Она мертва."
    c "Кто?"
    show velda frown with dissolve
    v "Роуз."
    c "Что?"
    c "Что, чёрт возьми, случилось?!"
    show velda nervous with dissolve
    v "Что ж..."
    show velda normal with dissolve
    v "После того как её выписали из больницы, она вернулась помогать людям."
    show velda nervous with dissolve
    v "И один из детей из детдома убежал..."
    show velda frown with dissolve
    v "Он зашёл слишком далеко и столкнулся с бандой."
    show velda nervous with dissolve
    v "Они попытались причинить ему вред, и Роуз их нашла."
    show velda frown with dissolve
    v "Для неё всё закончилось плохо."
    c "Она пыталась с ними драться?"
    show velda normal with dissolve
    v "Не знаю."
    show velda nervous with dissolve
    v "Но... это они забрали её жизнь."
    show velda frown with dissolve
    v "А, и ребёнок тоже мёртв."
    c "..."
    show velda nervous with dissolve
    v "Прости, что тебе пришлось просыпаться с такой новостью."
    hide velda nervous with dissolve
    x "Вельда затем выходит из моей комнаты."
    x "Я просто сижу в кровати, не зная, как реагировать."
    x "Мой друг мёртв."
    x "Это и правда были паршивые каникулы."
    stop music fadeout 1.0
    $ achievement.grant("Rose_Dead")
    x "ХУДШАЯ КОНЦОВКА — РОУЗ УМИРАЕТ"
    # Титры плохой концовки
    $ renpy.movie_cutscene("video/BadCredits.webm", delay=95, loops=0, stop_music=True)
    return

label rosenormalday10:

    play music rosetheme
    scene bg restaurant with fade
    show rose nervous with dissolve
    r "Мне так жаль!"
    c "О, правда?"
    show rose normal with dissolve
    r "Правда."
    show rose nervous with dissolve
    r "Мне не следовало делать всё это в одиночку."
    c "По крайней мере, ты сейчас в порядке."
    show rose smile with dissolve
    r "Ага."
    show rose nervous with dissolve
    r "Эм, Карон?"
    c "Да?"
    show rose normal with dissolve
    r "Пойдём со мной."
    show rose smile with dissolve
    r "Есть кое-что, о чём я хочу поговорить."
    c "Х-Хорошо."
    stop music fadeout 1.0
    hide rose smile with dissolve
#################################################################
    scene bg park 2 day with fade
    x "Опять этот парк."
    c "Так что ты хотела?"
    ug "Ты здесь!"
    c "О, привет."
    ug "Эм..."

    play music memories

    ug "Ты моя сестра?"
    show rose nervous with dissolve
    r "Что?"
    ug "Ну, этот дядька сказал, что тебя тоже удочерили."
    ug "Я подумала, может, ты моя сестра, которую я не видела много лет."
    show rose shock with dissolve
    r "..."
    ug "Ну, ты?"
    show rose nervous with dissolve #любопытство
    r "Мари?"
    ug "Ты помнишь моё имя...!"
    x "Значит, они правда..."
    ma "Роуз!"
    x "Мари подбежала к Роуз и начала её обнимать."
    show rose normal with dissolve
    r "Не могу поверить."
    show rose smile with dissolve
    r "Ты была не так уж далеко."
    show rose normal with dissolve
    r "Я так рада..."
    ma "Теперь мы снова сможем играть..."
    show rose smile with dissolve
    r "Ага..."
    ma "Что ж, мне пора."
    ma "Мама и Папа сказали, что у меня только полчаса здесь."
    ma "Кажется, моё время почти вышло."
    show rose normal with dissolve
    r "Ладно."
    x "Две сестры отпускают друг друга."
    ma "Увидимся позже!"
    play sound running
    x "И затем Мари убегает."
    stop sound fadeout 1.0
    c "Честно, удивлён, что это было не просто совпадение."
    c "Ты в порядке?"
    show rose normal with dissolve
    r "Да, я в порядке."
    stop music fadeout 1.0
    show rose nervous with dissolve
    r "Эм..."
    show rose normal with dissolve
    r "Чувствую себя немного странно, говоря об этом, но... именно поэтому я привела тебя сюда."

    if rosepoints >= 12:
        jump roseconfessonday10
    else:
        jump rosefriendshipday10

label roseconfessonday10:

    if confesstorose == True:
        jump roseconfessresponseday10
    else:
        jump roseconfesstocaronday10

label roseconfessresponseday10:
    show rose nervous with dissolve
    r "Я хочу, чтобы ты знал..."
    play music loveconfess
    show rose embarassed with dissolve
    r "Ты мне тоже нравишься!"
    jump roseconfessonday10part2

label roseconfesstocaronday10:
    show rose nervous with dissolve
    r "Я хотела тебе сказать..."
    play music loveconfess
    show rose embarassed with dissolve
    r "Ты мне правда нравишься!"
    jump roseconfessonday10part2

label roseconfessonday10part2:

    c "Правда?"
    show rose normal with dissolve
    r "Ага."
    show rose smile with dissolve
    r "Я недавно поняла, что чувствую."
    show rose normal with dissolve
    r "Мне правда нравится быть с тобой."
    show rose smile with dissolve
    r "И я всегда думаю о тебе."
    c "Честно, у меня так же."
    c "Я всегда переживал за тебя."
    c "Прежде чем я это осознал, я захотел, чтобы мы были больше, чем друзья."
    show rose normal with dissolve
    r "Что ж, почему бы нам не начать?"
    c "Ага."
    c "Звучит хорошо."
    play sound kiss
    x "Роуз наклоняется и целует меня в лоб."
    show rose embarassed with dissolve
    r "Как тебе?"
    c "Немного неловко."
    show rose smile with dissolve
    r "Что ж, привыкай."
    x "Вот так я и получил девушку на каникулах."
    x "Я стал счастливее, чем когда-либо."
    stop music fadeout 1.0
    $ persistent.roseromanceclear = True
    $ achievement.grant("Rose_Romance")
    x "РОМАНТИЧЕСКАЯ КОНЦОВКА — РОУЗ"
    $ renpy.movie_cutscene("video/LoveCredits.webm", delay=69, loops=0, stop_music=True)
    return

label rosefriendshipday10:

    if confesstorose == True:
        jump rosefriendzoneday10
    elif rosebff == True:
        jump rosebestfriendday10
    else:
        jump finalrosefriendsday10

label rosefriendzoneday10:
    show rose nervous with dissolve
    r "Я чувствую не так, как ты."
    c "О."
    play music friendship
    show rose normal with dissolve
    r "Но я бы хотела быть друзьями."
    show rose smile with dissolve
    r "Это нормально?"
    c "Ага."
    jump finalrosefriendsday10part2

label rosebestfriendday10:
    play music friendship
    show rose smile with dissolve
    r "Ты лучший друг, который у меня когда-либо был."
    c "Правда?"
    show rose normal with dissolve
    r "Ага."
    show rose smile with dissolve
    r "Спасибо, что всегда рядом."
    jump finalrosefriendsday10part2

label finalrosefriendsday10:
    play music friendship
    show rose normal with dissolve
    r "Я рада, что мы друзья."
    c "Я тоже."
    show rose smile with dissolve
    r "Надеюсь, ты останешься со мной."
    c "Планирую."
    jump finalrosefriendsday10part2

label finalrosefriendsday10part2:

    show rose normal with dissolve
    r "Я всегда буду рада, что встретила тебя."
    c "Я чувствую то же самое."
    show rose smile with dissolve
    r "Что ж, что нам теперь делать?"
    c "Не знаю."
    c "Что ты хочешь делать?"
    show rose nervous with dissolve
    r "Не знаю."
    show rose normal with dissolve
    r "Что ТЫ хочешь делать?"
    c "Не знаю."
    c "Что ТЫ хочешь делать?"
    show rose nervous with dissolve
    r "Мы не обязаны делать это вечно, знаешь?"
    c "Знаю."
    x "И вот так, я с нетерпением ждал, чтобы провести остаток каникул со своим лучшим другом."
    x "Оба мы хотели, чтобы эти моменты длились вечно."
    stop music fadeout 1.0
    $ persistent.rosefriendshipclear = True
    $ achievement.grant("Rose_Friendship")
    x "КОНЦОВКА ДРУЖБЫ — РОУЗ"
    # Титры концовки дружбы
    $ renpy.movie_cutscene("video/FriendCredits.webm", delay=85, loops=0, stop_music=True)
    return
