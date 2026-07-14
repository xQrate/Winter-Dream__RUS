label liferoutestart:

# День 1 #
    play music snowydays
    scene bg street 2 snow day with fade

    x "Я делаю глубокий вдох, впитывая знакомые пейзажи."
    x "Прошло много времени с тех пор, как я был в этом городе."
    x "Это ощущается как ностальгия, но я, честно говоря, не помню, когда был здесь в последний раз."
    x "Должно быть, моя память уже не та, что раньше."
    x "Меня зовут Карон Дафф, и я буду жить у своего дяди во время зимних каникул."
    x "Хммм.... почему-то у меня чувство, что я уже через это проходил."
    x "Наверное, мне это просто кажется."
    x "В любом случае, я почти уверен, что дядя заставит меня работать."
    x "По крайней мере, мне будет чем заняться."
    x "Глядя в небо, я рад, что уехал из дома."
    x "Я не ненавижу его, но уезжать время от времени — это здорово."
    x "Пока я иду через город, я осматриваюсь, вижу каждое здание, и у меня ощущение, что они не изменились с моего последнего визита."
    x "В конце концов я добираюсь до дома дяди."
##################################################################

    play music normalday
    scene bg restaurant with fade
    x "Зайдя в здание, я не вижу там много людей."
    x "Первый человек, которого я вижу — девушка примерно моего возраста."
    c "Эй, привет."
    show velda shock with dissolve
    ug "...!"
    c "Меня зовут Карон."
    c "А тебя?"
    show velda normal with dissolve
    v "Вельда..."
    show velda nervous with dissolve
    v "Ты племянник Дэниела...?"
    c "Ага."
    show velda normal with dissolve
    v "Понятно."
    show velda nervous with dissolve
    v "Думаю, мы будем часто видеться."
    show velda normal with dissolve
    v "Раз уж я тут работаю."
    c "Да."
    c "Эм... ты в порядке?"
    show velda frown with dissolve
    v "А?"
    show velda nervous with dissolve
    v "О, я в порядке."
    show velda frown with dissolve
    v "Не задавай слишком много вопросов, парень."
    show velda angry with dissolve
    v "Если будешь — пожалеешь!"
    c "О, ладно."
    c "Тогда прости, что спросил."
    c "Что ж, увидимся."
    show velda normal with dissolve
    v "Д-Да."
    x "Может, её что-то беспокоит?"
    hide velda normal with dissolve
##################################################################
    scene bg living room with fade
    x "Вскоре я нахожу своего дядю."
    d "Так ты наконец здесь..."
    d "Ты выглядишь... именно так, как я и думал."
    c "Правда?"
    c "Мы давно не виделись, да?"
    d "Наверное... но твоя мать присылала мне фотографии."
    x "Затем он вздыхает."
    c "Что-то случилось?"
    d "С чего ты взял?"
    c "Просто ты выглядишь уставшим. Вот и всё."
    d "Я в порядке."
    d "Ты уже встретил Вельду?"
    c "Да."
    d "Понятно."
    d "Эм... можешь пойти распаковать свои вещи."
    c "Ладно..."
    stop music fadeout 1.0
##################################################################

    play music calm
    scene bg bedroom with fade
    x "Эти двое странно себя ведут с тех пор, как я приехал."
    x "Интересно, что происходит...?"
    x "Что ж, лучше распаковать вещи, как дядя и сказал."
    x "Не знаю, смогу ли я привыкнуть к тому, что они так себя ведут."
    x "Моё присутствие их раздражает?"
    x "Очень надеюсь, что это не так."
    x "В любом случае, не стоит слишком переживать."
    x "Я буду жить здесь, так что лучше привыкнуть к своей жизни."
    x "А потом я ложусь спать пораньше."
    stop music fadeout 1.0

##################################################################

    #День 2#
    scene bg bedroom with fade
    x "Утро."
    x "Почему мне кажется, что что-то должно произойти?"
    x "Я распаковал все свои вещи, но по какой-то причине моя комната ощущается пустой."
    x "Что это?"
    x "Может, в этом месте что-то не так?"
##################################################################

    play music morningactivity
    scene bg restaurant with fade
    d "Тебе нравится твоя комната?"
    c "Нормальная."
    c "Но... мне кажется, чего-то не хватает."
    d "Правда?"
    c "Да."
    d "И как ты думаешь, что ей нужно?"
    c "Понятия не имею."
    d "Тогда я ничем не могу помочь."
    c "Прости."
    d "Не переживай об этом."
    show velda frown with dissolve
    v "Ты собираешься выйти отсюда когда-нибудь в этом году?"
    show velda nervous with dissolve
    v "Мне уже надоело смотреть на твоё лицо."
    c "Но мы же впервые встретились только вчера."
    show velda angry with dissolve
    v "Одного дня хватило."
    hide velda frown with dissolve
    d "О, точно."
    d "Почему бы тебе не выйти на улицу?"
    c "Тебе не нужна моя помощь в ресторане?"
    d "Нет."
    c "Ладно..."
    d "Вероятно, тебе нужно лучше узнать окрестности."
    c "Наверное..."
##################################################################
    scene bg street 2 day with fade
    x "Я вышел, как он и попросил."
    x "Хм..."
    x "Почему мне кажется, что я это уже делал?"
    x "Всё вокруг кажется таким знакомым."
    x "Всё должно быть для меня новым, но у меня чувство, что я делал это сотни раз."
    x "На ходу я встречаю девушку."
    x "Она выглядит немного знакомо, если подумать..."
    stop music fadeout 1.0
    c "Эм... простите?"
    show gwen shock with dissolve
    ug "Ах!"
    show gwen frown with dissolve
    ug "Кар-"
    c "Эм... можно задать вопрос?"

    play music worryaboutyou

    x "Её глаза начинают наполняться слезами."
    c "Что случилось?"
    x "Слёзы быстро катятся по её щекам."
    c "Серьёзно, что не так?"
    play sound running
    hide gwen frown with dissolve
    x "Затем она разворачивается и убегает, плача."
    x "Я чешу затылок."
    stop sound fadeout 1.0
    c "Чёрт."
    c "Что со всеми в этом городе?"
    stop music fadeout 1.0
##################################################################

    scene bg park 2 day with fade
    x "Я теперь в парке."
    x "Это место... оно согревает меня изнутри."
    x "Почему?"
    play music rosetheme
    show rose normal with dissolve
    ug "Ты тут новенький?"
    show rose nervous with dissolve
    ug "Я... не видела тебя раньше."
    x "Я смотрю на девушку, которая внезапно заговорила со мной."
    x "Она выглядит грустной."
    show rose normal with dissolve
    r "Я Роуз."
    show rose smile with dissolve
    r "А ты?"
    c "Карон."
    show rose nervous with dissolve
    r "Я... поняла."
    c "Что случилось?"
    show rose frown with dissolve
    r "Похоже, что у меня что-то не так?"
    c "Прости, что спросил."
    show rose smile with dissolve
    r "Не переживай об этом."
    show rose normal with dissolve
    r "Что ж, надеюсь, тебе тут понравится."
    stop music fadeout 1.0
    play sound walkingoutside
    hide rose normal with dissolve
    x "Затем она отворачивается и уходит."
    c "А, да."
    stop sound fadeout 1.0
##################################################################

    play music gwentheme
    scene bg restaurant with fade

    c "Я вернулся."
    show velda nervous with dissolve
    v "Д-Добро пожаловать."
    hide velda nervous with dissolve
    show gwen frown with dissolve
    play sound sniffle
    ug "*всхлип*"
    stop sound fadeout 1.0
    c "А с НЕЙ что?"
    hide gwen frown with dissolve
    show velda nervous with dissolve
    v "Я... не знаю."
    x "Она отводит взгляд."
    x "Я вздыхаю и подхожу к плачущей девушке."
    c "Эй."
    c "Ты в порядке?"
    hide velda nervous with dissolve
    show gwen frown with dissolve
    play sound sniffle
    ug "Я... *всхлип*... в порядке."
    stop sound fadeout 1.0
    c "Почему ты заплакала?"
    show gwen nervous with dissolve
    ug "Без причины..."
    c "Правда?"
    hide gwen nervous with dissolve
    show velda angry with dissolve
    v "Не приставай к ней."
    c "Х-Хорошо."
    c "В общем, я Карон."
    c "А тебя как зовут?"
    hide velda angry with dissolve
    show gwen nervous with dissolve
    g "Гвен..."
    c "Ты точно в порядке?"
    show gwen frown with dissolve
    g "Можешь, пожалуйста, оставить меня в покое?"
    c "А, ладно."
    c "Я... так и сделаю."
    hide gwen frown with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg living room with fade
    c "Что значит, у тебя для меня нет работы?"
    d "Именно то, что я сказал."

menu:

    "Я понимаю":
        jump iunderstanduncle

    "Ты серьёзно?!":
        jump cantbeseriousuncle

    "Да пофиг":
        jump whateveruncle

label iunderstanduncle:
    c "Я понимаю."
    d "Хорошо."
    jump liferouteday2continues

label cantbeseriousuncle:
    c "Ты серьёзно!"
    d "Да."
    c "..."
    jump liferouteday2continues

label whateveruncle:
    c "Да пофиг."
    c "Думаю, это не имеет значения."
    jump liferouteday2continues

label liferouteday2continues:
    c "Всё же... я правда думал, что у тебя найдётся для меня работа."
    d "Прости, но мы справляемся сами."
    d "Хотя, может быть, есть другие места, где нужны подработки."
    d "Почему бы тебе не попробовать?"
    c "Думаю, я подумаю об этом."
    c "В любом случае, сегодня был странный день."
    c "Так что я пойду спать."
    d "Уверен?"
    d "Ещё довольно рано."
    c "Да."
    c "Увидимся завтра."
    d "Ладно."
##################################################################

    #День 3#
    scene bg bedroom with fade

    x "Когда я просыпаюсь на следующее утро, моя спальня всё ещё кажется пустой."
    x "Почему мне кажется, что чего-то не хватает?"
    x "Ну ладно."
    x "Я потягиваюсь, затем выпрыгиваю из кровати и одеваюсь."
##################################################################

    play music snowydays
    scene bg restaurant with fade
    d "Доброе утро, Карон."
    c "Утро."
    show velda nervous with dissolve
    v "..."
    c "Что с ней?"
    show velda frown with dissolve
    v "Мне снова приходится смотреть на твоё уродливое лицо."
    c "Оу."
    d "Не обращай внимания."
    d "Она всегда такая."
    c "Да, я заметил."
    show velda angry with dissolve
    v "Я прямо здесь..."
    c "Я вижу."
    show velda frown with dissolve
    v "Так что не говори обо мне так."
    c "У тебя нет проблем, когда ты говоришь обо мне плохо прямо мне в лицо."
    show velda nervous with dissolve
    v "Это потому что ты... это ты."
    c "Не понимаю."
    show velda frown with dissolve
    v "А я не понимаю, как я это выношу..."
    c "Выносишь что?"
    show velda angry with dissolve
    v "Не твоё дело."
    c "Ладно..."
    c "Итак, полагаю, сегодня моя помощь тебе тоже не нужна..."
    show velda frown with dissolve
    v "Кому нужна ТВОЯ помощь?"
    d "Она права."
    d "Почему бы тебе не выйти на улицу или куда-нибудь ещё?"
    c "Ты всё ещё думаешь, что я заблужусь?"
    d "Кто знает...?"
    d "Почему бы тебе не пойти?"

menu:

    "Но я хочу остаться":
        jump iwanttostaywithuncle

    "Ладно, я пойду":
        jump iwillleaveuncle

label iwanttostaywithuncle:

    c "Но я хочу остаться..."
    show velda nervous with dissolve
    v "А я не хочу, чтобы ты был здесь."
    d "Тебе придётся мириться с... ЭТИМ, если останешься."
    d "И я бы предпочёл, чтобы ты этого не делал."
    c "Ладно..."
    c "Думаю, я пойду."
    show velda smile with dissolve
    v "Хорошо."
    c "..."
    hide velda smile with dissolve
    jump outsideonlifeday3

label iwillleaveuncle:
    c "Думаю, я пойду."
    c "Придётся выслушивать нытьё Вельды, если останусь."
    show velda nervous with dissolve
    v "Просто иди уже."
    d "Будь осторожен там."
    c "Я уже не маленький ребёнок."
    d "Знаю..."
    show velda angry with dissolve
    v "Выметайся уже отсюда!"
    c "Иду, иду!"
    hide velda angry with dissolve
    jump outsideonlifeday3

##################################################################
    label outsideonlifeday3:

    stop music fadeout 1.0
    play music happydays
    scene bg street 2 day snow with fade

    x "Меня выгнали из дома."
    x "Не то, что я ожидал."
    x "Это довольно странно."
    x "Я должен наслаждаться каникулами, но... честно говоря, это не так уж весело."
    x "Дядя ведёт себя странно, как и девушки, которых я только что встретил."
    x "Что, чёрт возьми, здесь происходит?"
    show gwen normal with dissolve
    g "Д-Доброе утро..."
    c "А, утро, Гвен."
    show gwen nervous with dissolve
    g "..."
    c "Что?"
    show gwen frown with dissolve
    g "Прости, мне нужно куда-то идти."
    play sound running
    hide gwen frown with dissolve
    x "Затем она убегает в направлении ресторана."
    c "Кажется, я никогда не пойму ни одну из этих девушек."
    stop sound fadeout 1.0
##################################################################
    scene bg park crossing snow with fade
    show rose nervous with dissolve
    r "Что ты тут делаешь один?"
    c "Меня вроде как выгнали из дома."
    show rose shock with dissolve
    r "Ты разозлил дядю?"
    c "...Не знаю."
    c "Не припоминаю, чтобы делал что-то, что могло бы его расстроить."
    c "Несмотря на это, мне сказали просто выйти на улицу."
    show rose nervous with dissolve
    r "Понятно."
    c "..."
    show rose normal with dissolve
    r "Что не так?"
    c "Мне кажется, что все здесь странно себя ведут."
    show rose nervous with dissolve
    r "Т-Ты, наверное, просто это выдумываешь."
    c "Почему ты звучишь так, будто что-то скрываешь?"
    show rose angry with dissolve
    r "Я-Я вообще ничего не скрываю!"
    show rose normal with dissolve
    r "О, точно!"
    show rose nervous with dissolve
    r "Мне нужно кое-куда успеть."
    show rose smile with dissolve
    r "Поговорим позже, Карон!"
    play sound running
    hide rose smile with dissolve
    x "Роуз убегает из парка."
    x "Я вздыхаю."
    x "Что со всеми в этом городе?!"
    stop sound fadeout 1.0
##################################################################

    stop music fadeout 1.0
    play music dontwanttokeepdoingthis
    scene bg restaurant with fade

    x "После того как я провёл на улице около часа, я вернулся в ресторан."
    show velda nervous with dissolve
    v "Итак, что нам делать?"
    hide velda nervous with dissolve
    show rose frown with dissolve
    r "Не знаю."
    hide rose frown with dissolve
    show gwen nervous with dissolve
    g "Я устала это делать..."
    d "Чудо, что это вообще произошло."
    d "Но бесконечное чудо — это, вроде как, кошмар."
    x "О чём они?"
    hide gwen nervous with dissolve
    show rose normal with dissolve
    r "Я была счастлива снова увидеть его после того, что случилось..."
    show rose frown with dissolve
    r "Но видеть его снова и снова только напоминает мне, насколько это ненормально..."
    hide rose frown with dissolve
    show gwen nervous with dissolve
    g "Нам не стоило этого начинать."
    show gwen frown with dissolve
    g "Это было неправильно."
    hide gwen frown with dissolve
    show velda nervous with dissolve
    v "Все те разы я лгала, но теперь, когда я говорю, что мне это надоело, я серьёзна."
    d "Да..."
    c "Эм... о чём вы все?"
    d "Карон!?"
    d "Когда ты вернулся?!"
    c "Эм, только что..."
    show velda angry with dissolve
    v "Кто дал тебе разрешение возвращаться?"
    c "О ком вы говорили?"
    hide velda angry with dissolve
    show rose nervous with dissolve
    r "Э... тебя это не касается."
    hide rose nervous with dissolve
    show gwen angry with dissolve
    g "Разве ты не знаешь, что вмешиваться в чужие разговоры невежливо?"
    c "Допустим..."
    d "Это не то, в чём тебе нужно участвовать."
    c "Прости, но вы все меня беспокоите."
    c "С тех пор, как я сюда приехал, все ведут себя странно."
    c "Разве я не имею права знать, что всё это значит?"
    hide gwen angry with dissolve
    show velda angry with dissolve
    v "Тебе не нужно быть таким любопытным."
    show velda nervous with dissolve
    v "Прямо как каждый раз..."
    c "Каждый... раз?"
    show velda angry with dissolve
    v "Я ничего не сказала!"
    hide velda angry with dissolve
    d "..."
    c "Дэниел...?"
    d "Прости, Карон."
    d "Это не то, о чём мы можем с тобой поговорить."
    c "Ладно."
    c "Пойду к себе в комнату."
    d "Давай..."

##################################################################

    stop music fadeout 1.0
    play music heisgone
    scene bg bedroom with fade

    x "Вот я сижу неподвижно в своей комнате."
    x "Зачем родители отправили меня сюда?"
    x "Была ли поездка сюда ошибкой всё это время?"
    x "Может, мне стоило просто остаться с ними?"
    x "Потому что в итоге кажется, что здесь никто не хочет моего присутствия."
    x "Я думал, что это будет мой шанс начать всё заново в новой обстановке."
    x "Может, я бы завёл новых друзей...?"
    x "Но... здесь, похоже, никто не заинтересован в этом."
    x "Мой дядя даже не хочет, чтобы я был в ресторане."
    x "Все, кого я здесь встретил, тоже, кажется, пытаются меня избегать."
    x "В то же время, мне кажется, что все от меня что-то скрывают."
    x "Что... это?"
    x "Я не думал, что меня что-то так сильно побеспокоит..."
    x "Я тяжело вздыхаю, падая на кровать."
    x "Если я останусь здесь дольше, это чего-нибудь даст?"
    x "Что я вообще могу сделать?"
    x "Может, мне стоит собрать вещи и вернуться домой?"
    x "Не знаю..."
    x "Не думаю, что родители обрадуются, если я вернусь так внезапно."
    x "Мои родители..."
    x "Прошло всего несколько дней с тех пор, как я их покинул, но у меня чувство, что я не видел их целую вечность."
    x "Это действительно странно."
    x "Может, просто потому, что эти несколько дней ощущаются так долго."

##################################################################

    stop music fadeout 1.0
    scene bg diningroom with fade
    x "За ужином дядя не проронил ни слова."
    x "По какой-то причине Вельда тоже с нами."
    x "Она тоже не хочет говорить."
    x "Так что... может, мне стоит что-то сделать с этой тишиной...?"
    c "Так, эм... сегодня что-нибудь интересное случилось?"
    show velda nervous with dissolve
    v "Заткнись, Карон."
    c "Ладно."
    hide velda nervous with dissolve
    x "Все снова замолчали."
    x "Я вздыхаю."
    d "Не переживай об этом."
    c "Не переживать о чём?"
    d "Ничего странного не происходит..."
    show velda angry with dissolve
    v "Почему бы тебе не помолчать?"
    d "Д-Да."
    d "Я помолчу..."
    c "...?"
    hide velda angry with dissolve
    x "Ужин был очень запутанным."
    x "Однако мне не хотелось ничего выяснять, и я просто пошёл спать после этого."

##################################################################

    # День 4 #
    scene bg bedroom with fade
    play music worryaboutyou
    x "Я так устал..."
    x "О, точно."
    x "Утро."
    x "Мне нужно встать."
    play sound choke
    x "Я кашляю."
    stop sound fadeout 1.0
    x "Я... чувствую себя паршиво."
    x "Я заболел?"
    x "Похоже, я не так хорошо о себе забочусь, как думал."
    x "Что ж, что мне делать сегодня?"

menu:

    "Отдохнуть":
        jump getsomerestlife

    "Пойти спать":
        jump gotosleeplife

    "Попробовать встать":
        jump trytogetuplife

    "Просто умереть":
        jump justdielife

label getsomerestlife:
    x "Раз я болен, мне стоит просто отдохнуть."
    x "Если я прикован к кровати, я не буду никому мешать."
    x "Думаю, они и не хотят со мной возиться."
    x "Так что, может, моя болезнь — это благословение."
    x "Самое классное — меня не выгонят."
    x "Всё ещё паршиво, что я себя так чувствую."
    x "Ну и ладно."
    x "Не то чтобы я умер..."
    jump lifeday4continues

label gotosleeplife:
    x "Я болен, так что стоит попробовать снова уснуть?"
    x "Лежу неподвижно в кровати и закрываю глаза."
    x "Если я не встану, я не буду им мешать."
    x "Так что, может, болеть — это даже хорошо."
    x "В таком состоянии они не смогут меня выгнать."
    x "Мне не нравится так себя чувствовать."
    x "Эх."
    x "Уверен, выживу..."
    jump lifeday4continues

label trytogetuplife:
    x "Мне стоит попробовать встать."
    x "Не хочу весь день валяться в кровати."
    x "Но... я слишком паршиво себя чувствую, чтобы встать."
    x "Похоже, я и правда буду лежать тут..."
    x "Ну и ладно."
    x "..."
    x "Боже, это отстой!"
    x "Зачем я должен был заболеть?!"
    jump lifeday4continues

label justdielife:
    x "Что ж, тут мало что можно сделать."
    x "Зачем я вообще продолжаю...?"
    x "Все меня игнорируют."
    x "Они не хотят иметь со мной ничего общего."
    x "Может, мне лучше умереть."
    x "Думаю, мне стоит просто умереть."
    x "Так будет лучше."
    stop music fadeout 1.0
    $ achievement.grant("Life_GiveUp")
    x "ПЛОХАЯ КОНЦОВКА — КАРОН ПРОСТО УМИРАЕТ"
    $ renpy.movie_cutscene("video/BadCredits.webm", delay=95, loops=0, stop_music=True)
    x "О чём я вообще думаю?"
    x "Я не могу умереть!"
    jump lifeday4continues

##################################################################
    label lifeday4continues:
    play music friendship
    scene bg bedroom with fade
    show velda nervous with dissolve
    v "Карон?"
    x "Я открываю глаза."
    c "Вельда...?"
    show velda normal with dissolve
    v "Как ты себя чувствуешь?"
    c "Странно, что тебе не всё равно."
    show velda nervous with dissolve
    v "..."
    show velda normal with dissolve
    v "Ну?"
    x "Она что, заставляет себя не оскорблять меня?"
    c "Эм... я правда чувствую себя паршиво."
    show velda nervous with dissolve
    v "Понятно..."
    show velda frown with dissolve
    v "Интересно, сколько времени осталось...?"
    c "О чём ты?"
    show velda shock with dissolve
    v "О!"
    show velda normal with dissolve
    v "Эм, твой дядя попросил меня поставить что-то в духовку..."
    c "..."
    show velda smile with dissolve
    v "В общем, лежи в кровати."
    c "Я и так собирался."
    show velda normal with dissolve
    v "Я принесу тебе лекарства, ладно?"
    c "Ладно..."
    hide velda normal with dissolve
##################################################################

    show gwen shock with dissolve
    g "О Боже!"
    show gwen smile with dissolve
    g "Ты ещё жив?"
    c "С чего ты взяла, что я мёртв?"
    hide gwen smile with dissolve
    show velda nervous with dissolve
    v "Я же тебе говорила, что он просто болен, нет?"
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Да..."
    show gwen normal with dissolve
    g "Я просто так волновалась..."
    c "Мы же познакомились всего несколько дней назад."
    c "У тебя нет причин обо мне беспокоиться."
    hide gwen normal with dissolve
    show rose smile with dissolve
    r "Что ж, все знают твоего дядю."
    show rose normal with dissolve
    r "Мы все знаем, что он расстроится, если с тобой что-то случится."
    c "Так вы здесь ради меня или ради моего дяди?"
    show rose smile with dissolve
    r "И то, и другое."
    c "Это не совсем..."
    hide rose smile with dissolve
    show velda nervous with dissolve
    v "Тихо."
    c "Х-Хорошо..."
    d "Как он?"
    show velda frown with dissolve
    v "Он всё ещё раздражает."
    d "Правда?"
    x "Мой дядя слабо смеётся."
    hide velda frown with dissolve
    c "Я вас вообще не понимаю."
    d "Что ты имеешь в виду?"
    c "Последние несколько дней вы все пытались меня избегать."
    c "Теперь вы все обращаете на меня внимание."
    c "В чём дело?"
    d "Мы просто немного были заняты и хотели, чтобы ты насладился отдыхом."
    c "Я в это не верю..."
    d "Эм... ну, я правда хотел, чтобы ты насладился отпуском."
    c "Но почему вы все здесь сейчас?"
    show velda normal with dissolve
    v "Потому что меня уволят, если я не помогу."
    hide velda normal with dissolve
    show gwen smile with dissolve
    g "Я пойду куда угодно, куда пойдёт Вельда."
    hide gwen smile with dissolve
    show rose normal with dissolve
    r "Я здесь, потому что это правильно."
    c "Угу..."
    show rose nervous with dissolve
    r "Ты нам не веришь?"
    c "Не скажу."
    hide rose nervous with dissolve
    show velda nervous with dissolve
    v "Ты мелкая стерва."
    c "А ТЫ большая стерва."
    show velda angry with dissolve
    v "Я бы тебя ударила, если бы ты не болел."
    c "Хех."
    hide velda angry with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg bedroom with fade
    x "Я провёл весь день в кровати."
    x "Чувствую себя лишь немного лучше."

    play music mysterious

    x "Мои руки выглядят странно."
    x "Это... как будто я могу сквозь них видеть."
    x "Что за чёрт?"
    x "Я... наверное, очень устал."
    x "Я, должно быть, просто вижу глюки."
    x "Чёрт, какие странные каникулы."
    x "И я ещё умудрился заболеть."
    x "В итоге мне грустно, что я мало чего достиг."
    x "Подожди..."
    x "Не может быть..."
    x "Я качаю головой."
    x "Эти мысли..."
    x "О чём я, чёрт возьми, думаю?"
    x "Но... я не думаю, что могу это отрицать."
    x "Я... кажется, понимаю."
    x "Это многое объясняет."
    x "Но в это довольно трудно поверить."
    x "Я не хочу в это верить, но это должна быть правда."
    x "Собирая всё воедино, я наконец пришёл к ответу."
    x "Я знаю правду."
    x "Я знаю... что что-то было не так всё это время."
    x "Но... нет причин слишком переживать об этом прямо сейчас."
    x "Так что пока я пойду спать."
    x "Я могу поволноваться об этом завтра."
    x "Хотя я не особо этого жду."
    stop music fadeout 1.0
##################################################################

    # День 5 #

    play music calm

    show velda normal with dissolve
    v "Итак, как ты сегодня?"
    c "Всё ещё паршиво."
    show velda nervous with dissolve
    v "Понятно."
    show velda normal with dissolve
    v "Тебе что-нибудь нужно?"
    c "Нет, я в порядке."
    show velda nervous with dissolve
    v "Ладно."
    show velda normal with dissolve
    v "Что ж, я пойду обратно работать."
    c "О, эм..."
    c "Спасибо... за всё."
    show velda smile with dissolve
    v "Понятия не имею, о чём ты."
    c "Ага..."
    show velda nervous with dissolve
    v "Что ж, мне лучше идти."
    c "Да..."
    hide velda nervous with dissolve
    x "Странно, что она вдруг обо мне заботится."
    x "Когда я только приехал, у меня было впечатление, что она не хотела иметь со мной ничего общего."
    x "Но с тех пор, как она поняла, что я болен, она обо мне заботится."
    x "Остальные девушки тоже."
    x "Все беспокоились обо мне."
    x "Ни разу не было ощущения, что я окружён незнакомцами."
    x "Я чувствовал, что знаю этих девушек давно."
    x "А теперь..."
    x "Боже, я сонный."
    x "А теперь мне стоит..."

menu:

    "Пойти спать":
        jump gosleepday5life

    "Закрыть глаза":
        jump gosleepday5life

    "Отдыхать в кровати":
        jump gosleepday5life

    "...":
        jump gosleepday5life

label gosleepday5life:
    stop music fadeout 1.0
    x "..."
    x "С трудом держу глаза открытыми."
    x "Думаю, я пойду спать."
    x "Это, наверное, единственное, что я сейчас могу сделать."

##################################################################
##################################################################
    # День неизвестен

    play music snowydays
    scene bg danielroom with fade
    x "Я просыпаюсь очередным утром."
    x "Каждое утро мне приходится всё настраивать."
    x "Это потому что... я владею рестораном."
    d "Боже, у меня опять был странный сон прошлой ночью."
    d "Я пытаюсь забыть о... том."
    d "Но я продолжаю думать о том, что случилось."
    d "Почему я разговариваю сам с собой?"
    x "В любом случае, мне лучше всё приготовить."
##################################################################
    scene bg restaurant with fade
    d "Ты сегодня рано."
    show velda normal with dissolve
    v "О, правда?"
    show velda smile with dissolve
    v "Я пришла рано или ты просто опоздал?"
    d "Кто уже знает?"
    hide velda smile with dissolve
    show gwen nervous with dissolve
    g "Хватит донимать его."
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Тьфу."
    show velda frown with dissolve
    v "Тяжело не донимать, когда он так напоминает мне о..."
    hide velda frown with dissolve
    show gwen angry with dissolve
    g "Это не его вина!"
    hide gwen angry with dissolve
    show velda nervous with dissolve
    v "Не надо мне это говорить..."
    hide velda nervous with dissolve
    show rose nervous with dissolve
    r "Вы правда собираетесь ссориться так рано утром?"
    d "Это не входило в мои планы, но похоже, что Вельда именно этого и хочет."
    hide rose nervous with dissolve
    show velda angry with dissolve
    v "Просто заткнись."
    hide velda angry with dissolve
    show gwen angry with dissolve
    g "Не смей говорить боссу заткнуться!"
    hide gwen angry with dissolve
    show velda nervous with dissolve
    v "Что?"
    show velda normal with dissolve
    v "Ты думаешь, он будет на твоей стороне, потому что ты «хорошая девочка»?"
    hide velda normal with dissolve
    show gwen nervous with dissolve
    g "Я..."
    hide gwen nervous with dissolve
    show rose normal with dissolve
    r "Пожалуйста, хватит ссориться..."
    hide rose normal with dissolve
    show velda nervous with dissolve
    v "Кто тебя спрашивал?"
    d "Мне правда нужно, чтобы ты перестала так разговаривать."
    d "Клиенты не останутся, если ты будешь продолжать."
    d "И... мне придётся урезать тебе зарплату."
    show velda frown with dissolve
    v "Ладно..."
    hide velda frown with dissolve
    stop music fadeout 1.0
##################################################################

    play music happydays
    scene bg restaurant with fade

    x "Прошёл ещё один обычный день в ресторане."
    x "Вельда так и не избавилась от своей привычки."
    x "Она всё ещё довольно груба с людьми."
    x "Я также слышал, что она курила, но сейчас пытается бросить."
    x "По крайней мере, у меня есть её кузина, которая может за неё заступиться."
    x "Честно говоря, не знаю, что бы я делал без них."
    x "Я бы, наверное, сошёл с ума."
    x "Я очень благодарен, что Гвен и Роуз тоже начали здесь работать."
    show rose nervous with dissolve
    r "О чём ты думаешь?"
    d "А, ни о чём."
    hide rose nervous with dissolve
    show velda smile with dissolve
    v "Он думает о том, что никогда не женится."
    d "Я вообще не об этом думал..."
    d "Но спасибо, что напомнила, что мне не везёт..."
    hide velda smile with dissolve
    show gwen smile with dissolve
    g "Сегодня здесь намного чище."
    hide gwen smile with dissolve
    show velda frown with dissolve
    v "Слишком чисто, если хочешь моё мнение."
    d "Что не так с чистотой?"
    hide velda frown with dissolve
    show gwen normal with dissolve
    g "Несколько лет назад здесь никогда не было так чисто."
    d "Допустим."
    d "Но сейчас у нас работает больше людей."
    d "Так что это логично, нет?"
    show gwen smile with dissolve
    g "Да..."
    hide gwen smile with dissolve
    show rose normal with dissolve
    r "Хватит об этом месте."
    show rose smile with dissolve
    r "Ты ведь придёшь на фейерверки сегодня вечером?"
    d "А, да."
    d "Всё равно делать нечего."
    show rose normal with dissolve
    r "Хорошо."
    hide rose normal with dissolve
    show velda smile with dissolve
    v "Если опоздаешь, я тебя убью."
    d "Эм, понял."
    hide velda smile with dissolve
    stop music fadeout 1.0
##################################################################

    scene bg street 2 day with fade
    x "Я оказываюсь на улице с моими тремя сотрудницами."
    d "..."
    play music struggletomoveon
    show rose frown with dissolve
    r "Ты всё ещё не можешь с этим смириться, да?"
    d "..."
    d "Наверное, нет."
    show rose nervous with dissolve
    r "Прошло уже несколько лет."
    hide rose nervous with dissolve
    show velda nervous with dissolve
    v "Нельзя же вечно переживать о том, что случилось так давно, правда?"
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Нас это тоже беспокоит, но..."
    show gwen normal with dissolve
    g "Мы пытаемся двигаться дальше."
    d "Да..."
    d "Было тяжело."
    d "Его больше нет."
    hide gwen normal with dissolve
    x "Мой племянник, Карон, умер несколько лет назад."
    x "Он приехал на зимние каникулы, а затем познакомился с Вельдой, Гвен и Роуз."
    x "Они все очень хорошо поладили с ним."
    x "Так что... они были убиты горем, когда он умер."
    x "Однажды его сбила машина."
    x "Что ещё хуже, за рулём был пьяный водитель."
    x "Вельда поклялась, что убьёт того водителя."
    x "Однако этого водителя в итоге самого госпитализировали."
    x "А потом он сам умер."
    x "После смерти Карона Роуз и Гвен начали работать на меня."
    x "Благодаря им я не сошёл с ума полностью."
    x "Но вполне очевидно, что смерть Карона беспокоила всех нас."
    show velda angry with dissolve
    v "Ты собираешься проснуться?!"
    d "О, точно."
    d "Эм... прости."
    show velda nervous with dissolve
    v "Смотри, куда идёшь."
    show velda frown with dissolve
    v "Ты чуть не врезался в столб."
    show velda angry with dissolve
    v "Ты тупой или что?"
    d "Может, я и тупой..."
    hide velda angry with dissolve
    show rose nervous with dissolve
    r "Можем не ссориться?"
    hide rose nervous with dissolve
    show velda nervous with dissolve
    v "..."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Нам не стоит ссориться."
    d "Верно."
    d "Пойдём."
    hide gwen normal with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg fireworks with fade

    x "Мы пошли смотреть фейерверки."
    x "Кажется, все хорошо провели время."
    x "Но... все думали об одном и том же."
    x "Было бы лучше, если бы Карон тоже был здесь."
    d "Нам пора идти."
    d "Не хочу, чтобы вы трое поздно возвращались."
    show velda normal with dissolve
    v "Мы сами о себе позаботимся."
    show velda smile with dissolve
    v "Мы уже все взрослые."
    d "Верно..."
    hide velda smile with dissolve
    play music prayer
    show gwen normal with dissolve
    g "Хотелось бы, чтобы Карон мог быть здесь."
    hide gwen normal with dissolve
    show velda frown with dissolve
    v "О, зачем ты это сказала?"
    hide velda frown with dissolve
    show rose nervous with dissolve
    r "...Я чувствую то же самое."
    d "..."
    hide rose nervous with dissolve
    show velda nervous with dissolve
    v "Да..."
    x "Мы все посмотрели вверх, чувствуя грусть, что Карона нет с нами."
    x "Глядя вверх, мы увидели, как пролетает падающая звезда."
    hide velda nervous with dissolve
    show gwen smile with dissolve
    g "Хочу снова увидеть Карона."
    hide gwen smile with dissolve
    show velda normal with dissolve
    v "Я тоже."
    hide velda normal with dissolve
    show rose smile with dissolve
    r "И я."
    d "..."
    d "Это было бы здорово, правда?"
    x "Я держу голову поднятой, пытаясь не заплакать."
    x "Вельда качает головой."
    hide rose smile with dissolve
    show velda normal with dissolve
    v "Просто желать — не значит получить."
    d "Верно."
    d "Подобное случается только в вымысле."
    hide velda normal with dissolve
    show gwen normal with dissolve
    g "..."
    hide gwen normal with dissolve
    show rose normal with dissolve
    r "..."
    $ flash = Fade(.25, 0, .75, color="#fff")
    scene bg fireworks with flash
    x "Внезапно вспыхнул яркий свет."
    d "Что это было?!"
    hide rose normal with dissolve
    show velda nervous with dissolve
    v "Лучше пойти домой..."
    hide velda nervous with dissolve
    show rose normal with dissolve
    r "Хорошая идея..."
    play sound running
    x "Мы вчетвером убегаем в направлении наших домов."
    stop sound fadeout 1.0
    scene bg fireworks with flash
    scene bg white with fade
    stop music fadeout 1.0
    x "Была ещё одна вспышка, а затем все мы увидели только белое."
    d "Что, чёрт возьми, происходит?!"
    show rose nervous with dissolve
    r "С вами всё в порядке?"
    hide rose nervous with dissolve
    show velda normal with dissolve
    v "Не думаю, что кто-то умер."
    hide velda normal with dissolve
    show gwen nervous with dissolve
    g "Где мы?"
    hide gwen nervous with dissolve
    show rose nervous with dissolve
    r "Хороший вопрос..."
    d "Хммм..."
    play music magic
    hide rose nervous with dissolve
    show rin normal with dissolve
    ug "Я здесь, чтобы помочь вам."
    hide rin normal with dissolve
    show velda angry with dissolve
    v "Похитив нас?!"
    hide velda angry with dissolve
    show rin frown with dissolve
    ug "Вас не похищали."
    hide rin frown with dissolve
    show rose normal with dissolve
    r "Кто ты?"
    hide rose normal with dissolve
    show rin normal with dissolve
    ri "Меня зовут Рин."
    show rin smile with dissolve
    ri "Я здесь, чтобы исполнить ваше желание."
    d "О чём ты?"
    show rin frown with dissolve
    ri "Вы же хотели снова увидеть того парня, нет?"
    ev "...!"
    d "Ну, да..."
    hide rin frown with dissolve
    show gwen nervous with dissolve
    g "Ты ведь не лжёшь?"
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Зачем бы ты нам помогала?"
    hide velda nervous with dissolve
    show rin normal with dissolve
    ri "Я говорю правду."
    show rin smile with dissolve
    ri "И моя цель — отвечать на желания людей."
    hide rin smile with dissolve
    show velda nervous with dissolve
    v "Правда?"
    hide velda nervous with dissolve
    show rin normal with dissolve
    ri "Я могу отправить вас в мир, где ваш друг всё ещё жив."
    show rin smile with dissolve
    ri "Что думаете?"
    d "..."
    hide rin smile with dissolve
    show gwen nervous with dissolve
    g "Дэниел?"
    d "Д-Да..."
    show gwen normal with dissolve
    g "Что нам делать?"

menu:

    "Принять её предложение":
        jump acceptrinoffer

    "Отказаться":
        jump denyheroffer

    "Не знаю":
        jump idkrinoffer

label acceptrinoffer:
    d "..."
    x "Может, мне стоит принять?"
    x "Возможно, мне больше не представится такой шанс."
    hide gwen normal with dissolve
    show rin normal with dissolve
    ri "Ну?"
    hide rin normal with dissolve
    jump rinoffer

label denyheroffer:
    d "Нет."
    d "Не знаю, стоит ли нам..."
    show gwen nervous with dissolve
    g "Но это может быть наш единственный шанс..."
    d "Хммм..."
    hide gwen nervous with dissolve
    jump rinoffer

label idkrinoffer:
    d "Я... не знаю."
    hide gwen normal with dissolve
    show rose normal with dissolve
    r "У нас может больше не быть такого шанса..."
    hide rose normal with dissolve
    show velda frown with dissolve
    v "Вы правда верите в эту чушь?"
    d "Хммм..."
    hide velda frown with dissolve
    jump rinoffer

label rinoffer:
    d "Я... мы... принимаем."
    show velda nervous with dissolve
    v "Серьёзно?"
    d "Да."
    d "Мы хотели бы увидеть его снова."
    hide velda nervous with dissolve
    show rin smile with dissolve
    ri "Тогда я исполню ваше желание."
    show rin normal with dissolve
    ri "Вы будете жить в мире, где он был ещё жив."
    show rin smile with dissolve
    ri "И вы можете повторять этот мир столько, сколько захотите."
    show rin frown with dissolve
    ri "Ну, по крайней мере, пока моя магия может это поддерживать."
    d "Понятно."
    d "Спасибо."
    show rin normal with dissolve
    ri "Не благодари."
    show rin smile with dissolve
    ri "Я просто делаю свою работу..."
    d "Если подумать, ты выглядишь знакомо..."
    show rin frown with dissolve
    ri "Ты, наверное, просто это выдумываешь."
    d "Может быть..."
    show rin normal with dissolve
    ri "Что ж, наслаждайтесь новым миром."
    d "Да..."
    hide rin normal with dissolve
##################################################################

    stop music fadeout 1.0
    play music paineverydirection
    scene bg mystery sky with fade
    x "Вот так мы вернулись в те зимние каникулы."
    x "Мы смогли жить нашей жизнью с Кароном снова, как будто он всегда был рядом."
    x "Это была мечта."
    x "Сначала все были счастливы."
    x "Мы повторяли те каникулы снова и снова."
    x "Каждый раз получая разный исход."
    x "Но что бы мы ни делали иначе, Карона всё равно сбивала машина."
    x "Мы могли связаться с Рин, чтобы попросить её перезагрузить мир."
    x "В конце концов, мы устали всё повторять."
    x "И теперь... похоже, наш общий сон подходит к концу."
    x "Похоже, силы Рин больше не смогут поддерживать этот мир."
##################################################################
##################################################################

    # Финальный день

    play music miracle
    scene bg bedroom with fade
    x "Теперь я понимаю."
    x "Меня здесь быть не должно."
    x "Всё это время я просто застрял в сне."
    x "Верно."
    x "Я... умер давно."
    x "После моих каникул меня сбила машина."
    x "К сожалению, я не выжил."
    x "Это действительно отстой."
    x "У меня были одни из лучших каникул в жизни, и я завел по-настоящему хороших друзей."
    x "Я был счастливее, чем когда-либо."
    x "Но судьба решила забрать всё это у меня."
    x "Чудо, что я смог увидеть их снова."
    x "В конце концов, я счастлив, что у нас было больше времени вместе."
    x "Но всё хорошее должно когда-нибудь закончиться."
    x "Я... не протяну долго."
    x "Как и мир, в котором я нахожусь."
##################################################################

    stop music fadeout 1.0
    scene bg bedroom with fade
    x "Кажется, силы вернулись ко мне."
    x "Что ж, думаю, пора всё закончить."
##################################################################

    scene bg restaurant with fade
    x "Я быстро выхожу из комнаты и направляюсь в обеденный зал."
    x "Как я и ожидал, все там."
    d "Д-Доброе утро."
    c "А, утро."
    c "Эм... вам не обязательно продолжать."
    show gwen nervous with dissolve
    g "Что ты имеешь в виду?"

    play music caronend

    c "Я всё помню."
    hide gwen nervous with dissolve
    show rose shock with dissolve
    r "Т-Ты помнишь?"
    c "Да, я помню."
    d "Понятно."
    c "Так что..."
    c "Думаю, это конец."
    hide rose shock with dissolve
    show velda frown with dissolve
    v "Подожди."
    show velda nervous with dissolve
    v "Ты правда счастлив с этим?"
    c "Что ж, я не могу остаться."
    c "Этот мир ненастоящий."
    c "И меня... больше не должно существовать."
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Но..."
    show gwen frown with dissolve
    g "Я не готова."
    show gwen nervous with dissolve
    g "Пожалуйста... побудь ещё немного."
    c "Я правда благодарен, что встретил всех вас."
    c "Спасибо за всё."
    hide gwen nervous with dissolve
    show rose nervous with dissolve
    r "Ну же..."
    show rose frown with dissolve
    r "Пожалуйста, не делай этого с нами..."
    c "Прости."
    hide rose frown with dissolve
    d "Карон..."
    c "Спасибо, что заботился обо мне."
    x "Моё тело начинает медленно исчезать."
    x "Странное ощущение — иметь прозрачное тело."
    c "Я... никогда не забуду время, которое мы провели вместе."
    show gwen normal with dissolve
    g "Ну же..."
    show gwen angry with dissolve
    g "Не может быть, что всё уже кончено!"
    hide gwen angry with dissolve
    show velda angry with dissolve
    v "Пожалуйста... побудь ещё немного!"
    hide velda angry with dissolve
    show rose angry with dissolve
    r "Не уходи ещё!"
    d "..."
    hide rose angry with dissolve
    show gwen normal with dissolve
    g "Ты был рядом, когда я потеряла брата."
    show gwen angry with dissolve
    g "Я не хочу потерять и тебя!"
    hide gwen angry with dissolve
    show velda normal with dissolve
    v "Никто так не заботился обо мне, пока я не встретила тебя."
    show velda angry with dissolve
    v "Так почему я должна быть в порядке с тем, что ты медленно исчезаешь у нас на глазах?!"
    hide velda angry with dissolve
    show rose smile with dissolve
    r "И ты был так мне полезен."
    show rose nervous with dissolve
    r "Ты мирился с тем, что я делала, и даже отчитывал меня за то, что я слишком много работаю..."
    hide rose nervous with dissolve
    d "Это место не было бы тем же без тебя."
    c "Вы все подарили мне лучшие зимние каникулы, что у меня когда-либо были."
    x "Моё тело всё ещё исчезает."
    x "Сквозь меня теперь стало гораздо легче видеть."
    c "Что ж..."
    c "Надеюсь, мы снова встретимся на небесах..."
    d "Тьфу."
    ev "Карон...!"
    show gwen frown with dissolve
    g "Пожалуйста... не уходи ещё."
    hide gwen frown with dissolve
    show rose frown with dissolve
    r "Почему сейчас...?"
    hide rose frown with dissolve
    show velda frown with dissolve
    v "Чёрт."
    hide velda frown with dissolve
    c "Вы..."
    c "Чёрт..."
    play sound mancry
    c "Конечно, я хочу остаться!"
    c "Я..."
    c "Я хочу быть с вами вечно!"
    c "Вы все мои лучшие друзья..."
    c "Как я мог хотеть просто оставить вас так?!"
    play sound womancry
    x "Все плачут, пока я продолжаю исчезать."
    c "Простите..."
    ev "Карон!"
    stop sound fadeout 1.0
    x "Моё тело почти невидимо."
    x "Слёзы катятся из глаз всех, пока я приближаюсь к небытию."
    c "Я... надеюсь, вы будете жить дальше."
    c "Вы можете сделать это для меня?"
    show gwen frown with dissolve
    g "Да."
    x "Гвен вытирает лицо рукавом."
    c "Спасибо всем за всё."
    x "А затем я теряю способность говорить."
    x "Я полностью исчез из существования."
    x "Мои друзья и мой дядя всё ещё там, плачут."
    hide gwen smile with dissolve
    show velda angry with dissolve
    v "Чёрт!"
    hide velda angry with dissolve
    show gwen normal with dissolve
    g "Карон..."
    hide gwen normal with dissolve
    show rose nervous with dissolve
    r "Не могу поверить, что его больше нет..."
    d "Не думаю, что кто-то из нас был к этому готов."
    d "Но... полагаю, это значит, что этот мир... скоро исчезнет."
    show rose normal with dissolve
    r "Да."
    hide rose normal with dissolve
    show velda nervous with dissolve
    v "Мы вернёмся в наш старый мир..."
    hide velda nervous with dissolve
    show gwen normal with dissolve
    g "Даже если этот мир был ненастоящим, я буду скучать по нему."
    d "Я тоже."
    hide gwen normal with dissolve
    stop music fadeout 1.0
##################################################################
    play music memories
    scene bg mystery sky with fade
    x "У всего есть начало и конец."
    x "На каждые несколько родившихся приходится несколько умерших."
    x "И каждая жизнь, которая родилась, однажды должна закончиться."
    x "Но каждая жизнь идёт по своему собственному пути от начала до конца."
    x "Длина этого пути различается."
    x "Для кого-то он короток."
    x "А для кого-то длинен."
    x "Единственное, что точно — все они заканчиваются."
    x "На протяжении жизни мы все смеёмся, плачем и веселимся."
    x "Мы все встречаем людей и формируем с ними отношения."
    x "Хотя некоторые, конечно, сильнее других."
    x "Что делает расставание гораздо более болезненным."
    x "В конце концов, важно то, была ли наша жизнь хорошей."
    x "Даже если некоторые могут быть короткими, мы всё равно можем быть уверены, что наша жизнь была хорошей."
    x "Это не для всех так, но, по крайней мере, я могу сказать, что моя была хорошей."
    x "Спасибо вам всем."
    x "Это были поистине самые счастливые дни в моей жизни."
    $ achievement.grant("Painful_Truth")
    x "КОНЕЦ — МАРШРУТ ЖИЗНИ"
    $ persistent.liferouteclear = True
    stop music fadeout 1.0
    # Титры истинной концовки
    $ renpy.movie_cutscene("video/LifeCredits.webm", delay=259, loops=0, stop_music=True)
    return
