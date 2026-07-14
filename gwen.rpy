label gwenroutestart:

# День 4

    play music normalday
    scene bg bedroom with fade
    show velda normal with dissolve
    v "Ты встаёшь?"
    c "Угу."
    x "Я медленно скатываюсь с кровати на пол."
    show velda frown with dissolve
    v "..."
    c "Знаешь, пол довольно удобный."
    play sound kick
    x "Она пинает меня."
    c "Ой!"
    show velda angry with dissolve
    v "Вставай!"
    c "Ладно, ладно."
    c "Встаю."
    hide velda angry with dissolve
##################################################################
    scene bg restaurant with fade
    x "Когда я прихожу в ресторан, там уже Гвен."
    c "Доброе утро."
    show gwen normal with dissolve
    g "Д-доброе утро."
    hide gwen normal with dissolve
    show velda normal with dissolve
    v "Ты опять к ней пристаёшь?"
    hide velda normal with dissolve
    show gwen normal with dissolve
    g "Он мне не докучает."
    hide gwen normal with dissolve
    show velda normal with dissolve
    v "Ты уверена?"
    show velda nervous with dissolve
    v "Этот парень невероятно раздражающий."
    c "Ты точно не про себя сейчас?"
    show velda angry with dissolve
    v "З-заткнись!"
    hide velda frown with dissolve
    x "Вельда уходит, разъярённая."
    show gwen normal with dissolve
    g "Эм…"
    c "Что?"
    show gwen frown with dissolve
    g "..."
    show gwen normal with dissolve
    g "А она…"
    c "..."
    c "А она что?"
    show gwen frown with dissolve
    g "Она всегда так с тобой разговаривает?"
    c "Да."
    show gwen nervous with dissolve
    g "О."
    c "А разве она со всеми так не разговаривает?"
    show gwen normal with dissolve
    g "Со мной она так не разговаривает."
    c "..."
    show gwen frown with dissolve
    g "Тебе грустно?"
    c "Нет."
    show gwen normal with dissolve
    c "Я в порядке."
    g "Ладно."
    hide gwen normal with dissolve
##################################################################

    play music veldatheme
    scene bg restaurant with fade
    x "После того как Гвен заканчивает есть, она уходит."
    show velda normal with dissolve
    v "Она тебе нравится?"
    c "А?"
    show velda nervous with dissolve
    v "Я спрашиваю, нравится ли тебе Гвен."
    c "Мы просто друзья."
    show velda angry with dissolve
    v "Я не это имею в виду, дурак."
    c "А что ты имеешь в виду?"
    show velda normal with dissolve
    v "Что ты о ней думаешь?"

menu:

    "Она добрая":
        jump gwenisnice

    "Она милая":
        jump gweniscute

    "Эм...":
        jump umgwen

    "Не особо":
        jump nottogwen

label gwenisnice:
    $ gwenpoints += 1
    c "Она добрая."
    show velda frown with dissolve
    v "И это всё, что ты можешь сказать?"
    c "Я просто с ней познакомился, так что пока плохо её знаю."
    c "Но она кажется хорошим человеком."
    show velda normal with dissolve
    v "Не обижай её, ладно?"
    c "Х-хорошо."
    jump veldaaskaboutgwen

label gweniscute:
    $ gwenpoints += 1
    $ achievement.grant("Gwen_Cute")
    c "Она милая."
    show velda nervous with dissolve
    v "Как ты можешь такое говорить, не смущаясь?"
    c "Хех."
    c "Что ж, она ещё и кажется хорошим человеком."
    show velda frown with dissolve
    v "Да мне всё равно. Просто не обижай её."
    c "П-понял."
    jump veldaaskaboutgwen

label umgwen:
    c "Эм…"
    show velda frown with dissolve
    v "..."
    c "Э-э, мы же только познакомились, знаешь?"
    show velda normal with dissolve
    v "Верно."
    show velda nervous with dissolve
    v "Прости, что спросила."
    show velda frown with dissolve
    v "Но если ты её обидишь, я тебя убью."
    c "..."
    jump veldaaskaboutgwen

label nottogwen:
    $ gwenbad += 1
    c "Не особо."
    show velda nervous with dissolve
    v "Тогда почему ты с ней проводишь время?"
    c "Просто из любопытства, наверное."
    show velda angry with dissolve
    v "Боже, да что с тобой не так?"
    c "А что с тобой случилось?"
    show velda normal with dissolve
    v "Если с ней что-нибудь случится, ты умрёшь первым."
    c "Эм…"
    jump veldaaskaboutgwen

label veldaaskaboutgwen:
    c "Похоже, ты заботишься о Гвен."
    show velda nervous with dissolve
    v "Т-тебе так кажется?"
    c "Ты угрожаешь мне расправой, если она пострадает."
    c "Довольно очевидно."
    show velda angry with dissolve
    v "Я имею в виду то, что сказала!"
    c "Она важна для тебя, да?"
    show velda nervous with dissolve
    v "И что, если так…?"
    c "Я не говорю, что в этом что-то не так."
    c "Мне просто любопытно."
    c "Какая у вас связь…?"
    show velda normal with dissolve
    v "Не твоё дело."
    c "Ладно."
    c "Прости, что спросил."
    x "Наш разговор прерывается, когда мы замечаем что-то на столе Гвен."
    show velda nervous with dissolve
    v "Она опять забыла?"
    c "Опять?"
    x "Подойдя ближе, я вижу кошелёк."
    show velda frown with dissolve
    v "Вот это уже проблема."
    show velda nervous with dissolve
    v "Я не могу ей отнести, у меня работа."
    show velda frown with dissolve
    v "И не хочу, чтобы это делал ты, потому что я тебе не доверяю."
    c "Э-эй!"
    show velda nervous with dissolve
    v "Что ж, похоже, у меня нет выбора."
    c "..."
    show velda normal with dissolve
    v "Карон, ты не мог бы отнести ей кошелёк?"

menu:

    "Отнести Гвен кошелёк":
        jump gwenwalletaccept

    "Отказаться":
        jump gwenwalletdeny

label gwenwalletaccept:
    $ gwenpoints += 1
    c "Хорошо."
    c "Я это сделаю."
    show velda smile with dissolve
    v "Хорошо."
    show velda frown with dissolve
    v "Я бы тебе всыпала, если бы ты отказался."
    c "П-понятно."
    show velda nervous with dissolve
    v "А теперь давай."
    hide velda nervous with dissolve
    jump walletchoice

label gwenwalletdeny:
    $ gwenbad += 1
    $ achievement.grant("Wallet_Refusal")
    c "Нет."
    show velda angry with dissolve
    v "ОТНЕСИ. ЕЙ. КОШЕЛЁК."
    c "Эм, я отнесу! Отнесу!"
    show velda nervous with dissolve
    v "Боже."
    show velda frown with dissolve
    v "Отнеси ей, пока я тебе не всыпала."
    c "Иду. Иду."
    hide velda frown with dissolve
    jump walletchoice

label walletchoice:
    play sound runninginhall
    x "В итоге я поспешно выбегаю оттуда."
    stop sound fadeout 1.0
##################################################################

    play music timetowork
    scene bg street 2 day with fade

    x "Я обыскиваю весь город в поисках неё."
    show rose normal with dissolve
    r "Карон? Что ты делаешь?"
    c "Я ищу…"
    show rose nervous with dissolve
    r "Ты выглядишь уставшим…"
    c "Ну да, я устал."
    show rose normal with dissolve
    r "Это из-за Гвен?"
    c "Да."
    c "Откуда ты знаешь?"
    show rose nervous with dissolve
    r "Ну, я видела, как она бежала раньше."
    show rose normal with dissolve
    r "И ты единственный, кто тоже бегает."
    show rose smile with dissolve
    r "Так вы двое играете в догонялки или что-то такое?"
    c "Нет."
    show rose normal with dissolve
    r "Хм."
    show rose nervous with dissolve
    r "Ну, может, она снова играет одна…"
    c "Можешь сказать, в какую сторону она побежала?"
    show rose normal with dissolve
    r "Туда."
    x "Роуз указывает направление, куда побежала Гвен."
    c "Спасибо."
    play sound running
    x "После этого я бегу в том направлении."
    hide rose normal with dissolve
##################################################################
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene bg street day with fade
    x "Это занимает какое-то время, но мне удаётся её найти."

    play music gwentheme
    show gwen normal with dissolve
    g "Карон?"
    c "Вот ты где."
    show gwen nervous with dissolve
    g "Я тебе была нужна?"
    show gwen normal with dissolve
    g "Зачем?"
    c "Ты это забыла."
    x "Я отдаю ей кошелёк."
    show gwen shock with dissolve
    g "Я о-опять забыла!?"
    c "Вельда сказала, что у тебя такая привычка."
    show gwen normal with dissolve
    g "Понятно."
    c "Какие у вас отношения с Вельдой?"
    show gwen nervous with dissolve
    g "Ты её спросил?"
    c "Да, но она мне не сказала."
    show gwen normal with dissolve
    g "Если она тебе не сказала, мне, наверное, тоже не стоит."
    c "Что ж, я не могу вытянуть это из всех подряд."
    show gwen frown with dissolve
    g "Тебе ведь не обязательно это знать, да?"
    c "Наверное, нет."
    show gwen normal with dissolve
    g "Что ж, мне нужно идти."

menu:

    "Куда ты направляешься?":
        jump whereareyougoing

    "О, ладно":
        jump ohalright

    "Я не разрешал тебе убегать":
        jump norunoffgwen

    "Это важно?":
        jump isitimportant

label whereareyougoing:
    c "Куда ты направляешься?"
    show gwen nervous with dissolve
    g "В одно важное место."
    c "Можешь сказать куда?"
    show gwen frown with dissolve
    g "Нет, прости."
    show gwen shock with dissolve
    g "Мне пора!"
    hide gwen nervous with dissolve
    jump gwenrunoff

label ohalright:
    $ gwenpoints += 1
    $ achievement.grant("Respectful_Caron")
    c "О, ладно."
    show gwen smile with dissolve
    g "Спасибо."
    c "Увидимся позже."
    show gwen normal with dissolve
    g "Ага."
    hide gwen normal with dissolve
    jump gwenrunoff

label norunoffgwen:
    $ gwenbad += 1
    $ achievement.grant("Disrespectful_Caron")
    c "Я не разрешал тебе убегать!"
    show gwen frown with dissolve
    g "Пожалуйста, не кричи на меня…"
    show gwen nervous with dissolve
    g "И это правда важно."
    c "Правда?"
    show gwen normal with dissolve
    g "Да."
    show gwen shock with dissolve
    g "Ах! Мне пора!"
    hide gwen shock with dissolve
    jump gwenrunoff

label isitimportant:
    $ gwenpoints += 1
    $ achievement.grant("Respectful_Caron")
    c "Это важно?"
    show gwen nervous with dissolve
    g "Очень."
    c "Тогда я не буду тебя задерживать."
    show gwen normal with dissolve
    g "Ага."
    show gwen smile with dissolve
    g "Э-э, увидимся позже."
    c "Да, пока."
    hide gwen smile with dissolve
    jump gwenrunoff

label gwenrunoff:
    play sound running
    x "И затем она убегает."
    stop sound fadeout 1.0
    x "Мне действительно любопытно, что с ней происходит."
    x "Надеюсь, она расскажет мне позже."
##################################################################
    scene bg restaurant with fade
    play music veldatheme
    show velda normal with dissolve
    v "Что ты завис?"
    c "О, прости."
    show velda nervous with dissolve
    v "Почему ты такой бесполезный?"
    show velda frown with dissolve
    v "Не понимаю, зачем Гвен вообще с тобой разговаривает."
    c "Ты же САМА сейчас со мной разговариваешь, нет?"
    show velda angry with dissolve
    v "Заткнись нахрен!"
    c "Да, прости."
    show velda normal with dissolve
    v "Так ты отнёс Гвен её кошелёк, да?"
    c "Отнёс."
    show velda smile with dissolve
    v "Хорошо."
    c "Эм…"
    show velda normal with dissolve
    v "Что?"
    c "Она куда-то очень спешила."
    c "Ты не знаешь, что это может быть?"
    show velda nervous with dissolve
    v "Нет."
    c "Не знаешь?"
    show velda frown with dissolve
    v "Почему ты спрашиваешь?"
    c "Потому что мне кажется, ты бы знала."
    show velda nervous with dissolve
    v "С чего ты взял, что я бы… о, точно."
    c "Наверное, мне не стоило спрашивать."
    show velda normal with dissolve
    v "Ты беспокоишься о ней?"
    c "Это проблема?"
    show velda nervous with dissolve
    v "Нет…"
    hide velda nervous with dissolve
##################################################################

    #День 5#
    scene bg bedroom with fade
    stop music fadeout 1.0
    show velda shock with fade
    v "Ты уже на ногах?"
    c "Удивлена?"
    show velda nervous with dissolve
    v "..."
    show velda frown with dissolve
    v "Просто не вались обратно."
    c "Не буду."
    c "Какой смысл снова ложиться, если уже встал?"
    show velda nervous with dissolve
    v "Да мне плевать."
    show velda frown with dissolve
    v "Просто не мешай мне сегодня."
    c "Не буду."
    hide velda frown with dissolve
##################################################################

    scene bg street 2 day with fade
    play music snowydays

    x "Я выхожу на улицу и ищу Гвен."
    x "Как и вчера, её трудно найти."
    x "Чёрт, чем же эта девчонка занимается?"
##################################################################

    scene bg hospital outside with fade
    x "Побродив какое-то время, я вижу больницу."
    x "И Гвен заходит внутрь."
    x "Что она здесь делает?"
    x "Мне очень любопытно, но я думаю, что пока сдержусь."
##################################################################
    scene bg downtown day with fade
    show rose normal with dissolve
    r "Карон?"
    show rose nervous with dissolve
    r "Что происходит?"
    c "Привет."
    c "..."
    show rose frown with dissolve
    r "Ты выглядишь подавленным."
    show rose nervous with dissolve
    r "Что тебя беспокоит?"
    c "А, ничего."
    show rose nervous with dissolve
    r "Ты уверен?"
    show rose smile with dissolve
    r "Вы с Гвен играли в прятки и теперь не можешь её найти?"
    c "Мы не играем в прятки."
    show rose nervous with dissolve
    r "Понятно."
    show rose frown with dissolve
    r "Эм… я тебя отвлекаю?"
    c "Нет, не особо."
    show rose nervous with dissolve
    r "Вы с Гвен поссорились?"
    c "Нет. Ничего такого."
    c "Эм…"
    c "С ней что-то не так?"
    show rose normal with dissolve
    r "Насколько я знаю, нет."
    show rose nervous with dissolve
    r "И что ты вообще имеешь в виду?"
    c "Прости, ничего."
    c "Забудь, что я спросил."
    show rose normal with dissolve
    r "Но теперь мне любопытно…"
    c "Я сказал, ничего."
    show rose nervous with dissolve
    r "Ладно."
    hide rose nervous with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg restaurant with fade
    x "В конце концов я возвращаюсь домой."
    show velda angry with dissolve
    v "Ты опоздал."
    c "Прости."
    show velda nervous with dissolve
    v "Что ж, «прости» недостаточно."
    show velda normal with dissolve
    v "Давай, пошевеливайся на работу."
    c "Понял."
    hide velda normal with dissolve
##################################################################

    play music worryaboutyou
    scene bg restaurant with fade

    show velda normal with dissolve
    v "Итак, о чём ты думаешь?"
    c "Ни о чём."
    show velda frown with dissolve
    v "Чушь."
    show velda normal with dissolve
    v "О чём ты думаешь?"
    c "Ладно."
    c "Это о Гвен."
    c "Я видел, как она заходила в больницу раньше."
    c "С ней… что-то не так?"
    show velda nervous with dissolve
    v "Не суй нос не в своё дело."
    c "А?"
    show velda frown with dissolve
    v "Что бы с ней ни происходило — это её дело. Не твоё."
    c "Но разве тебе не хотелось узнать, что со мной происходит?"
    show velda normal with dissolve
    v "Это другое."
    c "Чем же?"
    show velda nervous with dissolve
    v "Потому что."
    show velda normal with dissolve
    v "Так ты переживаешь за неё?"

menu:

    "Конечно":
        jump worryaboutgwen

    "Честно говоря, просто любопытно":
        jump curiousaboutgwen

    "А ты?":
        jump whataboutvelda

label worryaboutgwen:
    $ gwenpoints += 2
    c "Конечно."
    c "Было бы странно, если бы я не переживал."
    show velda smile with dissolve
    v "Понимаю."
    show velda normal with  dissolve
    v "..."
    show velda smile with dissolve
    v "Пожалуйста, будь с..."
