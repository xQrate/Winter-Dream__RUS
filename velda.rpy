label veldaroutestart:

    # День 4 #
    scene bg bedroom with fade
    show velda angry with dissolve
    v "ПОРА ВСТАВАТЬ!"
    c "О, Боже мой!"
    c "Что за чёрт!?"
    show velda normal with dissolve
    v "Одевай свою задницу и за работу."
    c "Ладно, ладно."
    hide velda normal with dissolve
##################################################################

    play music veldatheme
    scene bg restaurant with fade
    x "Я работаю в ресторане."
    x "Знаю, дядя хочет, чтобы я работал, но в основном потому, что хочу, чтобы Вельда перестала на меня орать."
    x "Зачем он вообще нанял такую девушку, как она?"
    show velda nervous with dissolve
    v "Ты о чём-то грубом думаешь, да?"
    c "Нет, конечно нет!"
    show velda frown with dissolve
    v "Твоё лицо говорит об обратном."
    c "Можно я просто поработаю, пожалуйста?"
    show velda nervous with dissolve
    v "Если увижу, что ты действительно стараешься."
    d "Так, так, вы двое."
    c "Доброе утро."
    d "Утро."
    show velda normal with dissolve
    v "Скажи своему ленивому племяннику работать."
    d "О, ах, Карон. За работу."
    show velda angry with dissolve
    v "Почему это не звучит так, будто ты серьёзно!?"
    d "Он ведь не нарочно плохо работает."
    c "Это значит, ты думаешь, я недостаточно хорош?"
    d "Нет, нет."
    d "Вельда, посмотри, что ты начала."
    show velda nervous with dissolve
    v "Но-"
    d "Хватит спорить с коллегами."
    d "Не забывай, кто тебе платит."
    show velda normal with dissolve
    v "Д-да, сэр."
    x "Ого, дядя действительно может её заткнуть."
    v "Сотри эту тупую ухмылку со своего лица."
    x "Ох, похоже, она будет просто тихо бормотать свои мысли."
    x "Ну, это будет чертовски раздражающим."
##################################################################
    stop music fadeout 1.0
    scene bg restaurant with fade
    x "Довольно быстро наступает после обеда."
    x "Как ни странно, я нигде не вижу Вельду."
    x "Куда она могла деться?"
    d "Карон?"
    c "Да?"
    d "Можешь вынести мусор?"
    c "Конечно."
##################################################################
    scene bg street 2 day with fade
    x "Выхожу на улицу с мусорными пакетами и несу их к мусорному контейнеру."
    x "Затем замечаю что-то в переулке за рестораном."
    x "Мне любопытно, так что я пойду посмотрю."
##################################################################
    scene bg alley with fade
    x "Когда я возвращаюсь, вижу Вельду."
    play music youdontbelong
    x "И она... курит сигарету."
    x "Вельда... курит?"
    show velda shock with dissolve
    v "К-Как давно ты тут стоишь?"
    c "Только что пришёл."
    c "Так, эм, ты часто сюда ходишь?"
    play sound running
    x "Вельда быстро подбегает ко мне и кладёт руки мне на плечи, крепко сжимая их."
    stop sound fadeout 1.0
    show velda angry with dissolve
    v "Никому. Никому. Не рассказывай."
    show velda frown with dissolve
    v "Понял?"

menu:

    "Пообещать не рассказывать":
        jump promisenottotellonher

    "Может рассказать Дэниелу":
        jump mighttelluncle

    "Не знаю":
        jump idkaboutcig

label idkaboutcig:

    c "Не знаю."
    show velda nervous with dissolve
    v "Лучше не надо."
    c "Кто знает?"
    c "Может быть."
    show velda angry with dissolve
    v "Заткнёшься ты?"
    c "Хорошо."
    c "Буду молчать."
    jump cigencounter

label mighttelluncle:

    $ veldabad += 1

    c "Может, расскажу дяде."
    show velda nervous with dissolve
    v "Чёрт, Карон."
    c "Ты вечно ведёшь себя как стерва."
    c "Почему я должен тебя слушать?"
    show velda angry with dissolve
    v "Что ты, чёрт возьми, только что сказал?"
    $ achievement.grant("Caron_Balls")
    c "Я просто сказал, что ты стерва."
    show velda nervous with dissolve
    v "Если кому-то расскажешь, я тебя убью, мать твою."
    c "Хорошо, хорошо."
    c "Не скажу."
    jump cigencounter

label promisenottotellonher:

    c "Обещаю, что не расскажу!"
    c "Уверен, будут проблемы, если слишком много людей узнает!"
    show velda nervous with dissolve
    v "Лучше не надо."
    $ achievement.grant("Caron_LipsSealed")
    c "Я уже сказал, что не скажу."
    show velda normal with dissolve
    v "Чёрт."
    show velda nervous with dissolve
    v "Не могу поверить, что именно ты обнаружил мой секрет."
    c "Прости."
    show velda frown with dissolve
    v "Ничего не могу с этим поделать."
    c "Буду держать рот на замке."
    jump cigencounter

label cigencounter:

    show velda normal with dissolve
    v "Хорошо."
    show velda smile with dissolve
    v "Теперь мне не придётся тебя убивать."
    c "Честно, никогда не знаю, шутишь ты или нет."
    show velda normal with dissolve
    v "Мальчик, я похожа на шутящую?"
    c "С тобой никогда не поймёшь."
    show velda nervous with dissolve
    v "Заткнись уже."
    c "Ладно, буду молчать."
    hide velda nervous with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg restaurant with fade
    x "Позже той ночью я очень нервничаю."
    x "Я узнал секрет Вельды."
    x "И она пригрозила мне держать рот на замке."
    x "Я не ожидал узнать, что она курит, но в то же время не особо удивлён."
    v "Ты работаешь?"
    c "Д-да, работаю!"
    x "Находиться в одной зоне с ней или просто слышать её голос..."
    x "Ни то, ни другое не полезно для моего сердца."
##################################################################

    # День 5 #

    scene bg bedroom with fade
    show velda angry with dissolve
    v "ПРОСЫПАЙСЯ!"
    c "Не обязательно будить меня так."
    c "Знаю, ты расстроена из-за вчерашнего, но я сказал, что не расскажу."
    show velda nervous with dissolve
    v "Откуда мне знать, что ты не нарушишь обещание?"
    c "Боже правый."
    hide velda nervous with dissolve
##################################################################

    play music snowydays
    scene bg restaurant with fade
    x "Не желая, чтобы она на меня больше кричала, я быстро берусь за работу."
    d "Ты сегодня полон энергии."
    c "Раз уж ты позволяешь мне остаться, я бы предпочёл не лениться."
    show velda nervous with dissolve
    v "Кто не работает, тот не ест."
    show velda smile with dissolve
    v "Хотя тебе всё равно ничего не достанется."
    c "Ты меня так ненавидишь?"
    d "Не принимай так близко к сердцу."
    d "Она ненавидит ВСЕХ!"
    show velda angry with dissolve
    v "Как ты смеешь!?"
    d "О, точно."
    d "Есть ОДНО исключение."
    show velda nervous with dissolve
    v "Заткнись."
    d "А, точно."
    d "Мне нельзя это говорить."
    c "Теперь мне стало любопытно."
    play sound thudhard
    x "Вельда наступает мне на ногу."
    stop sound fadeout 1.0
    c "Ой!"
    show velda angry with dissolve
    v "Не лезь не в своё дело!"
    c "Ладно, ладно."
    c "Не буду."
    show velda normal with dissolve
    v "Хорошо."
    d "Вы двое отлично ладите."
    show velda angry with dissolve
    cv "Нет, не ладим!"
    hide velda frown with dissolve
    stop music fadeout 1.0
##################################################################

    play music happydays
    scene bg restaurant with fade
    show velda normal with dissolve
    v "Тебе нужно быть осторожнее."
    hide velda normal with dissolve
    show gwen frown with dissolve
    g "П-Прости."
    hide gwen frown with dissolve
    show velda smile with dissolve
    v "Не переживай об этом."
    c "Что случилось?"
    hide velda smile with dissolve
    show gwen shock with dissolve
    g "Прости, я наделала беспорядок! Я не хотела-"
    hide gwen shock with dissolve
    show velda normal with dissolve
    v "Я же сказала, всё в порядке."
    x "А если бы я наделал беспорядок, Вельда бы меня ударила или что-то в этом роде."
    show velda nervous with dissolve
    v "Ни слова."
    hide velda nervous with dissolve
    show gwen frown with dissolve
    g "П-прости."
    hide gwen frown with dissolve
    show velda frown with dissolve
    v "Я не с тобой разговариваю."
    c "Верно..."
    x "Так вот с кем Вельда милая?"
    x "Похоже, это не долго оставалось секретом."
    x "Вельда оставляет нас вдвоём."
    c "Так, эм..."
    hide velda frown with dissolve
    show gwen normal with dissolve
    g "Я в порядке."
    c "Можно спросить кое-что?"
    show gwen nervous with dissolve
    g "Что?"
    c "Какие у вас отношения с Вельдой?"
    show gwen frown with dissolve
    g "О, эм... мне можно говорить?"
    c "Вы друзья или что-то такое?"
    show gwen nervous with dissolve
    g "Э, д-да..."
    show gwen normal with dissolve
    g "Что-то вроде того."
    x "Почему она нервничает...?"
    c "Можешь рассказать мне что-нибудь о ней?"
    c "Ну, какая она... или её история?"
    show gwen nervous with dissolve
    g "Разве не следует спросить у неё?"
    c "Она бы мне, наверное, не рассказала."
    show gwen smile with dissolve
    g "Ну, она для меня как сестра."
    show gwen nervous with dissolve
    g "И эм... она не самый приятный человек."
    show gwen frown with dissolve
    g "Она довольно груба с большинством."
    c "Это я уже знаю."
    show gwen normal with dissolve
    g "Но ей правда не всё равно до других."
    show gwen nervous with dissolve
    g "Она говорит вещи вроде того, что не хочет, чтобы кто-то из них закончил как она..."
    show gwen shock with dissolve
    g "Кажется, я слишком много сказала!"
    c "Эй, эй."
    c "Если не должна была говорить, то я не буду думать об этом."
    show gwen nervous with dissolve
    g "Я правда мало что знаю о её прошлом."
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Эй, о чём вы говорите?"
    hide velda normal with dissolve
    show gwen normal with dissolve
    g "Мы точно не о тебе говорили, если ты об этом подумала-"
    show gwen shock with dissolve
    g "Ах, прости!"
    x "Вельда вздыхает."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Не знаю, о чём ты там болтаешь, но не выдумывай, ладно?"
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "П-поняла."
    hide gwen nervous with dissolve
    stop music fadeout 1.0
##################################################################

    play music calm
    scene bg restaurant with fade
    x "После работы я нахожу дядю."
    x "Как ни странно, с ним и Роуз."
    d "А, Карон."
    d "Чем могу помочь?"
    c "Можешь рассказать мне о Вельде?"
    d "Что о ней?"
    c "Почему ты её нанял?"
    d "Она захотела здесь работать."
    c "И всё?"
    show rose normal with dissolve
    r "Зачем тебе вообще знать о Вельде?"
    c "А, без причины."
    show rose nervous with dissolve
    r "Ну, я тоже мало что о ней знаю."
    hide rose nervous with dissolve
    c "Прости, что спросил."
    d "Она тебе нравится или что?"
    c "Нет, ничего подобного."
    c "Просто любопытно, как такая девушка работает на тебя."
    d "Что ж, я не из тех, кто лезет не в своё дело."
    d "Так что я позволил ей работать, не особо вникая в её прошлое."
    c "Разве ты не должен был это сделать!?"
    d "Расслабься, всё будет хорошо!"
##################################################################

    stop music fadeout 1.0
    scene bg bedroom with fade
    x "В итоге я не так много узнал о Вельде."
    x "Что за девушка и как она оказалась работающей на дядю?"
    x "И почему она меня интересует?"
    x "Она не из тех девушек, с которыми я бы хотел быть рядом."
    x "...Наверное."
##################################################################

# День 6 #

    play music morningactivity
    scene bg bedroom with fade
    x "Мне приснился странный сон прошлой ночью."
    x "Думаю, там была Вельда... и что произошло?"
    play sound slap
    x "Меня только что ударили."
    x "А, точно, это случилось."
    show velda angry with dissolve
    v "Просыпайся, козёл!"
    c "Это не моё имя."
    show velda nervous with dissolve
    v "Что ж, ты бы не отозвался на своё настоящее имя."
    c "Моё лицо болит..."
    show velda normal with dissolve
    v "Ну."
    show velda smile with dissolve
    v "Я всё это время тебя била."
    x "Так вот что мне снилось..."
    x "Похоже, мне это не понравилось, да?"
    show velda angry with dissolve
    v "Сотри эту тупую ухмылку со своего лица."
    c "Какую ухмылку?"
    show velda nervous with dissolve
    v "Ту тупую на твоём лице."
    c "На моём лице?"
    show velda angry with dissolve
    v "Боже, ты тупой."
    c "Может быть..."
    show velda nervous with dissolve
    v "Почему бы тебе просто не встать?"
    c "Я подумаю."
    play sound slap
    x "Она снова меня бьёт."
    c "Знаешь, если будешь продолжать, мне может это начать нравиться."
    play sound thudhard
    x "Она прыгает на меня."
    stop sound fadeout 1.0
    c "Ох!"
    c "Ладно, ладно!"
    c "Больше ничего такого не скажу."
    show velda angry with dissolve
    v "Лучше не говори!"
    hide velda angry with dissolve
##################################################################

    scene bg restaurant with fade

    d "Ты выглядишь уставшим."
    c "Разве?"
    d "Да."
    d "Ты вообще выспался прошлой ночью?"
    c "Думаю, я спал нормально."
    c "Просто мне приснился действительно странный сон."
    d "Что случилось?"
    c "Я бы предпочёл не говорить."
    d "Так это был один из ТЕХ снов, да...?"
    d "Нам нужно сменить тебе-"
    c "Нет, я не это имел в виду!"
    d "О, так стирать не придётся?"
    show velda nervous with dissolve
    v "Что вы, чёрт возьми, обсуждаете?"
    c "Не знаю, но мой дядя ведёт себя мерзко."
    show velda frown with dissolve
    v "Вы оба отвратительны."
    hide velda frown with dissolve
    stop music fadeout 1.0
##################################################################

    play music veldatheme
    scene bg restaurant with fade
    show velda nervous with dissolve
    v "Не могу поверить, что мне приходится мириться с тобой."
    c "Ты когда-нибудь пробовала быть добрее?"
    show velda normal with dissolve
    v "Добрее?"
    show velda nervous with dissolve
    v "К тебе?"
    show velda frown with dissolve
    v "Зачем бы я это делала?"
    c "Было бы приятнее?"
    c "У тебя, наверное, было бы больше друзей."
    show velda nervous with dissolve
    v "Меня и так устраивает."
    c "Одиноко?"
    show velda angry with dissolve
    v "Заткнись!"
    show velda nervous with dissolve
    v "Что, чёрт возьми, заставляет тебя думать, что мне одиноко?"
    c "Похоже, у тебя нет друзей."
    c "Кроме Гвен, в смысле..."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Д-Д кто-то назвал моё имя?"
    c "Ах!"
    c "Как давно ты здесь?"
    show gwen nervous with dissolve
    g "Какое-то время."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Не нужно волноваться из-за этого парня."
    show velda normal with dissolve
    v "Он просто жалкий неудачник без друзей."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Но у тебя ведь тоже нет друзей..."
    show gwen shock with dissolve
    g "Ах!"
    show gwen frown with dissolve
    g "Прости!"
    show gwen shock with dissolve
    g "Я не это имела в виду!"
    x "Вельда вздыхает."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Давай просто не будем об этом говорить."
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Х-Хорошо."
    show gwen normal with dissolve
    g "Так, эм..."
    show gwen nervous with dissolve
    g "Вельда доставляет тебе проблемы?"
    c "Что ты имеешь в виду?"
    show gwen normal with dissolve
    g "Как ты себя чувствуешь, работая с ней?"

menu:

    "Мне не нравится":
        jump dontlikeworkingwithvelda

    "Нормально":
        jump okayworkingwithvelda

    "Мне нравится":
        jump likeworkingwithvelda

    "Не уверен":
        jump idkworkwithvelda

label dontlikeworkingwithvelda:
    $ veldabad += 1
    c "Мне не особо нравится с ней работать."
    c "Она невероятно грубая."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Ты ведь понимаешь, что я прямо здесь, да?"
    c "Да."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Понимаю."
    hide gwen normal with dissolve
    show velda angry with dissolve
    v "Эй!"
    jump gwenasksaboutvelda

label okayworkingwithvelda:
    c "Думаю, я нормально к этому отношусь."
    c "Она немного грубая, но я могу это потерпеть."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Я прямо здесь..."
    c "Точно."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Понятно."
    hide gwen normal with dissolve
    jump gwenasksaboutvelda

label likeworkingwithvelda:
    $ veldapoints += 1
    c "Мне на самом деле нравится с ней работать."
    c "Она немного грубая, но я не думаю, что она плохой человек."
    show gwen nervous with dissolve
    g "Правда?"
    c "Да."
    hide gwen nervous with dissolve
    show velda frown with dissolve
    v "Почему вы двое обсуждаете меня, как будто меня тут нет?"
    jump gwenasksaboutvelda

label idkworkwithvelda:
    c "Я правда не знаю."
    c "Учитывая, насколько она груба, я не уверен."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Ты это прямо при мне говоришь."
    c "Точно."
    hide velda nervous with dissolve
    show gwen smile with dissolve
    g "Хех."
    hide gwen smile with dissolve
    show velda frown with dissolve
    v "Не смешно."
    jump gwenasksaboutvelda

label gwenasksaboutvelda:

    show velda nervous with dissolve
    v "Можете не говорить обо мне?"
    c "Я не слышал, чтобы ты говорила «пожалуйста»."
    show velda frown with dissolve
    v "Пожалуйста... прекратите обсуждать меня."
    c "О мой Бог."
    hide velda frown with dissolve
    show gwen shock with dissolve
    g "..."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Что?"
    c "Нам нужно это записать в календарь!"
    show velda frown with dissolve
    v "Что?"
    show velda nervous with dissolve
    v "Что я сделала?"
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Ты сказала «пожалуйста»..."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Это не такое уж большое событие, как вы делаете."
    c "Но у тебя никогда не было манер."
    show velda angry with dissolve
    v "Как насчёт того, чтобы ты заткнулся, пока я не вбила твоё лицо в пол?"
    show velda nervous with dissolve
    v "И Гвен... пожалуйста, не поощряй его."
    hide velda frown with dissolve
    show gwen shock with dissolve #шок
    g "Ты снова это сказала..."
    c "Теперь мне точно нужно это записать!"
    hide gwen shock with dissolve
    show velda nervous with dissolve
    v "Я убью вас обоих."
    hide velda nervous with dissolve
    stop music fadeout 1.0
##################################################################

    play music snowydays

    scene bg restaurant with fade
    show velda normal with dissolve
    v "Твоему дяде нужно, чтобы мы сходили за покупками."
    c "Нам обоим нужно идти?"
    show velda nervous with dissolve
    v "Слишком много вещей для одного человека."
    show velda normal with dissolve
    v "И кто-то должен присмотреть за магазином."
    c "Думаю, ему было бы неловко идти с одним из нас."
    show velda nervous with dissolve
    v "Наверное."
    show velda frown with dissolve
    v "Но я бы предпочла не идти с тобой."
    c "Не можешь попросить Гвен?"
    show velda nervous with dissolve
    v "Она здесь не работает."
    c "Ладно, я пойду с тобой."
    hide velda nervous with dissolve
    stop music fadeout 1.0
##################################################################

    scene bg store day with fade
    x "Иду в магазин с Вельдой."
    x "К нам быстро подходит знакомое лицо."
    play music rosetheme
    show rose normal with dissolve
    r "Что вы двое делаете вместе?"
    c "Ходим за покупками."
    show rose shock with dissolve
    r "Это свидание...?"
    hide rose shock with dissolve
    show velda nervous with dissolve
    v "Как будто я бы встречалась с этим неудачником..."
    c "Ей нужно поработать над навыками общения с людьми, прежде чем даже думать о свиданиях."
    play sound slap
    x "Она снова меня ударила..."
    stop sound fadeout 1.0
    hide velda nervous with dissolve
    show rose smile with dissolve
    r "Вы двое кажетесь близкими."
    cv "Нет, не близкие!"
    show rose normal with dissolve
    r "Хех."
    hide rose normal with dissolve
    show velda nervous with dissolve
    v "Мы здесь по поручению."
    c "А, точно."
    c "Дядя попросил нас закупить кое-какие вещи."
    hide velda nervous with dissolve
    show rose nervous with dissolve
    r "И вы пришли вместе?"
    c "Так проще нести всё это обратно."
    c "Плюс, дядя хочет остаться и присмотреть за рестораном."
    show rose normal with dissolve
    r "Он правда любит свой ресторан, да...?"
    c "Наверное..."
    show rose nervous with dissolve
    r "Что ж, не буду вам мешать."
    show rose smile with dissolve
    r "Не хочу портить ваше свидание."
    cv "Это не свидание!"
    hide rose smile with dissolve
    stop music fadeout 1.0
##################################################################
    play music normalday
    scene bg store day with fade
    show velda nervous with dissolve
    v "Ненавижу её."
    c "Серьёзно?"
    c "Что она тебе сделала?"
    show velda frown with dissolve
    v "Тьфу."
    show velda nervous with dissolve
    v "Ни один человек не может быть настолько добрым."
    show velda normal with dissolve
    v "Она точно притворяется."
    c "Ты так думаешь?"
    show velda nervous with dissolve
    v "Думаю?"
    show velda normal with dissolve
    v "Я это знаю..."
    c "Не знаю..."
    c "Имеет ли это значение?"
    show velda nervous with dissolve
    v "Наверное, нет."
    show velda frown with dissolve
    v "Она мне не особо важна."
    show velda normal with dissolve
    v "Так что, какая она на самом деле, не должно иметь значения."
    c "Даже если она правда такая добрая?"
    show velda nervous with dissolve
    v "Мне в это трудно поверить."
    c "Думаю, я могу это понять."
    show velda normal with dissolve
    v "Эм... "
    c "Что?"
    show velda nervous with dissolve
    v "..."
    c "Давай, говори."
    show velda frown with dissolve
    v "Неважно."
    c "Эй, нельзя же так."
    c "Сделать вид, что хочешь сказать что-то важное, и просто промолчать."
    show velda nervous with dissolve
    v "Не переживай об этом."
    c "Чем больше ты говоришь мне не переживать, тем больше я переживаю."
    show velda normal with dissolve
    v "Ладно..."
    c "Ты звучишь расстроенно..."
    show velda nervous with dissolve
    v "Хочешь, чтобы я поговорил или нет?"
    c "Да."
    show velda normal with dissolve
    v "Я слышала, ты вчера расспрашивал обо мне."
    c "О?"
    c "Кто тебе сказал?"
    show velda nervous with dissolve
    v "Гвен."
    c "Понятно."
    show velda frown with dissolve
    v "Почему ты такой любопытный?"
    show velda nervous with dissolve
    v "Это не твоё дело."
    c "Ну, после того, что я видел, разве это не моё дело?"
    show velda angry with dissolve
    v "Тебе обязательно нужно было это поднять, да?"
    c "Прости."
    show velda nervous with dissolve
    v "Да пофиг."
    show velda normal with dissolve
    v "Мне просто любопытно."
    show velda nervous with dissolve
    v "Почему тебе вообще есть до меня дело?"
    show velda normal with dissolve
    v "Почему ты вообще мной заинтересовался?"

menu:

    "Потому что ты мне нравишься":
        jump crushonvelda

    "Хочу, чтобы мы стали друзьями":
        jump wanttobefriendswithvelda

    "Хочу узнать больше о коллеге":
        jump learnaboutcoworker

label crushonvelda:
    $ veldapoints += 1
    $ confesstovelda = True
    $ achievement.grant("Caron_LikeVelda")
    c "Потому что ты мне нравишься."
    show velda shock with dissolve
    v "Что?"
    c "Ты мне нравишься."
    c "В смысле, ты мне правда нравишься."
    show velda embarassed with dissolve
    v "..."
    show velda nervous with dissolve
    v "Как ты можешь такое говорить?"
    c "Я правда так чувствую."
    show velda embarassed with dissolve
    v "Эм... спасибо?"
    show velda nervous with dissolve
    v "Но я не знаю, как мне реагировать."
    c "Тебе не нужно отвечать прямо сейчас."
    show velda frown with dissolve
    v "Тогда не буду."
    c "Но, пожалуйста, когда-нибудь скажи что-нибудь."
    show velda nervous with dissolve
    v "Я подумаю."
    jump whycaroncaresaboutvelda

label wanttobefriendswithvelda:
    $ veldapoints += 1
    $ friendswithvelda = True
    $ achievement.grant("Caron_VeldaFriend")
    c "Хочу, чтобы мы стали друзьями."
    show velda nervous with dissolve
    v "Правда?"
    show velda frown with dissolve
    v "С тем, как я с тобой разговариваю, ты хочешь быть друзьями?"
    c "Да."
    c "В смысле, ты такая, потому что у тебя нет друзей, да?"
    show velda angry with dissolve
    v "Зачем ты так?"
    c "Прости."
    show velda normal with dissolve
    v "Да пофиг."
    show velda smile with dissolve
    v "Но... думаю, это нормально."
    c "Так мы теперь друзья?"
    show velda normal with dissolve
    v "Ага."
    show velda nervous with dissolve
    v "Но не думай, что я изменю то, как разговариваю, ради тебя."
    c "Я так и подумал, что это не изменится..."
    jump whycaroncaresaboutvelda

label learnaboutcoworker:
    c "Я просто хочу узнать о своей коллеге."
    c "Раз мы оба работаем в одном месте, знать друг о друге больше не повредит, да?"
    show velda nervous with dissolve
    v "Наверное, нет."
    show velda frown with dissolve
    v "Однако не жди, что я расскажу тебе всё."
    c "Ты думаешь, я захочу узнать что-то неуместное?"
    show velda shock with dissolve #шок
    v "Что ещё в голове у парня?"
    c "Вещи, которые не грязные."
    show velda frown with dissolve
    v "Значит, ты признаёшь, что у тебя грязные мысли?"
    c "Я такого не говорил."
    show velda angry with dissolve #злой
    v "Тьфу."
    show velda nervous with dissolve
    v "Если ты когда-нибудь спросишь что-то действительно личное, я убью тебя."
    c "Я не собираюсь спрашивать о чём-то настолько большом."
    show velda frown with dissolve
    v "Да пофиг."
    jump whycaroncaresaboutvelda

label whycaroncaresaboutvelda:
    show velda smile with dissolve
    v "Спасибо, что ответил мне."
    c "..."
    show velda nervous with dissolve
    v "Что?"
    c "Ты меня поблагодарила...?"
    show velda frown with dissolve
    v "И что?"
    c "Мне нужно это тоже в календарь записать!"
    show velda nervous with dissolve
    v "Я правда тебя убью..."
    hide velda nervous with dissolve
    stop music fadeout 1.0
##################################################################

    # День 7 #

    scene bg bedroom with fade
    show velda smile with dissolve
    v "Доброе утро."
    c "А, утро."
    x "Странно."
    x "Обычно меня ждёт грубое пробуждение."
    x "Она что, добрая?"
    show velda normal with dissolve
    v "Я дам тебе одеться."
    hide velda normal with dissolve
    x "Она выходит из комнаты."
    x "Кто эта девушка и что она сделала с Вельдой!?"
##################################################################

    play music snowydays
    scene bg restaurant with fade
    c "Ты в порядке?"
    show velda smile with dissolve
    v "Я в порядке."
    show velda normal with dissolve
    v "Почему ты спрашиваешь?"
    c "Ну, ты сегодня просто не похожа на себя."
    show velda angry with dissolve
    v "Что, чёрт возьми, заставляет тебя думать, что я не я?"
    c "Ну, когда ты будишь меня... ты обычно не так добра об этом."
    show velda nervous with dissolve
    v "Я немного подумала о том, что ты сказал."
    c "Понятно."
    show velda angry with dissolve
    v "Не пойми неправильно!"
    show velda nervous with dissolve
    v "Это не значит, что я делаю это только ради тебя!"
    c "Понял."
    show velda normal with dissolve
    v "Так, эм... после работы..."
    c "Что будет после работы?"
    show velda nervous with dissolve
    v "Я бы хотела поговорить с тобой кое о чём."
    c "О, ладно?"
    hide velda nervous with dissolve
    show gwen angry with dissolve
    g "Эй, нечестно!"
    c "Откуда ты взялась!"
    show gwen nervous with dissolve
    g "Почему ты забираешь Вельду?"
    show gwen angry with dissolve
    g "Она моя!"
    hide gwen angry with dissolve
    show velda nervous with dissolve
    v "..."
    hide velda nervous with dissolve
    show gwen shock with dissolve
    g "Ах, прости!"
    show gwen nervous with dissolve
    g "Я не хотела-"
    hide gwen nervous with dissolve
    show velda normal with dissolve
    v "Не нужно каждый раз так паниковать."
    hide velda normal with dissolve
    show gwen frown with dissolve
    g "Прости."
    hide gwen frown with dissolve
    show velda nervous with dissolve
    v "Хватит извиняться."
    c "Она тебе правда нравится, да?"
    hide velda nervous with dissolve
    show gwen smile with dissolve
    g "Да."
    show gwen normal with dissolve
    g "Потому что она моя-"
    show gwen shock with dissolve
    g "Ах, прости!"
    hide gwen shock with dissolve
    show velda normal with dissolve
    v "Ты слишком сильно паникуешь..."
    c "Даже не буду спрашивать."
    show velda smile with dissolve
    v "Хорошо."
    show velda normal with dissolve
    v "Я бы убила тебя, если бы ты спросил."
    hide velda normal with dissolve
    stop music fadeout 1.0
##################################################################

    play music rosetheme
    scene bg restaurant with fade
    show rose normal with dissolve
    r "Вижу, вы двое всё ещё ладите."
    c "Это так выглядит?"
    show rose smile with dissolve
    r "Ага."
    c "Не знаю."
    c "Думаю, она стала немного добрее, но... не знаю."
    show rose nervous with dissolve
    r "Не знаешь?"
    c "Да."
    show rose normal with dissolve
    r "Так вы двое не встречаетесь?"

    if confesstovelda == True:
        jump tellroseaboutveldacrush
    elif friendswithvelda == True:
        jump tellroseaboutveldafriendship
    else:
        jump denywhatroseasksaboutvelda

label tellroseaboutveldacrush:
    c "Нет, но надеюсь, скоро будем."
    show rose smile with dissolve
    r "Так она тебе нравится?"
    c "Да..."
    jump answerroseaboutveldaday7

label tellroseaboutveldafriendship:
    c "Мы просто друзья."
    show rose nervous with dissolve
    r "Ох."
    jump answerroseaboutveldaday7

label denywhatroseasksaboutvelda:
    c "Нет, вообще нет."
    c "Не знаю, буду ли когда-нибудь, если честно."
    show rose frown with dissolve
    r "Понятно."
    jump answerroseaboutveldaday7

label answerroseaboutveldaday7:

    show rose normal with dissolve
    r "Что ж, думаю, то, что у тебя сейчас с ней, нормально."
    show rose smile with dissolve
    r "Так что не облажайся."
    c "А, да."
    c "Постараюсь."
    show rose normal with dissolve
    r "Что ж, мне пора идти."
    c "Ладно."
    stop music fadeout 1.0
    play sound walkinginside
    hide rose normal with dissolve
    x "Роуз выходит из ресторана."
    stop sound fadeout 1.0
    play music veldatheme
    show velda normal with dissolve
    v "О чём вы с ней разговаривали?"
    c "О всяком."
    show velda nervous with dissolve
    v "О чём?"
    c "О всяком."
    show velda frown with dissolve
    v "Это не ответ на мой вопрос."

menu:

    "Какая ты милая":
        jump howcuteyouarevelda

    "Какая ты крутая":
        jump howcoolyouarevelda

    "Какая ты грубая":
        jump howrudeyouarevelda

    "Ни о чём важном":
        jump notaboutyouvelda

label howcuteyouarevelda:
    $ veldapoints += 1
    $ achievement.grant("Velda_Cool")
    c "Мы говорили о том, какая ты милая."
    show velda shock with dissolve
    v "М-милая?"
    show velda embarassed with dissolve
    v "Ты думаешь, я милая?"
    c "Да."
    show velda nervous with dissolve
    v "Понятно."
    show velda embarassed with dissolve
    v "..."
    c "Ты смущена?"
    show velda angry with dissolve
    v "Заткнись!"
    jump veldawantstoknowday7

label howcoolyouarevelda:
    $ veldapoints += 1
    c "Мы говорили о том, какая ты крутая."
    show velda nervous with dissolve
    v "О, правда?"
    show velda normal with dissolve
    v "Ты думаешь, я крутая?"
    c "Да."
    show velda nervous with dissolve
    v "Хм."
    c "Что?"
    show velda normal with dissolve
    v "Ничего."
    jump veldawantstoknowday7

label howrudeyouarevelda:
    $ veldabad += 1
    c "Мы говорили о том, какая ты грубая."
    show velda frown with dissolve
    v "Мог бы просто соврать, знаешь ли?"
    show velda nervous with dissolve
    v "Теперь я немного раздражена."
    c "Нет, ты — Вельда."
    show velda angry with dissolve
    v "Мне тебя пнуть?"
    c "Нет."
    c "Я уже заткнусь."
    show velda normal with dissolve
    v "Хорошо."
    jump veldawantstoknowday7

label notaboutyouvelda:
    c "Мы не говорили ни о чём важном."
    show velda nervous with dissolve
    v "Правда?"
    c "Да."
    c "Я бы когда-нибудь тебе соврал?"
    show velda normal with dissolve
    v "Возможно."
    c "Ты сомневаешься во мне?"
    show velda frown with dissolve
    v "Я не доверяю большинству людей."
    c "Понятно."
    jump veldawantstoknowday7

label veldawantstoknowday7:
    show velda nervous with dissolve
    v "Наверное, мне не стоило спрашивать."
    c "Но ты хотела знать."
    show velda frown with dissolve
    v "Хотела, но... "
    show velda nervous with dissolve
    v "А-а!"
    show velda angry with dissolve
    v "Хватит уже!"
    c "Ладно."
    show velda nervous with dissolve
    v "Ты не забыл о том, что я сказала?"
    c "Нет."
    show velda smile with dissolve
    v "Хорошо."
    show velda normal with dissolve
    v "Тогда встретимся позже."
    c "Да."
    stop music fadeout 1.0
##################################################################

    play music calm
    scene bg park day 2 with fade
    x "Вельда попросила меня прийти в парк."
    x "Я уже здесь, но Вельды не видно."
    x "Она опаздывает?"
    x "Или делает это нарочно?"
    x "Что, если она не придёт?"
    show velda normal with dissolve
    v "Прости, что опоздала."
    show velda nervous with dissolve
    v "Ты долго ждал?"
    c "Я только что пришёл."
    show velda frown with dissolve
    v "Я знаю, что это ложь."
    c "Прошло всего пятнадцать минут."
    c "Это не то чтобы ты опоздала на час."
    show velda nervous with dissolve
    v "Прости."
    c "Ты курила?"
    show velda angry with dissolve
    v "Не так громко!"
    c "А, прости."
    show velda nervous with dissolve
    v "Может, и курила..."
    c "Так о чём ты хотела поговорить?"

    if veldabad >= 3:
        jump veldabadend1
    else:
        jump veldanormalpath

label veldabadend1:

    stop music fadeout 1.0
    play music regrets

    show velda frown with dissolve
    v "Прости."
    c "Прости за что?"
    show velda nervous with dissolve
    v "Нам не стоит быть вместе."
    c "Что ты несёшь?"
    show velda frown with dissolve
    v "Если ты будешь рядом со мной, тебе будет плохо."
    show velda nervous with dissolve
    v "Так что... пожалуйста, перестань со мной разговаривать."
    c "Я не понимаю."
    show velda normal with dissolve
    v "Я... нехороший человек."
    show velda nervous with dissolve
    v "Если люди узнают, что ты всё время рядом со мной, они о тебе плохо подумают."
    show velda normal with dissolve
    v "Найди других людей, с которыми можно быть."
    c "Я всё ещё не-"
    show velda nervous with dissolve
    v "Я... уеду из этого города."
    c "Что?"
    show velda frown with dissolve
    v "И не вернусь."
    show velda normal with dissolve
    v "Так будет лучше."
    c "Ты правда думаешь, что так будет лучше?"
    c "Это чушь!"
    show velda nervous with dissolve
    v "Может, ты так думаешь... но так лучше."
    show velda frown with dissolve
    v "Будет лучше, если мы больше не увидимся."
    hide velda frown with dissolve
    play sound walkingoutside
    x "Вельда разворачивается и начинает уходить."
    stop sound fadeout 1.0
    c "Подожди!"
    c "Вернись!"
    x "Она не отвечает ни на что."
    c "Вельда!"
    x "Это был последний раз, когда я её видел."
    x "Остаток каникул я чувствовал себя опустошённым."
    x "Казалось, что чего-то или кого-то не хватает."
    x "Без неё всё было не так."
    stop music fadeout 1.0
    $ achievement.grant("Velda_Leaves")
    x "ПЛОХАЯ КОНЦОВКА — ВЕЛЬДА УЕЗЖАЕТ"
    # Титры нейтральной концовки
    hide velda frown with dissolve
    $ renpy.movie_cutscene("video/NeutralCredits.webm", delay=100, loops=0, stop_music=True)
    return

label veldanormalpath:

    stop music fadeout 1.0
    play music bittersweet
    v "Это о том, что ты сказал раньше."

    if confesstovelda == True:
        jump veldarespondstoconfession
    elif friendswithvelda == True:
        jump veldarespondstofriendship
    else:
        jump veldawantstobefriends

label veldarespondstoconfession:
    show velda normal with dissolve
    v "Я знаю, ты сказал, что я тебе нравлюсь."
    show velda nervous with dissolve
    v "Но... мне всё ещё нужно время."
    c "Ты могла бы просто подождать."
    show velda nervous with dissolve
    v "Прости."
    c "Всё в порядке."
    jump veldaparkday7over

label veldarespondstofriendship:
    show velda normal with dissolve
    v "Ты нормальный парень."
    c "Что это значит?"
    show velda smile with dissolve
    v "Я рада, что у меня есть такой друг."
    c "Правда?"
    show velda nervous with dissolve
    v "Не накручивай себе. Я просто сказала, что ты друг."
    c "Хех."
    jump veldaparkday7over

label veldawantstobefriends:
    show velda normal with dissolve
    v "Хотела бы, чтобы мы были друзьями!"
    c "О?"
    c "Что ж, я уже считал нас друзьями..."
    show velda nervous with dissolve
    v "..."
    show velda frown with dissolve
    v "Боже, теперь я чувствую себя дурой."
    c "Не переживай об этом."
    jump veldaparkday7over

label veldaparkday7over:
    c "Это всё, о чём ты хотела поговорить?"
    show velda normal with dissolve
    v "Да."
    show velda smile with dissolve
    v "Спасибо, что выслушал."
    c "Без проблем."

    stop music fadeout 1.0

    show velda nervous with dissolve
    v "Эм..."
    c "Что такое?"
    show velda normal with dissolve
    v "Я могла бы также рассказать тебе кое-что."
    c "Х-Хорошо."
    show velda nervous with dissolve
    v "Это важно."
    show velda angry with dissolve
    v "Так что лучше слушай!"
    c "Буду."

    play music sadpast

    show velda normal with dissolve
    v "Когда-то у меня всё было довольно обычно."
    show velda frown with dissolve
    v "Когда я была младше, мои родители погибли."
    show velda nervous with dissolve
    v "Как именно они погибли, так и не выяснили."
    show velda frown with dissolve
    v "Всё, что известно — их убили."
    show velda nervous with dissolve
    v "Так что у меня, по сути, не было родителей."
    show velda normal with dissolve
    v "Какое-то время меня приютили родственники, но я скоро ушла от них."
    show velda nervous with dissolve
    v "После ухода от них я стала жить одна."
    show velda frown with dissolve
    v "Было нелегко."
    show velda nervous with dissolve
    v "Я часто нервничала, связалась с плохой компанией и начала курить."
    show velda frown with dissolve
    v "Но... мне надоела такая жизнь."
    show velda normal with dissolve
    v "Я решила, что хочу измениться."
    show velda smile with dissolve
    v "Так что я ушла от тех людей."
    show velda normal with dissolve
    v "После ухода я хотела начать относиться к жизни серьёзно, поэтому попробовала найти работу."
    show velda frown with dissolve
    v "Большинство мест отказали мне из-за моего прошлого."
    show velda nervous with dissolve
    v "Твой дядя был первым, кто не стал спрашивать об этом."
    show velda normal with dissolve
    v "Он просто нанял меня без всяких вопросов."
    show velda smile with dissolve
    v "И вот так я оказалась там, где сейчас."
    c "..."
    show velda normal with dissolve
    v "Вот что я хотела сказать."
    c "..."
    show velda nervous with dissolve
    v "Что?"
    c "Я просто не знаю, что ответить."
    show velda nervous with dissolve
    v "Тогда не отвечай."
    c "Но тогда мне будет плохо."
    show velda normal with dissolve
    v "Не переживай об этом."
    show velda nervous with dissolve
    v "Это всё в прошлом."
    show velda normal with dissolve
    v "Ты ничего не можешь с этим поделать."
    c "Наверное."
    show velda smile with dissolve
    v "Что ж, я иду домой."
    show velda normal with dissolve
    v "Увидимся завтра."
    c "Да…"
    hide velda normal with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg downtown evening with fade
    play sound walkingoutside
    x "Вместо того чтобы сразу идти домой, я брожу по городу."
    x "Думаю, я зашёл слишком далеко, потому что не очень знаком с этим районом."
    stop sound fadeout 1.0

    play music youdontbelong

    sg "Что ты делаешь здесь так поздно?"
    c "О, просто гуляю."
    sg "Тебе следует быть осторожнее."
    c "Учту."
    sg "Никогда не знаешь, на каких людей можешь наткнуться."
    c "Я-Я знаю."
    sg "Так..."
    c "Чего ты хочешь?"
    sg "Что ты делаешь с этой девушкой?"
    c "С какой девушкой?"
    c "О чём ты?"
    sg "Не прикидывайся дурачком со мной!"
    sg "Ты знаешь, о ком я говорю."
    c "Нет, не знаю."
    sg "Парень, я тебе сейчас лицо разобью."
    c "Я правда не знаю, о чём ты."
    sg "Эта девушка, с которой ты всегда!"
    c "Вельда?"
    c "Откуда ты её знаешь?"
    sg "Скажем так, мы... знакомы."
    c "И что это имеет отношение ко мне?"
    sg "Связываться с ней опасно, знаешь ли?"
    c "Спасибо за предупреждение."
    sg "О, думаешь уйти?"
    c "Ну, мне нужно домой."
    c "Дядя ждёт, чтобы я приступил к работе."
    sg "Так ты примерный мальчик, делаешь всё, что дядя просит, да?"
    c "Мне нужно поспать."
    c "Если не посплю, у меня не будет сил работать завтра."
    sg "Ты вообще слушаешь, что я говорю?"
    c "Да."
    c "Но ты слушаешь, что я говорю?"
    sg "Нет, потому что ты должен слушать МЕНЯ!"
    c "Слишком злиться вредно для тебя."
    sg "Тогда перестань меня бесить."
    c "Разве не ты начал?"
    sg "Всё, хватит."
    sg "Я больше не могу!"
    sg "Я тебе сейчас задницу надру!"
    stop music fadeout 1.0
    x "Наверное, не стоило заходить так далеко."
    x "Чёрт."
    x "Что мне теперь делать?"

menu:

    "Думать о Вельде":
        jump thinkaboutveldaday7

    "Попробовать подраться":
        jump trytofightday7

    "Ничего не делать":
        jump notrytofightday7

label thinkaboutveldaday7:
    $ veldapoints += 1
    x "Вельда..."
    x "Интересно, что она сейчас делает."
    x "Подожди."
    $ achievement.grant("Velda_Thought")
    x "Почему я думаю о ней в такой момент!?"
    jump veldasavescaron

label trytofightday7:
    x "Я... должен защитить себя."
    x "Готовлюсь к драке."
    x "Смогу... я реально это сделать?"
    jump veldasavescaron

label notrytofightday7:
    x "Я не боец."
    x "Не стоило его дразнить."
    x "Я идиот."
    jump veldasavescaron

label veldasavescaron:

    play music gangbattle

    show velda angry with dissolve
    v "Что, чёрт возьми, ты делаешь!?"
    sg "Ты..."
    show velda nervous with dissolve
    v "Отпусти его."
    sg "О, успокойся."
    sg "Я просто болтаю с твоим парнем."
    show velda frown with dissolve
    v "Он не мой парень."
    sg "Тогда тебе не должно быть дела до того, что я с ним делаю."
    show velda nervous with dissolve
    v "Ты же только что сказал, что просто болтаешь?"
    sg "Ты прекрасно знаешь, что я имею в виду под такими словами, предательница!"
    c "Предательница?"
    show velda angry with dissolve
    v "Заткнись!"
    play sound kick
    x "Она прыгает на странного парня и бьёт его ногой в лицо."
    stop sound fadeout 1.0
    x "Он отпускает меня от боли."
    sg "Ты... стерва!"
    show velda nervous with dissolve
    v "Хочешь ещё!?"

    stop music fadeout 1.0

    sg "..."
    sg "Хех."
    sg "Вам двоим лучше за собой следить."
    x "Затем парень разворачивается и уходит."

    play music bittersweet

    show velda frown with dissolve
    v "Ты в порядке, Карон?"
    c "Я в порядке, спасибо тебе."
    show velda nervous with dissolve
    v "О чём, чёрт возьми, ты думал!?"
    c "Не знаю."
    c "Я гулял какое-то время и заблудился."
    c "Потом, похоже, разозлил того парня."
    show velda angry with dissolve
    v "Зачем ты вообще с ним заговорил!?"
    c "Это он начал."
    c "И в чём твоя проблема?"
    show velda nervous with dissolve
    v "Что ты имеешь в виду?"
    c "Ты — причина, по которой он вообще хотел со мной поговорить."
    c "И что значит «предательница»?"
    show velda frown with dissolve
    v "Думаю, мне стоит тебе рассказать."
    show velda normal with dissolve
    v "Я говорила тебе раньше, что связалась с плохой компанией..."
    show velda nervous with dissolve
    v "Какое-то время я была в банде."
    show velda normal with dissolve
    v "И была довольно жёсткой."
    show velda frown with dissolve
    v "Однако большинство людей боялись меня из-за этого."
    show velda nervous with dissolve
    v "Даже когда я решила уйти, люди всё ещё считали меня монстром."
    show velda frown with dissolve
    v "Мне надоело быть в банде."
    show velda normal with dissolve
    v "Я знала, что это неправильно, и не хотела больше марать руки."
    show velda frown with dissolve
    v "Они были недовольны тем, что я ушла."
    show velda nervous with dissolve
    v "Они пытались приходить за мной больше одного раза."
    show velda normal with dissolve
    v "Но каждый раз у них не получалось."
    show velda nervous with dissolve
    v "Вот почему я не хочу сближаться с людьми."
    show velda frown with dissolve
    v "Потому что... они думают, что победят, причинив боль тем, кто мне дорог."
    c "Так вот почему ты так разговариваешь."
    show velda nervous with dissolve
    v "Да, чтобы ты не ввязывался."
    c "А как же Гвен?"
    show velda frown with dissolve
    v "Я не могу так с ней."
    show velda normal with dissolve
    v "Она... моя единственная семья."
    c "Что ты имеешь в виду?"
    show velda nervous with dissolve
    v "Гвен на самом деле моя кузина."
    c "...!"
    c "Правда?"
    show velda normal with dissolve
    v "Да."
    show velda nervous with dissolve
    v "У неё также есть брат, но он в больнице с неизлечимой болезнью."
    show velda frown with dissolve
    v "Похоже, он не проживёт слишком долго."
    show velda nervous with dissolve
    v "Так что... она, по сути, моя единственная семья."
    c "А как же...?"
    show velda frown with dissolve
    v "Она тоже потеряла родителей."
    c "Ох."
    show velda normal with dissolve
    v "Почему бы тебе не пойти домой?"
    show velda nervous with dissolve
    v "Я не хочу, чтобы ты попал в ещё большие неприятности."
    c "Ладно."
    hide velda nervous with dissolve
##################################################################

    play music stressful
    scene bg bedroom with fade
    show velda shock with dissolve
    v "Это ужасно!"
    show velda nervous with dissolve
    v "Просто ужасно!"
    c "Можешь слезть с меня, пожалуйста?"
    show velda frown with dissolve
    v "Неважно!"
    show velda shock with dissolve
    v "Это Гвен!"
    c "Что с ней?"
    show velda frown with dissolve
    v "Она пропала!"
    c "Я мало что могу сделать, пока ты на мне сверху."
    show velda normal with dissolve
    v "О, точно."
    x "Она слезает с меня."
    show velda shock with dissolve
    v "Гвен пропала!"
    c "Я слышу тебя в первый раз."
    show velda nervous with dissolve
    v "Чёрт."
    c "Эм..."
    c "Я помогу тебе её искать."
    show velda frown with dissolve
    v "Нет."
    c "Что?"
    show velda normal with dissolve
    v "Тебе не нужно ввязываться."
    c "Почему ты так говоришь?"
    show velda nervous with dissolve
    v "Не переживай об этом."
    c "Но я волнуюсь!"
    show velda frown with dissolve
    v "После вчерашнего я не хочу, чтобы ты ввязывался в это."
    d "Что за шум?"
    c "Похоже, Гвен пропала."
    d "О, да?"
    d "Честно говоря, она обычно приходит утром."
    d "Однако я не видел её со вчерашнего дня."
    c "Думаешь, что-то случилось?"
    show velda nervous with dissolve
    v "Я иду."
    d "Куда ты идёшь?"
    show velda angry with dissolve
    v "Не переживай за меня!"
    show velda smile with dissolve
    v "И Карон..."
    show velda normal with dissolve
    v "Оставайся здесь."

menu:

    "Остаться":
        jump staybehind_day8

    "Пойти с ней":
        jump gowithveldaday8

label staybehind_day8:

    $ achievement.grant("Stay_Behind")
    c "Ладно."
    c "Я останусь."
    show velda smile with dissolve
    v "Хорошо."
    play sound runninginhall
    hide velda smile with dissolve
    x "Вельда убегает."
    stop sound fadeout 1.0
    d "Стоит волноваться?"
    c "Не знаю."
    c "Наверное, она справится."
##################################################################

    play music snowydays
    scene bg restaurant with fade
    x "Подметаю обеденный зал."
    x "Без Вельды здесь так одиноко..."
    d "Хмм..."
    d "Не чувствуется правильным, да?"
    c "Не особо."
    d "Ты волнуешься за неё, да?"
    c "Да..."
    d "Ну, она же не может не позаботиться о себе."
    d "Наверное, всё будет нормально."
    c "Но что если её ранят...?"
    d "Даже думать об этом не хочу."
    c "Ничего не могу с собой поделать."
    x "Мы замолкаем, и я продолжаю подметать."
    d "Знаешь, ты делаешь ещё больше беспорядка так..."
    c "Правда?"
    d "Ты же не можешь сосредоточиться сейчас, да?"
    c "Я в порядке."
    d "Нет, не в порядке."
    x "Дядя забирает у меня швабру."
    d "Я сам подмету."
    c "Но..."
    d "Нет смысла работать, если ты не сосредоточен."
    x "Вздыхаю."
    d "Иди отдохни."
    c "Ладно."
##################################################################

    stop music fadeout 1.0
    scene bg restaurant with fade
    x "Наступает конец дня."

    play music worryaboutyou

    x "Вельда возвращается с Гвен, но я был прав, что волновался."
    x "Вельда выглядит уставшей, грязной и избитой."
    show velda angry with dissolve
    v "Я же сказала, что справлюсь сама!"
    c "Ну да, справишься."
    c "Выглядишь так, будто тебе досталось."
    show velda nervous with dissolve
    v "Сомневаюсь, что ты бы справился лучше."
    c "Разве не знаешь, что в количестве сила?"
    c "Чувствую, что должен был пойти с тобой."
    show velda normal with dissolve
    v "Да пофиг."
    hide velda normal with dissolve
    show gwen nervous with dissolve
    g "Я голодная..."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Даже после всего этого..."
    c "Так что случилось?"
    show velda frown with dissolve
    v "Банда её похитила."
    c "Она выглядит нормально."
    show velda nervous with dissolve
    v "Да, странно, да?"
    show velda normal with dissolve
    v "Она не испугалась и вообще ничего."
    show velda nervous with dissolve
    v "Вообще-то, она проспала всё это."
    c "П-правда?"
    show velda smile with dissolve
    v "Ага."
    hide velda smile with dissolve
    show gwen frown with dissolve
    g "Нужна еда."
    hide gwen frown with dissolve
    show velda nervous with dissolve
    v "Подожди."
    c "Хех."
    c "Она тебе правда важна, да?"
    show velda normal with dissolve
    v "..."
    show velda smile with dissolve
    v "Да."
    hide velda smile with dissolve
jump day8isover

label gowithveldaday8:

    $ veldapoints += 1
    c "Не будь такой!"
    c "Я иду с тобой!"
    show velda angry with dissolve
    v "Я сказала остаться!"
    c "Я не могу просто остаться здесь!"
    show velda nervous with dissolve
    v "Ладно."
    show velda frown with dissolve
    v "Но не путайся у меня под ногами."
    hide velda frown with dissolve
    $ achievement.grant("GoWith_Velda")
##################################################################

    stop music fadeout 1.0
    scene bg downtown day with fade
    x "Я в незнакомой части города."
    x "Чувствую, что могу легко заблудиться."
    show velda normal with dissolve
    v "Не уходи далеко."
    sg "Так, ты вернулась."
    show velda angry with dissolve
    v "Что ты с ней сделал!?"
    sg "Я ещё ничего не сделал."
    show velda nervous with dissolve
    v "Я убью тебя!"
    sg "Этого не случится."

    play music biggangbattle

    x "Он щёлкает пальцами, и его окружают несколько других мужчин."
    gl "Теперь я здесь главный."
    show velda smile with dissolve
    v "О, значит, так вот как это будет."
    show velda shock with dissolve
    v "Отойди, Карон!"
    c "Х-Хорошо!"
    play sound kick
    x "Его люди идут на неё, но она размашисто бьёт ногой, умудряясь пнуть нескольких одновременно."
    stop sound fadeout 1.0
    gm "Чёрт!"
    gl "Понадобится больше усилий."
    x "Лидер банды идёт на неё, размахивая кулаками."
    x "Вельда уклоняется от каждого удара."
    gl "Позволь мне ударить тебя!"
    show velda angry with dissolve
    v "Нет!"
    play sound kick
    x "Она бьёт его по яйцам."
    gl "Чёрт тебя подери!"
    x "Он падает, и ещё несколько его людей идут на Вельду."
    play sound kick
    x "Она прыгает в воздух и, размахивая ногой, сбивает ещё нескольких."
    gl "Дерьмо."
    show velda nervous with dissolve
    v "Отпусти её."
    gm "Я убью её."
    x "Один из членов банды держит Гвен, которая выглядит спящей, с ножом у горла."
    show velda angry with dissolve
    v "Не смей!"
    gm "Ещё шаг, и я это сделаю!"
    c "Что нам делать?"
    hide velda frown with dissolve
    play sound bite
    gm "А-ай!"
    stop sound fadeout 1.0
    x "Гвен укусила его за руку, и он выронил нож."
    gm "Что за...!?"
    gm "Ты была в сознании!?"
    play sound kick
    x "Тогда Вельда сильно пинает его в голову."
    stop sound fadeout 1.0
    gl "Ещё не всё!"
    x "Лидер бросает удары в мою сторону, и я уклоняюсь."
    x "Затем я бью его по яйцам, и он падает."
    play sound kick
    x "Затем пинаю его в голову."
    play sound thudhard
    x "Его голова ударяется о землю."
    $ caronfaught = True
    stop sound fadeout 1.0
    c "О, чёрт."
    c "Я его убил?"
    show velda nervous with dissolve
    v "Похоже, ты его просто вырубил."
    show velda frown with dissolve
    v "Гвен, ты в порядке?"
    hide velda frown with dissolve
    show gwen normal with dissolve
    g "Я в порядке."
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Очень хочу, чтобы ты остался."
    c "Но я же помог, да?"
    c "К тому же, я не мог оставить тебя одну."
    c "Ты мне не безразлична."
    show velda embarassed with dissolve
    v "..."
    show velda nervous with dissolve
    v "Уходим."
    c "Ладно."
    hide velda nervous with dissolve
    jump day8isover

label day8isover:

    stop music fadeout 1.0
    scene bg bedroom with fade
    x "Это был странный день."
    x "Ну ладно."
    x "Думаю, теперь просто лягу спать и продолжу жить дальше."
    play sound trashbag

    play music hugerealization

    x "Что за чёрт!?"
    c "Кто здесь!?"
    u "Ты идёшь со мной...."
    stop sound fadeout 1.0
##################################################################

# День 9

    scene bg alley with fade
    gl "Ты слишком сближаешься с этой стервой!"
    play sound kick
    x "Он бьёт меня."
    stop sound fadeout 1.0
    c "Ах, почему тебе не всё равно!?"

    if caronfaught == True:
        jump leaderpissedoffatcaron
    else:
        jump leaderpissedoffatvelda

label leaderpissedoffatcaron:
    gl "И после того дерьма, что ты устроил раньше..."
    gl "Как я могу НЕ злиться на тебя."
    play sound kick
    c "Ох!"
    jump leaderpiss

label leaderpissedoffatvelda:
    gl "Эта девушка."
    gl "Я ненавижу её."
    play sound kick
    c "Ай!"
    jump leaderpiss

label leaderpiss:
    stop sound fadeout 1.0
    c "Хватит, ублюдок!"
    c "Я не мог нормально спать из-за тебя прошлой ночью!"
    gl "И это твоя вина, что связался с ней!"
    play sound kick
    c "Н-р-р!"
    stop sound fadeout 1.0
    x "Боль."
    x "Так больно..."
    x "Так много..."
    play sound choke
    x "Кашляю."
    x "Это... кровь?"
    x "Чёрт."
    x "Этот парень действительно собирается забить меня до смерти, да?"
    play sound kick
    scene bg black with fade
    x "Он сильно бьёт меня в голову, и потом я вижу только тьму."
    stop sound fadeout 1.0

    stop music fadeout 1.0

    x "Это... смерть?"
    x "Я умер?"
    x "Эм... разве нет загробной жизни или чего-то такого?"
    x "Подождите... боль."
    x "Я всё ещё её чувствую."
    x "Думаю, я не мёртв."
    x "Мои глаза медленно открываются."
    scene bg alley with fade
    show velda nervous with dissolve
    x "Передо мной знакомая девушка."
    c "В-Вельда?"
    play sound sirens
    x "Слышу сирены вдалеке."
    c "Спасибо... тебе..."
    hide velda nervous with dissolve
    stop sound fadeout 1.0
    scene bg black with fade
    x "Я потерял сознание."

##################################################################

    play music happyending
    scene bg hospital room day with fade
    x "Я в больнице."
    x "Боже, мне всё ещё больно."
    x "Не могу поверить, что пропустил самое интересное."
    x "Вельда пришла и надрала всем задницы, пока я был без сознания."
    d "Ты наконец проснулся."
    c "Что случилось?"
    d "Похоже, ты подрался."
    d "Были сообщения о возросшей активности банд в городе, и, видимо, они вломились в дом прошлой ночью."
    d "Ты бы это видел."
    d "Вельда была в панике, когда ты пропал."
    c "Правда?"
    show gwen normal with dissolve
    g "Да."
    show gwen shock with dissolve
    g "Она правда волновалась за тебя!"
    c "Когда ты успела прийти?"
    d "Она была здесь всё это время."
    show gwen normal with dissolve
    g "Я видела, как тебя сюда привезли, и мне нужно было убедиться, что ты в порядке."
    c "Ты уже была здесь?"
    show gwen smile with dissolve
    g "Да."
    show gwen nervous with dissolve
    g "Я была здесь, чтобы навестить кое-кого..."
    x "Наверное, её брата."
    show gwen smile with dissolve
    g "Я просто рада, что ты в порядке."
    show gwen frown with dissolve
    g "Даже не хочу думать, что бы сделала Вельда, если бы ты умер."
    c "Эм..."
    c "Когда ты так говоришь, мне правда становится не по себе."
    hide gwen frown with dissolve
    c "Кстати о Вельде, где она?"
    d "Ну, после той драки..."
    d "Полиция забрала её на допрос."
    c "...Ох."
    d "Что касается тебя, ты, скорее всего, пробудешь здесь пару дней."
    c "Что ж, отстой."
    d "У меня будет не хватать двух работников."
    d "Что думаешь, Гвен?"
    d "Ты можешь начать работать на меня сегодня!"
    show gwen shock with dissolve
    g "Э-э!?"
    c "Ого, нельзя же просто так сваливать это на неё."
    show gwen normal with dissolve
    g "В-Всё нормально."
    show gwen smile with dissolve
    g "Я сделаю это."
    show gwen normal with dissolve
    g "По крайней мере, пока Вельда не вернётся."
    c "Ладно."
    hide gwen normal with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg hospital room night with fade
    x "Наступает ночь, и я один в больничной палате."
    x "Многое произошло с тех пор, как я приехал в этот город."
    x "Просто не ожидал, что меня изобьют."
    x "Всё ещё болит... но хотя бы я выжил."
    x "Должен быть благодарен, что не умер."
    x "Вельда спасла меня, да?"
    x "Было бы хуже, если бы она не пришла."

menu:

    "Я рад, что это была она":
        jump gladitwasher

    "Я не хотел ввязываться":
        jump caughtupinthis

    "Я просто рад, что жив":
        jump gladtobealive

    "Я благодарен":
        jump gratefultovelda

label gladitwasher:
    $ veldapoints += 1
    x "Я рад, что это была она."
    x "Правда рад, что она в моей жизни."
    x "Даже если она иногда... не очень милая."
    x "В целом она не плохой человек."
    jump finalveldachoice

label caughtupinthis:
    $ veldabad += 1
    x "Ненавижу, что меня втянули в это."
    x "Зачем мне вообще было связываться с ней?"
    x "Знакомство с ней было ошибкой?"
    x "С тех пор я просто магнит для неприятностей."
    jump finalveldachoice

label gladtobealive:
    x "Я просто рад, что жив."
    x "Это была заварушка, в которую я попал."
    x "К счастью, Вельда спасла мне задницу."
    x "Хотя я бы предпочёл не ввязываться в такое."
    jump finalveldachoice

label gratefultovelda:
    $ veldapoints += 1
    x "Я ей благодарен."
    x "Она спасла мне жизнь."
    x "Если бы она не пришла, не знаю, выжил бы я."
    x "Никогда не ожидал многого от неё, когда мы впервые встретились."
    jump finalveldachoice

    label finalveldachoice:
    x "Я устаю."
    x "Почему бы мне не пойти поспать?"
    x "Хотя, наверное, это единственное, что я могу сейчас сделать."
    x "Пройдёт какое-то время, прежде чем я смогу пойти домой."
##################################################################

    # День 10 (прошло несколько дней)#

    play music problemsolved
    scene bg restaurant with fade
    x "Прошло несколько дней, и наконец я смог вернуться домой."
    x "Ну, это дом дяди."
    x "Я же здесь только на каникулах."
    show gwen normal with dissolve
    g "Как ты себя чувствуешь?"
    c "Гораздо лучше."
    c "А ты?"
    c "Ты же несколько дней работала за кузину."
    show gwen smile with dissolve
    g "Да..."
    show gwen normal with dissolve
    g "У меня всё хорошо."
    hide gwen normal with dissolve
    d "Вижу, вы двое усердно работаете."
    d "Или нет?"
    d "В последнее время не могу разобрать."
    c "А ты?"
    c "Я не вижу, чтобы ты большую часть времени работал."
    d "Эй, у меня есть обязанности менеджера!"
    c "Например, стоять без дела?"
    d "И выглядеть устрашающе!"
    c "Ты не выглядишь особо устрашающе..."
    d "Заткнись!"
    d "Дай мне это!"
    x "Гвен просто смеётся."
    d "О, точно."
    d "У меня кое-что для тебя есть."
    c "Что?"
    x "Он даёт мне письмо."
    d "Это от Вельды."
    c "Мне?"
    show gwen angry with dissolve
    g "Нечестно!"
    x "Я открываю его."
    hide gwen angry with dissolve
    v "Прости, не могу поговорить с тобой лично."
    v "Могла бы подождать, пока срок не выйдет, но хотела связаться с тобой."
    v "После той драки с бандой меня допросили, и теперь я под домашним арестом."
    v "Пройдёт какое-то время, прежде чем я смогу снова выйти."
    v "Прости за это."
    v "Но хотя бы у тебя всё хорошо."
    v "Каждый член банды был пойман."
    v "Им предъявлены обвинения в нападении, покушении на убийство и убийстве."
    v "Похоже, один из их членов был виновен в смерти моих родителей."
    v "Он создавал проблемы, и мои родители противостояли ему."
    v "Но он разозлился, и что произошло, ты можешь представить."
    v "Я не знала об этом до недавнего времени."
    v "Похоже, у полиции было достаточно улик, чтобы связать банду со всем."
    v "И есть ещё одна вещь, которую я хотела бы тебе сказать."
    stop music fadeout 1.0

    if veldapoints >= 8:
        jump veldaromanceending
    elif veldabad >= 3:
        jump veldaworstending
    else:
        jump veldafriendending

label veldaworstending:

    play music dontwanttokeepdoingthis
    v "Думаю, нам больше не стоит видеться."
    v "С тех пор как ты меня узнал, для тебя были только неприятности."
    v "Я просто не хочу, чтобы ты больше ввязывался."
    v "Наверное, я не вернусь в ресторан."
    v "Так что позаботься о Гвен за меня."
    v "Без меня тебе будет лучше."
    c "Что?"
    c "Ты шутишь."
    show gwen nervous with dissolve
    g "Что случилось?"
    play sound sniffle
    c "Я..."
    show gwen frown with dissolve
    g "Ты... плачешь?"
    c "Плачу?"
    x "Подношу руку к лицу."
    c "Хм."
    c "Похоже, что да."
    hide gwen frown with dissolve
    x "Мы больше никогда не видели Вельду."
    x "Мне самому было паршиво, но Гвен это приняла очень тяжело."
    x "Неужели всё должно было закончиться именно так?"
    stop music fadeout 1.0
    $ achievement.grant("Velda_Dead")
    x "ХУДШАЯ КОНЦОВКА — ВЕЛЬДА НИКОГДА НЕ ВЕРНЁТСЯ"
    # Титры плохой концовки
    $ renpy.movie_cutscene("video/BadCredits.webm", delay=95, loops=0, stop_music=True)
    return

label veldafriendending:

    v "Правда рада, что встретила тебя."
    play music friendship

    if confesstovelda == True:
        jump veldafriendzone
    elif friendswithvelda == True:
        jump veldafriendzone2
    else:
        jump veldafriendzone3

label veldafriendzone:
    v "Прости, не могу ответить тебе взаимностью."
    v "Но... хотела бы остаться друзьями."
    jump veldafriendzoneover

label veldafriendzone2:
    v "Не знаю, почему ты хотел дружить с такой, как я."
    v "Но я рада, что мы друзья."
    jump veldafriendzoneover

label veldafriendzone3:
    v "Правда, я это имею в виду."
    v "Только не пойми неправильно."
    jump veldafriendzoneover

label veldafriendzoneover:
    v "Просто хочу, чтобы ты знал — ты мой лучший друг."
    v "Уф, было немного неловко это писать."
    v "Но всё же ты правда важен для меня."
    v "Знаю, я говорила обидные вещи в прошлом."
    v "Так что прости меня за это."
    v "Я буду счастлива, пока ты рядом."
    v "Надеюсь, скоро увидимся."
    c "Вот как она чувствует."
    show gwen nervous with dissolve
    g "Что случилось?"
    c "О, ничего."
    c "Не могу дождаться, когда снова её увижу."
    show gwen smile with dissolve
    g "Да..."
    hide gwen smile with dissolve
    x "Мы вдвоём с нетерпением ждали возвращения Вельды."
    x "Когда этот день наконец настал, это были самые счастливые дни в нашей жизни."
    stop music fadeout 1.0
    $ persistent.veldafriendshipclear = True
    $ achievement.grant("Velda_Friendship")
    x "КОНЦОВКА ДРУЖБЫ — ВЕЛЬДА"
    # Титры концовки дружбы
    $ renpy.movie_cutscene("video/FriendCredits.webm", delay=85, loops=0, stop_music=True)
    return

label veldaromanceending:

    v "Правда рада, что встретила тебя."
    play music loveconfess

    if confesstovelda == True:
        jump acceptfeelingsvelda
    elif friendswithvelda == True:
        jump wantsmorevelda
    else:
        jump confesstoyouvelda

label acceptfeelingsvelda:
    v "Честно говоря, поняла, что ты тоже мне нравишься."
    v "Я... влюблена в тебя."
    jump veldafeelingsover

label wantsmorevelda:
    v "Рада, что ты хотел быть моим другом, но я хочу большего."
    v "Ты правда, правда нравишься мне, Карон."
    jump veldafeelingsover

label confesstoyouvelda:
    v "Честно говоря, думаю, я влюбилась в тебя."
    v "И я не шучу!"
    jump veldafeelingsover

label veldafeelingsover:
    v "Не знаю, как давно я это чувствую."
    v "Прежде чем я это поняла, не могла перестать думать о тебе."
    v "И от этого у меня болит в груди."
    v "Боже, это так неловко..."
    v "Что ж, я люблю тебя."
    v "Правда с нетерпением жду, когда снова тебя увижу."
    v "Надеюсь, это будет скоро."
    c "Так она чувствует то же самое..."
    show gwen nervous with dissolve
    g "Так вы двое теперь будете встречаться!?"
    c "Наверное."
    show gwen angry with dissolve
    g "Если ты её обидишь, я тебя не прощу!"
    c "Когда это вы с ней поменялись?"
    hide gwen angry with dissolve
    x "Мы вдвоём смеёмся после этого."
    x "День, когда Вельда вернётся, в конце концов настанет, и мы официально станем парой."
    stop music fadeout 1.0
    $ persistent.veldaromanceclear = True
    $ achievement.grant("Velda_Romance")
    x "РОМАНТИЧЕСКАЯ КОНЦОВКА — ВЕЛЬДА"
    # Титры романтической концовки
    $ renpy.movie_cutscene("video/LoveCredits.webm", delay=69, loops=0, stop_music=True)
    return
