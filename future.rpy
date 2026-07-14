label futureroutestart:

    play music magic
    scene bg white with fade
    x "Я просыпаюсь в полностью белом пространстве."
    d "Где я…?"
    show velda normal with dissolve
    v "Мир снов закончился."
    d "А, точно."
    d "Так когда мы вернёмся домой?"
    hide velda normal with dissolve
    show gwen nervous with dissolve
    g "Мне страшно…"
    hide gwen nervous with dissolve
    show rose nervous with dissolve
    r "Мы ведь ничего не испортили?"
    hide rose nervous with dissolve
    show rin smile with dissolve
    ri "С вами всеми всё будет хорошо."
    hide rin smile with dissolve
    show velda shock with dissolve
    v "Это ты!"
    hide velda shock with dissolve
    show rose normal with dissolve
    r "Что мы делаем снова здесь?"
    hide rose normal with dissolve
    show rin normal with dissolve
    ri "Что ж, мне нужно отправить вас обратно в ваш старый мир."
    hide rin normal with dissolve
    show velda normal with dissolve
    v "Значит, это было действительно всё, да?"
    hide velda normal with dissolve
    show rin normal with dissolve
    ri "Вы не можете по-настоящему изменить реальность."
    show rin frown with dissolve
    ri "По крайней мере, не легко."
    d "Не легко, значит…?"
    hide rin frown with dissolve
    show velda normal with dissolve
    v "Подожди…"
    show velda nervous with dissolve
    v "Ты ведь не думаешь о том, о чём я думаю, что ты думаешь?"
    d "Может быть, думаю, а может быть, нет…"
    hide velda nervous with dissolve
    show rin normal with dissolve
    ri "Хочешь попробовать?"
    d "Может быть…"
    hide rin normal with dissolve
    show gwen nervous with dissolve
    g "Я не знаю."
    hide gwen nervous with dissolve
    show rose nervous with dissolve
    r "Это правда хорошая идея?"
    hide rose nervous with dissolve
    show velda normal with dissolve
    v "Да ладно."
    show velda nervous with dissolve
    v "Нам не обязательно это делать…"

menu:

    "Давайте попробуем":
        jump letustryfuture

    "Не стоит":
        jump donottryfuture

label donottryfuture:
    d "Ты права."
    d "Нам действительно не нужно этого делать."
    d "Возможно, это всё равно невозможно."
    hide velda nervous with dissolve
    show rin normal with dissolve
    ri "Значит, ты собираешься просто вернуться к тому, как всё было?"
    d "Да…"
    d "Спасибо за всё."
    show rin smile with dissolve
    ri "Я просто делаю свою работу."
    x "И вот так… нас отправили обратно в ту временную линию, где Карон мёртв."
    x "А потом… мы просто продолжили жить своей жизнью."
    $ achievement.grant("Gave_Up")
    x "КОНЕЦ — СДАЧА"
    stop music fadeout 1.0
    $ renpy.movie_cutscene("video/NeutralCredits.webm", delay=100, loops=0, stop_music=True)
    #Нейтральные титры
    return

label letustryfuture:
    d "Я хочу попробовать."
    d "Если есть способ спасти Карона, я должен попытаться."
    show velda smile with dissolve
    v "Что ж, если ты идёшь, я тоже пойду."
    hide velda smile with dissolve
    show gwen normal with dissolve
    g "Я-Я тоже."
    hide gwen normal with dissolve
    show rose nervous with dissolve
    r "Я не хочу, чтобы вы все бросили меня."
    hide rose nervous with dissolve
    show rin normal with dissolve
    ri "Значит, вы правда планируете это сделать…?"
    d "Ага!"
    show rin smile with dissolve
    ri "Что ж, ладно."
    show rin normal with dissolve
    ri "Но у вас только один шанс."
    d "Понял."
    play sound teleport
    stop music fadeout 1.0
    hide rin normal with dissolve
##################################################################

    play music neverendingproblems
    scene bg mystery sky with fade
    x "Нас отправили обратно в те зимние каникулы."
    x "Карон пришёл как обычно, представился Вельде, а потом и мне."
    x "Он вышел на улицу и встретил Роуз и Гвен."
    x "Потом он проводил время в ресторане или гулял с девочками на улице."
    x "Мы не стали перезапускать мир."
    x "У нас был только один шанс, в конце концов."
    x "Не успели мы оглянуться, как наступил день автомобильной аварии."
    scene bg intersection with fade
    x "Все мы бегали вокруг, разыскивая Карона."
    x "А потом… мы увидели, как он переходит дорогу."
    x "Он не делал ничего плохого… но…"
    x "Чёрт. Машина приближается."
    show velda shock with dissolve
    v "Карон…!"
    hide velda shock with dissolve
    show gwen shock with dissolve
    g "Д-Двигайся!"
    hide gwen shock with dissolve
    show rose angry with dissolve
    r "Уйди с дороги!"
    hide rose angry with dissolve
    x "Похоже, он нас не слышал."
    x "Машина подъехала к нему ближе, и тогда-"
    x "Я прыгнул."
    x "Я двигался, не думая."
    x "Я оттолкнул его-"
    x "И тогда-"
    play sound carcrash
    x "Машина переехала мне ноги."
    play sound scream
    x "Я закричал от боли."
    stop sound fadeout 1.0
    x "А потом потерял сознание."
##################################################################

    stop music fadeout 1.0
    play music happyending

    scene bg hospital room day with fade
    x "Я очнулся в больнице."
    show velda frown with dissolve
    v "Ты что, пытался покончить с собой?"
    d "Нет…"
    show velda angry with dissolve
    v "Мы пытались спасти его. А не подставить кого-то другого!"
    d "Прости."
    d "Но я же не умер…"
    show velda normal with dissolve
    v "Допустим."
    show velda smile with dissolve
    v "Боже, ты такой дурак…"
    d "Прости."
    show velda nervous with dissolve
    v "Хватит извиняться."
    hide velda nervous with dissolve
    show gwen shock with dissolve
    g "О Боже!"
    show gwen normal with dissolve
    g "Он не умер!"
    d "Не то чтобы я так легко умер."
    hide gwen normal with dissolve
    show rose smile with dissolve
    r "Мы просто рады, что ты в порядке."
    hide rose smile with dissolve
    c "Чёрт."
    c "Кто бы управлял твоим рестораном, если бы ты умер?"
    d "Наверное, заставил бы тебя."
    c "Ой, да ладно."
    c "Я недостаточно ответственный."
    x "Я слабо рассмеялся."
    d "Я просто рад, что ты не пострадал."
    c "Благодаря тебе."
    stop music fadeout 1.0
    play music bittersweet
    c "Но… почему?"
    d "Мы семья."
    d "А почему бы и нет?"
    c "Я не это имел в виду."
    show velda normal with dissolve
    v "Тогда что ты имел в виду?"
    c "Почему вы все вернулись ради меня?"
    c "Я же должен был…"
    x "У Карона на глазах появились слёзы."
    hide velda normal with dissolve
    show rose normal with dissolve
    r "Мы знаем."
    x "Девушки подошли к Карону и обняли его."
    c "..."
    hide rose normal with dissolve
    show gwen smile with dissolve
    g "Мы просто не хотели жить в мире без тебя."
    c "Это нечестно…"
    show gwen nervous with dissolve
    g "Нет, ТЫ нечестный…"
    hide gwen nervous with dissolve
    show velda smile with dissolve
    v "Собственно говоря, мы мстим тебе за то, что было раньше."
    c "Но… это ломает то, как всё должно быть."
    d "Разве это правда важно?"
    d "Пока ты здесь…"
    c "Ребята…"
    c "...Спасибо."
    hide velda smile with dissolve
    stop music fadeout 1.0
##################################################################

    play sound teleport
    scene bg white with fade
    play music miracle
    show rin normal with dissolve
    ri "Ты теперь доволен?"
    d "Да."
    show rin frown with dissolve
    ri "Я удивлена."
    show rin normal with dissolve
    ri "Я не думала, что ты действительно это сделаешь."
    d "Ты ведь никогда в меня не верила, да?"
    show rin frown with dissolve
    ri "Что ты имеешь в виду?"
    hide rin frown with dissolve
    show rose shock with dissolve
    r "Вы двое встречались раньше?"
    d "Спасибо за то, что ты сделала… Мам."
    eve "...!"
    hide rose normal with dissolve
    show rin normal with dissolve
    ri "Значит, ты знал, кто я…?"
    d "Да."
    show rin smile with dissolve
    ri "Хех."
    show rin normal with dissolve
    ri "Я сделала это не ради тебя."
    show rin smile with dissolve
    ri "Я сделала это ради моего внука."
    d "Да-да, я знаю."
    d "Я понимаю."
    hide rin smile with dissolve
    show gwen nervous with dissolve
    g "Ты не выглядишь такой старой."
    hide gwen nervous with dissolve
    show rin normal with dissolve
    ri "Это потому что я приняла облик своей молодой версии."
    show rin smile with dissolve
    ri "Позаботься о Кароне."
    show rin frown with dissolve
    ri "Я буду наблюдать за всеми вами."
    show rin smile with dissolve
    ri "Всегда наблюдать."
    d "Тебе правда не обязательно было делать это жутко."
    hide rin smile with dissolve
    show velda frown with dissolve
    v "Эта семья что, полна психов?"
    hide velda frown with dissolve
    show rin frown with dissolve
    ri "Осторожнее."
    show rin smile with dissolve
    ri "А то могу тебя проклясть."
    hide rin smile with dissolve
    show velda nervous with dissolve
    v "Я-Я молчу."
    hide velda nervous with dissolve
    show rin normal with dissolve
    ri "Я отправлю вас всех обратно в ваше настоящее."
    show rin smile with dissolve
    ri "Когда вы туда попадёте, Карон будет с вами."
    d "Прощай…"
    show rin normal with dissolve
    ri "Увидимся позже, Дэниел…"
    hide rin rormal with dissolve
    stop music fadeout 1.0
##################################################################
##################################################################

    play music happydays
    scene bg street 2 snow day with fade
    x "Прошло какое-то время с тех пор, как я был здесь."
    x "Я решил, что сейчас самое подходящее время."
    x "В конце концов, именно в этом городе я встретил своих лучших друзей."
    x "Уверен, они были бы рады снова меня увидеть."
    x "Я гуляю по городу, чувствуя ностальгию."
    x "Похоже, он не особо изменился с моего последнего визита."
    x "Вскоре я дохожу до ресторана моего дяди."
    x "Делаю глубокий вдох и открываю дверь."
    x "По ту сторону я вижу всех."
##################################################################
    scene bg restaurant with fade
    show velda normal with dissolve
    v "Ты вернулся."
    c "Ага."
    d "Рад тебя видеть."
    hide velda normal with dissolve
    show gwen smile with dissolve
    g "Ты выжил."
    hide gwen smile with dissolve
    show rose smile with dissolve
    r "Хорошо снова тебя видеть."
    c "Вы все меня ждали?"
    c "Если так, то это немного жутко."
    c "Я никому не говорил, что приду."
    hide rose smile with dissolve
    show velda nervous with dissolve
    v "Ну, мы давно хотели тебя увидеть."
    c "Да, кажется, прошла целая вечность, да?"
    hide velda nervous with dissolve
    show rose normal with dissolve
    r "Неважно."
    show rose smile with dissolve
    r "Главное, что мы снова вместе."
    c "Да."
    hide rose smile with dissolve
    show gwen nervous with dissolve
    g "Н-Ну… Что нам делать сначала?"
    d "Почему бы вам всем не отдохнуть?"
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Ты уверен?"
    d "Да, я могу сам присмотреть за рестораном."
    d "Уверен, вам всем есть что наверстать."
    show velda smile with dissolve
    v "Спасибо!"
    c "Не помню, чтобы ты когда-нибудь был таким вежливым."
    show velda angry with dissolve
    v "Заткнись!"
    c "Вот это уже больше на тебя похоже…"
    show velda nervous with dissolve
    x "Гвен и Роуз смеются."
    v "Пойдёмте…"
    hide velda nervous with dissolve
    show rose normal with dissolve
    r "Ага."
    hide rose normal with dissolve
    x "Мы вчетвером выходим на улицу, чтобы провести время вместе."
    stop sound fadeout 1.0
##################################################################
    play music memories
    scene bg mystery sky with fade
    x "В жизни есть много возможностей."
    x "Может быть, всё пойдёт по-твоему, а может и нет."
    x "Но в любом случае, ты должен приложить усилия."
    x "Нужно работать, чтобы пройти путь от того места, где ты начал, до того, где ты сейчас."
    x "В это может быть трудно поверить, но ты тоже можешь достичь хорошего конца."
    x "Это может казаться невозможным."
    x "Это может казаться далёким."
    x "Но если ты будешь тянуться к нему, ты его достигнешь."
    x "Наверное."
    x "Раньше я думал, что этого никогда не случится, но теперь я знаю, что счастливые концы существуют."
    x "Потому что я сам сейчас проживаю один из них."
    x "Многие наши действия повлияют на наше будущее."
    x "Мы сами несём ответственность за то, как они обернутся."
    x "Никто другой."
    x "И теперь я действительно с нетерпением жду, что принесёт мне будущее."
    x "Пока я с Вельдой, Роуз и Гвен, я буду счастлив увидеть его вместе с ними."
    $ achievement.grant("Happy_Ending")
    x "КОНЕЦ — БУДУЩЕЕ"
    stop music fadeout 1.0
    # Самые счастливые титры
    $ renpy.movie_cutscene("video/FutureCredits.webm", delay=199, loops=0, stop_music=True)
    return
