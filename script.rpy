#####

#image placeholder = "bgs/placeholder.png"
#$ achievement.grant("achievement_text")

image ctc_animation = Animation("ui/ctc1.png", 0.4, "ui/ctc2.png", 0.2, "ui/ctc3.png", 0.2, "ui/ctc4.png", 0.2, xpos=1.5, ypos=0.99, xanchor=1.0, yanchor=1.0)

############
# Персонажи
############

define n = Character('Намастаии',  color="#fff", ctc="ctc_animation")
define x = Character(' ', what_prefix="(",what_suffix=")",ctc="ctc_animation")
define me = Character('Я', color="#b7ccd8", ctc="ctc_animation")
define c = Character('Карон', color="#b7ccd8", ctc="ctc_animation")
define v = Character('Вельда', color="#b7ccd8", ctc="ctc_animation")
define r = Character('Роуз', color="#b7ccd8", ctc="ctc_animation")
define g = Character('Гвен', color="#b7ccd8", ctc="ctc_animation")
define d = Character('Дэниел', color="#b7ccd8", ctc="ctc_animation")
define k = Character('Кевин', color="#b7ccd8", ctc="ctc_animation")
define b = Character('Брат Гвен', color="#b7ccd8", ctc="ctc_animation")
define u = Character('???', color="#b7ccd8", ctc="ctc_animation")
define m = Character('Мужчина', color="#b7ccd8", ctc="ctc_animation")
define w = Character('Женщина', color="#b7ccd8", ctc="ctc_animation")
define do = Character('Доктор', color="#b7ccd8", ctc="ctc_animation")
define cv = Character('Карон и Вельда', color="#b7ccd8", ctc="ctc_animation")
define sg = Character('Подозрительный парень', color="#b7ccd8", ctc="ctc_animation")
define gm = Character('Член банды', color="#b7ccd8", ctc="ctc_animation")
define gl = Character('Лидер банды', color="#b7ccd8", ctc="ctc_animation")
define ug = Character('Девочка', color="#b7ccd8", ctc="ctc_animation")
define ub = Character('Мальчик', color="#b7ccd8", ctc="ctc_animation")
define ma = Character('Мари', color="#b7ccd8", ctc="ctc_animation")
define ri = Character('Рин', color="#b7ccd8", ctc="ctc_animation")
define ev = Character('Все', color="#b7ccd8", ctc="ctc_animation")
define eve = Character('Все остальные', color="#b7ccd8", ctc="ctc_animation")

##########
# Переменные
##########

default veldapoints = 0
default rosepoints = 0
default gwenpoints = 0
default veldabad = 0
default rosebad = 0
default gwenbad = 0

default veldahangout1 = False
default rosehangout1 = False
default gwenhangout1 = False
default confesstogwen = False
default confesstovelda = False
default friendswithvelda = False
default caronfaught = False
default admitlikerose = False
default rosebff = False
default confesstorose = False
default checkhospital = False
default checkorphanage = False
default hangoutalone = False
# default persistent.liferouteunlocked = False
# default persistent.futurerouteunlocked = False
# default persistent.futurerouteclear = False
# default veldaromanceclear = False
# default veldafriendshipclear = False
# default roseromanceclear = False
# default rosefriendshipclear = False
# default gwenromanceclear = False
# default gwenfriendshipclear = False

############
# Фоны
############

# Фоны остаются как есть (только пути к файлам, не переводятся)
#Ayaemo
image bg hospital hall = "img/bg/ayaemo/hospitalhall.jpg"
image bg hospital hall dark = "img/bg/ayaemo/hospitalhalldark.jpg"
image bg hospital room day = "img/bg/ayaemo/hospitalroomday.jpg"
image bg hospital room evening = "img/bg/ayaemo/hospitalroomevening.jpg"
image bg hospital room night = "img/bg/ayaemo/hospitalroomnight.jpg"
image bg hospital waiting = "img/bg/ayaemo/hospitalwaiting.jpg"
image bg hospital outside = "img/bg/ayaemo/outsidehospital.jpg"
image bg hospital outside evening = "img/bg/ayaemo/outsidehospitalevening.jpg"
image bg hospital outside dark = "img/bg/ayaemo/outsidehospitaldark.jpg"
image bg hospital outsidenight = "img/bg/ayaemo/outsidehospitalnight.jpg"
image bg store day = "img/bg/ayaemo/storeday.jpg"
image bg store dark = "img/bg/ayaemo/storedark.jpg"

#Kimagure After
image bg downtown day = "img/bg/kimagureafter/downtownday.jpg"
image bg downtown evening = "img/bg/kimagureafter/downtownevening.jpg"
image bg downtown night = "img/bg/kimagureafter/downtownnight.jpg"
image bg downtown night 2 = "img/bg/kimagureafter/downtownnight2.jpg"
image bg house outside day = "img/bg/kimagureafter/houseoutsideday.jpg"
image bg house outside evening = "img/bg/kimagureafter/houseoutsideevening.jpg"
image bg house outside night = "img/bg/kimagureafter/houseoutsidenight.jpg"
image bg house outside night 2 = "img/bg/kimagureafter/houseoutsidenight2.jpg"
image bg mystery sky = "img/bg/kimagureafter/mysterysky.jpg"
image bg street 2 day = "img/bg/kimagureafter/street2day.jpg"
image bg street 2 evening = "img/bg/kimagureafter/street2evening.jpg"
image bg street 2 night = "img/bg/kimagureafter/street2night.jpg"
image bg street 2 night 2 = "img/bg/kimagureafter/street2night2.jpg"
image bg street 2 snow day = "img/bg/kimagureafter/street2snowday.jpg"
image bg street 2 snow evening = "img/bg/kimagureafter/street2snowevening.jpg"
image bg street 2 snow night = "img/bg/kimagureafter/street2snownight.jpg"
image bg street 2 snow night 2 = "img/bg/kimagureafter/street2snownight2.jpg"
image bg street day = "img/bg/kimagureafter/streetday.jpg"
image bg street evening = "img/bg/kimagureafter/streetevening.jpg"
image bg street night = "img/bg/kimagureafter/streetnight.jpg"
image bg street night 2 = "img/bg/kimagureafter/streetnight2.jpg"

#Noraneko Games
image bg bathroom = "img/bg/noranekogames/bathroom.png"
image bg festival = "img/bg/noranekogames/festival.png"
image bg fireworks = "img/bg/noranekogames/fireworks.png"
image bg funeral = "img/bg/noranekogames/funeral.png"
image bg hallway = "img/bg/noranekogames/hallway.png"
image bg kitchen = "img/bg/noranekogames/kitchen.png"
image bg living room = "img/bg/noranekogames/livingroom.png"
image bg outside house = "img/bg/noranekogames/outsidehouse.png"
image bg restaurant = "img/bg/noranekogames/restaurant.png"

#Uncle Mugen
image bg alley = "img/bg/unclemugen/alley.jpg"
image bg around town = "img/bg/unclemugen/aroundtown.jpg"
image bg around town 2 = "img/bg/unclemugen/aroundtown2.jpg"
image bg intersection = "img/bg/unclemugen/intersection.png"
image bg intersection night = "img/bg/unclemugen/intersectionatnight.png"
image bg intersection night 2 = "img/bg/unclemugen/intersectionatnight2.png"
image bg park 2 day = "img/bg/unclemugen/park2day.jpg"
image bg park 2 night = "img/bg/unclemugen/park2night.jpg"
image bg park crossing day = "img/bg/unclemugen/parkcrossingday.jpg"
image bg park crossing snow = "img/bg/unclemugen/parkcrossingsnow.jpg"
image bg park day = "img/bg/unclemugen/parkday.jpg"
image bg sakura = "img/bg/unclemugen/sakura.jpg"
image bg snow intersection = "img/bg/unclemugen/snow intersection.jpg"
image bg random street = "img/bg/unclemugen/street.jpg"
image bg town night = "img/bg/unclemugen/townatnight.jpg"
image bg town day = "img/bg/unclemugen/townday.jpg"
image bg town sunset = "img/bg/unclemugen/townsunset.jpg"
image bg underpass day = "img/bg/unclemugen/underpassday.jpg"
image bg underpass evening = "img/bg/unclemugen/underpassevening.png"
image bg underpass night = "img/bg/unclemugen/underpassnight.jpg"

#annako
image bg bedroom = "img/bg/annako/bedroom.png"
image bg orphanage = "img/bg/annako/living room.png"

#Potat0Master
image bg danielroom = "img/bg/Potat0Master/danroom.png"
image bg diningroom = "img/bg/Potat0Master/diningroom.png"

#другое
image bg white = "img/bg/other/white.jpg"
image bg black = "img/bg/other/black.jpg"

########
# Спрайты
########

#Гвен
image gwen frown = "img/sprites/gwen/Natsumi_Casual_Closed_Frown.png"
image gwen nervous = "img/sprites/gwen/Natsumi_Casual_Closed_Open.png"
image gwen normal = "img/sprites/gwen/Natsumi_Casual_Open.png"
image gwen smile = "img/sprites/gwen/Natsumi_Casual_Smile.png"
image gwen angry = "img/sprites/gwen/Natsumi_Casual_Closed_Frown_Blush.png"
image gwen shock = "img/sprites/gwen/Natsumi_Casual_Open_Blush.png"
image gwen embarassed = "img/sprites/gwen/Natsumi_Casual_Frown_Blush.png"

#Рин
image rin frown = "img/sprites/rin/Sumi_Casual_Frown.png"
image rin nervous = "img/sprites/rin/Sumi_Casual_Closed_Open.png"
image rin normal = "img/sprites/rin/Sumi_Casual_Open.png"
image rin smile = "img/sprites/rin/Sumi_Casual_Smile.png"

#Роуз
image rose frown = "img/sprites/rose/Nora_Casual_Closed_Frown.png"
image rose nervous = "img/sprites/rose/Nora_Casual_Closed_Open.png"
image rose normal = "img/sprites/rose/Nora_Casual_Open.png"
image rose smile = "img/sprites/rose/Nora_Casual_Smile.png"
image rose angry = "img/sprites/rose/Nora_Casual_Closed_Frown_Blush.png"
image rose shock = "img/sprites/rose/Nora_Casual_Open_Blush.png"
image rose embarassed = "img/sprites/rose/Nora_Casual_Frown_Blush.png"

#Вельда
image velda frown = "img/sprites/velda/Rin_Casual_Frown.png"
image velda nervous = "img/sprites/velda/Rin_Casual_Frown_EyesClosed.png"
image velda normal = "img/sprites/velda/Rin_Casual_Smile.png"
image velda smile = "img/sprites/velda/Rin_Casual_OpenSmile.png"
image velda angry = "img/sprites/velda/Rin_Casual_Frown_EyesClosed_Blush.png"
image velda shock = "img/sprites/velda/Rin_Casual_Frown_Blush.png"
image velda embarassed = "img/sprites/velda/Rin_Casual_Frown_Blush.png"

######
# Музыка (пути остаются)
######

#Amacha Music Studio
define audio.problemsolved = "audio/music/amacha/After School Evening Sky.mp3"
define audio.peacefulmorning = "audio/music/amacha/Autumn Hill.mp3"
define audio.discomfort = "audio/music/amacha/Birds Flying In The Night Sky.mp3"
define audio.energetickids = "audio/music/amacha/Candy Bouqet.mp3"
define audio.badfeeling = "audio/music/amacha/Elegy Of Strings.mp3"
define audio.dontwanttokeepdoingthis = "audio/music/amacha/Firefly Sky.mp3"
define audio.youdontbelong = "audio/music/amacha/Hollowness And Starry Sky.mp3"
define audio.morningactivity = "audio/music/amacha/Go Out With Boots.mp3"
define audio.paineverydirection = "audio/music/amacha/Labyrinth Of Sadness.mp3"
define audio.heisgone = "audio/music/amacha/Loneliness.mp3"
define audio.happyperson = "audio/music/amacha/Lovely Flower.mp3"
define audio.hugerealization = "audio/music/amacha/Neon On A Rainy Day.mp3"
define audio.mistake = "audio/music/amacha/Piano Sinking In Water.mp3"
define audio.magic = "audio/music/amacha/Purkinhe Phenominan.mp3"
define audio.somethingisoff = "audio/music/amacha/Rain Prelude.mp3"
define audio.miracle = "audio/music/amacha/Snow Dancing In The Beech Forest.mp3"
define audio.mysterious = "audio/music/amacha/Southern Cross.mp3"
define audio.badcredits = "audio/music/amacha/Beyond The Drizzle.mp3"
define audio.neutralcredits = "audio/music/amacha/Dreaming Whale.mp3"
define audio.sadpast = "audio/music/amacha/Reality Gap.mp3"
define audio.kevintheme = "audio/music/amacha/Street Light.mp3"
define audio.stressful = "audio/music/amacha/The Emptiness Of 2 AM.mp3"
define audio.loss = "audio/music/amacha/The clear breeze of the fjord.mp3"
define audio.caronend = "audio/music/amacha/Feelings That Do Not Reach.mp3"

#Music Material
define audio.worryaboutyou = "audio/music/musicmaterial/atmosphere.mp3"
define audio.bittersweet = "audio/music/musicmaterial/By The Lake.mp3"
define audio.memories = "audio/music/musicmaterial/hidamari.mp3"
define audio.rosetheme = "audio/music/musicmaterial/kind.mp3"
define audio.regrets = "audio/music/musicmaterial/Winter Sea.mp3"

#Noiseless World
define audio.motivation = "audio/music/noiselessworld/ameagari.mp3"
define audio.movingon = "audio/music/noiselessworld/meteor.wav" #Happy
define audio.outatnight = "audio/music/noiselessworld/night.mp3" #Upbeat
define audio.dreamsandplans = "audio/music/noiselessworld/ships.mp3"
define audio.struggletomoveon = "audio/music/noiselessworld/snowfall.mp3"
define audio.gwentheme = "audio/music/noiselessworld/space3.mp3"
define audio.biggangbattle = "audio/music/noiselessworld/penguin3rd.wav"
define audio.gangbattle = "audio/music/noiselessworld/sheep.wav"

#Pocket Sound
define audio.normalday = "audio/music/pocketsound/Raspberry Scent.mp3"
define audio.opening = "audio/music/pocketsound/Strawberry Love.mp3"
define audio.timetowork = "audio/music/pocketsound/At The Surface Of Soda Water.mp3"
define audio.title = "audio/music/pocketsound/Invited To The Springy Earth.mp3"
define audio.liferoutecredits = "audio/music/pocketsound/Best Friends.mp3"

#TURBO X
define audio.calm = "audio/music/turbox/Calm Afternoon.mp3"
define audio.neverendingproblems = "audio/music/turbox/Don't Forget.mp3"
define audio.veldatheme = "audio/music/turbox/For This Day.mp3"
define audio.thingsareokay = "audio/music/turbox/Forever You.mp3"
define audio.friendcredits = "audio/music/turbox/Let The Voice.mp3"
define audio.lovecredits = "audio/music/turbox/Love Station.mp3"
define audio.happydays = "audio/music/turbox/Smile -GroovyMix-.mp3"
define audio.happyending = "audio/music/turbox/Together Forever.mp3"
define audio.date = "audio/music/turbox/Will Begin.mp3"
define audio.friendship = "audio/music/turbox/Wings.mp3"
define audio.snowydays = "audio/music/turbox/Winter Light.mp3"
define audio.prayer = "audio/music/turbox/Wish.mp3"
define audio.loveconfess = "audio/music/turbox/Premonition of the beginning.mp3"

##############
# Звуковые эффекты (пути остаются)
##############

#Sound Bible
define audio.dragging = "audio/sound/Sound Bible/trashbag.mp3"
define audio.digging = "audio/sound/Sound Bible/digging.mp3"
define audio.choke = "audio/sound/Sound Bible/choke.mp3"
define audio.clang = "audio/sound/Sound Bible/clang.mp3"
define audio.scream = "audio/sound/Sound Bible/scream.mp3"
define audio.shower = "audio/sound/Sound Bible/shower.mp3"
define audio.stab = "audio/sound/Sound Bible/stab.mp3"
define audio.static = "audio/sound/Sound Bible/static.mp3"
define audio.sirens = "audio/sound/Sound Bible/siren.mp3"
define audio.bite = "audio/sound/Sound Bible/bite.mp3"
define audio.slap = "audio/sound/Sound Bible/slap.mp3"
define audio.punch = "audio/sound/Sound Bible/punch.mp3"
define audio.kick = "audio/sound/Sound Bible/kick.mp3"
define audio.mancry = "audio/sound/Sound Bible/sadmale.mp3"
define audio.womancry = "audio/sound/Sound Bible/womancrying.mp3"

#Taira Komori
define audio.thudhard = "audio/sound/Taira Komori/hitting_a_floor2.mp3"
define audio.dining = "audio/sound/Taira Komori/clinking2.mp3"
define audio.enteringdoor = "audio/sound/Taira Komori/entering_a_house1.mp3"
define audio.fallstreets = "audio/sound/Taira Komori/fall_streets1.mp3"
define audio.heartbeat = "audio/sound/Taira Komori/heartbeat1.mp3"
define audio.kiss = "audio/sound/Taira Komori/kiss1.mp3"
define audio.kissintense = "audio/sound/Taira Komori/kiss2.mp3"
define audio.knocking = "audio/sound/Taira Komori/knocking_a_wooden_door1.mp3"
define audio.runninginhall = "audio/sound/Taira Komori/running_in_a_hall.mp3"
define audio.running = "audio/sound/Taira Komori/running1.mp3"
define audio.footsteps = "audio/sound/Taira Komori/small_footsteps.mp3"
define audio.walkingatnight = "audio/sound/Taira Komori/walking_at_night.mp3"
define audio.walkingoutside = "audio/sound/Taira Komori/walking_on_a_fall_street.mp3"
define audio.walkinginside = "audio/sound/Taira Komori/walking_on_floor1.mp3"
define audio.youmessedup = "audio/sound/Taira Komori/badend1.mp3"
define audio.doorshut = "audio/sound/Taira Komori/big_door_shut.mp3"
define audio.gulp = "audio/sound/Taira Komori/swallowing.mp3"
define audio.cutting = "audio/sound/Taira Komori/cutting.mp3"
define audio.eating = "audio/sound/Taira Komori/eating.mp3"
define audio.wind = "audio/sound/Taira Komori/wind.mp3"
define audio.sniffle = "audio/sound/Taira Komori/catching_a_cold.mp3"
define audio.eaten = "audio/sound/Taira Komori/lunch_of_a_monster1.mp3"
define audio.oven = "audio/sound/Taira Komori/oven.mp3"
define audio.jumpscare = "audio/sound/Taira Komori/surprise.mp3"
define audio.carcrash = "audio/sound/Taira Komori/car_passing.mp3"
define audio.meow = "audio/sound/Taira Komori/cat1b.mp3"
define audio.teleport = "audio/sound/Taira Komori/warp1.mp3"
define audio.ringtone = "audio/sound/Taira Komori/phone_calling.mp3"

####################################################
##################                 #################
##################  ЗАСТАВКА  #################
##################                 #################
####################################################

init:
    image splash = "ui/splash.png"

label splashscreen:


    scene black
    with Pause(0.5)

    show splash
    with dissolve
    #play sound "sfx/logo.wav"
    with Pause(2.0)

    scene black
    with dissolve
    with Pause(1.0)

    return


##########################################################
##########################################################
##########################################################

label start:

    scene bg mystery sky with fade

    if (persistent.veldaromanceclear == True or persistent.veldafriendshipclear == True) and (persistent.roseromanceclear == True or persistent.rosefriendshipclear == True) and (persistent.gwenromanceclear == True or persistent.gwenfriendshipclear == True) and persistent.liferouteclear == True:
        jump threemenuoptions
    elif (persistent.veldaromanceclear == True or persistent.veldafriendshipclear == True) and (persistent.roseromanceclear == True or persistent.rosefriendshipclear == True) and (persistent.gwenromanceclear == True or persistent.gwenfriendshipclear == True):
        jump twomenuoptions
    else:
        jump onlyonemenuoption

    # if persistent.futurerouteclear == True:
    #     jump threemenuoptions
    # elif persistent.liferouteunlocked == True:
    #     jump twomenuoptions
    # else:
    #     jump onlyonemenuoption

label onlyonemenuoption:

menu:

    "Каникулы":
        jump commonroutestart

label twomenuoptions:

menu:

    "Каникулы":
        jump commonroutestart

    "Жизнь":
        jump liferoutestart


label threemenuoptions:

menu:

    "Каникулы":
        jump commonroutestart

    "Жизнь":
        jump liferoutestart

    "Будущее":
        jump futureroutestart

label commonroutestart:

    #День 1#

    scene bg street 2 snow day with fade
    play music snowydays
    x "Я делаю глубокий вдох, впитывая знакомые пейзажи."
    x "Прошло много времени с тех пор, как я был в этом городе."
    x "Хотя это ощущается как ностальгия, я, честно говоря, не помню, что случилось в прошлый раз."
    x "Думаю, у меня просто плохая память."
    x "Что ж, думаю, стоит представиться."
    x "Меня зовут Карон Дафф, и я приеду к своему дяде на зимние каникулы."
    x "Его дом — он же ресторан, — и он, скорее всего, заставит меня работать."
    x "Я не особо против."
    x "Хоть какое-то занятие."
    x "Я смотрю в небо, радуясь, что уехал из дома."
    x "Не то чтобы там было ужасно, просто мне нравится бывать в новой обстановке время от времени."
    play sound walkingoutside
    x "Иду через город, осматриваюсь, и каждое здание выглядит так, будто не изменилось с моего последнего визита."
    x "До дома дяди удаётся добраться довольно быстро."
    stop sound fadeout 1.0
##################################################################
    scene bg restaurant with fade
    x "Когда я захожу, людей внутри не так уж много."
    x "Я замечаю только одного человека — девушку, которая протирает один из столов."

menu:

    "Представиться":
        jump introduceselftovelda

    "Не беспокоить её":
        jump donotworryaboutvelda

label introduceselftovelda:
    $ veldapoints += 1
    x "Лучше представлюсь."
    x "Если она здесь работает, я, наверное, буду её часто видеть."
    jump veldaintroduction

label donotworryaboutvelda:

    x "Лучше её не беспокоить."
    x "Пойду к себе в комнату и распакую вещи."
    jump veldaintroduction

label veldaintroduction:

    stop music fadeout 1.0
    play music veldatheme

    show velda normal with dissolve
    u "Эй, ты."
    c "А?"
    c "Ты мне?"
    show velda angry with dissolve
    u "Тут больше никого нет, придурок."
    show velda normal with dissolve
    u "Ты так и будешь стоять?"
    c "А, прости."
    show velda frown with dissolve
    u "Если ты здесь не за чем-то конкретным, проваливай."
    x "Что за девушка?"
    x "Только познакомился, а она уже ведёт себя как стерва."
    c "Я буду здесь жить какое-то время."
    show velda normal with dissolve
    u "О, так ты Карон?"
    c "Ага."
    c "А ты?"
    show velda normal with dissolve
    v "Вельда."
    show velda frown with dissolve
    v "А теперь мне нужно вернуться к работе."
    show velda angry with dissolve
    v "Не путайся у меня под ногами, и проблем не будет."
    c "Понял."
    hide velda angry with dissolve
    stop music fadeout 1.0
    x "После этого я ухожу из ресторана."
##################################################################
    scene bg living room with fade
    play music morningactivity
    x "Не проходит много времени, прежде чем я нахожу своего дядю, Дэниела."
    d "А, Карон."
    d "Ты вырос."
    c "А, д-да."
    c "Рад тебя видеть."
    d "Не нервничай."
    d "Я ведь менял тебе подгузники и купал тебя."
    c "Ты делаешь это как-то жутко."
    d "О, прости."
    d "Я не хотел."
    d "В общем, вижу, ты уже познакомился с Вельдой."
    c "Ага..."
    d "Знаю, она немного грубовата, но постарайся с ней поладить, если сможешь."
    c "Эм, ладно."
    d "Почему бы тебе не пойти распаковать вещи?"
##################################################################

    stop music fadeout 1.0
    scene bg bedroom with fade
    play sound trashbag
    x "После того как он отпускает меня, я иду к себе в комнату распаковывать вещи."
    stop sound fadeout 1.0
    x "Не уверен, что смогу привыкнуть к этому месту."
    x "Когда рядом постоянно находится раздражающая девушка вроде Вельды..."
    x "Думаю, это будет непросто."
    x "Лучше не слишком переживать об этом."
    x "Я буду жить здесь, так что придётся мириться с ней."
    x "В итоге я ложусь спать рано."
##################################################################

    #День 2#
    play music calm
    scene bg bedroom with fade
    show velda normal with dissolve
    v "Ты собираешься весь день валяться в кровати?"
    x "Я открываю глаза и вижу Вельду."
    c "Почему ты в моей комнате?"
    show velda nervous with dissolve
    v "Твой дядя попросил меня тебя разбудить."
    show velda frown with dissolve
    v "А теперь вытаскивай свою задницу из кровати."

menu:

    "Делать, как она говорит":
        jump doasyouaretold

    "Сказать ей уйти":
        jump tellveldatogoaway

    "Остаться в кровати":
        jump stayinbed

label doasyouaretold:

    $ veldapoints += 1
    c "Ладно, встаю, встаю."
    show velda smile with dissolve
    v "Хорошо."
    hide velda smile with dissolve
    play sound walkinginside
    x "Она уходит, чтобы я мог переодеться в обычную одежду."
    stop sound fadeout 1.0
    x "Она что, мой будильник?"
    jump bedroomday2

label tellveldatogoaway:
    $ veldabad += 1
    c "Уходи."
    show velda angry with dissolve
    v "Что?"
    c "Что ты делаешь в комнате парня?"
    c "Ты что, извращенка?"
    play sound slap
    x "Она бьёт меня."
    stop sound fadeout 1.0
    c "Ой..."
    show velda frown with dissolve
    v "Я пришла только разбудить тебя, идиот."
    show velda angry with dissolve
    v "С чего бы мне хотеть быть с кем-то вроде тебя!"
    hide velda angry with dissolve
    play sound walkinginside
    x "Она уходит, хлопнув дверью."
    stop sound fadeout 1.0
    x "Я... думаю, мне стоит встать, пока я не разозлил её ещё сильнее."
    jump bedroomday2

label stayinbed:
    c "Не-а, останусь в кровати."
    c "Не хочется вставать."
    show velda angry with dissolve
    v "Вставай уже, чёрт возьми."
    c "..."
    show velda normal with dissolve
    v "Если не встанешь, я вылью на тебя холодную воду."
    c "Ладно, ладно."
    c "Встаю."
    show velda smile with dissolve
    v "Хорошо."
    hide velda smile with dissolve
    play sound walkinginside
    x "Затем она уходит, чтобы я мог переодеться в обычную одежду."
    stop sound fadeout 1.0
    jump bedroomday2

label bedroomday2:

    scene bg restaurant with fade
    stop music fadeout 1.0
    play music normalday
    x "Я спускаюсь в ресторан, и ко мне подходит дядя."
    d "Доброе утро."
    c "Ага, утро..."
    x "Он смеётся."
    d "Ты не жаворонок, да?"
    c "Не особо."
    show velda normal with dissolve
    v "Что ж, тебе придётся привыкнуть."
    c "Да, я вроде как понял."
    #hide velda normal with dissolve
    d "Раз ты в городе, почему бы тебе не выйти и не осмотреться?"
    d "Ты так давно здесь не был, что вряд ли помнишь, где что."
    c "Тебе не нужна моя помощь?"
    d "Поработаешь позже."
    show velda nervous with dissolve
    v "Он говорит тебе проваливать с наших глаз."
    d "Я бы не стал формулировать это так, но да, пока выйди на улицу."
    c "Думаю, хуже не будет."
    show velda angry with dissolve
    v "Тогда хватит тратить время и вали отсюда."
    c "Ладно, ухожу!"
    hide velda angry with dissolve
##################################################################

    stop music fadeout 1.0
    scene bg street 2 snow day with fade
    x "Я выхожу на улицу по своей воле, но в то же время чувствую, что меня заставили."
    x "Интересно, куда стоит пойти сначала?"
    play sound thudhard
    x "Идя по улице, я случайно сталкиваюсь с кем-то."

    play music gwentheme

    show gwen nervous with dissolve
    u "Ай!"
    x "Оказывается, это девушка примерно моего возраста."

menu:

    "Извиниться перед ней":
        jump apologizetoher

    "Сказать ей смотреть, куда идёт":
        jump tellhertowatchwhereshesgoing

    "Ничего не говорить":
        jump dontsayanything

label apologizetoher:
    $ gwenpoints += 1
    c "Прости."
    c "Я не смотрел по сторонам."
    x "Девушка, похоже, не замечает ничего вокруг."
    c "Ты в порядке?"
    show gwen shock with dissolve
    u "А!"
    play sound running
    hide gwen shock with dissolve
    x "Она не отвечает на мой вопрос и просто убегает."
    stop sound fadeout 1.0
    jump firstgwenencounter

label tellhertowatchwhereshesgoing:
    $ gwenbad += 1
    c "Смотри, куда идёшь!"
    show gwen normal with dissolve
    u "..."
    x "Девушка выглядит так, будто сейчас заплачет."
    c "Просто будь внимательнее в следующий раз, ладно?"
    show gwen shock with dissolve
    u "А!"
    play sound running
    x "После этого она просто убегает."
    stop sound fadeout 1.0
    hide gwen frown with dissolve
    jump firstgwenencounter

label dontsayanything:

    c "..."
    show gwen normal with dissolve
    u "..."
    c "..."
    show gwen nervous with dissolve
    u "..."
    x "Ну, это неловко."
    show gwen shock with dissolve
    u "А!"
    hide gwen shock with dissolve
    play sound running
    x "Не успел я и слова сказать, как девушка убегает."
    stop sound fadeout 1.0
    jump firstgwenencounter

label firstgwenencounter:

    stop music fadeout 1.0

    x "Чёрт..."
    x "Что это было?"
    x "Лучше не буду переживать об этом."
    x "Просто попробую осмотреться в городе."
##################################################################
    scene bg park crossing snow with fade
    play music rosetheme

    play sound walkingoutside
    x "Пока я иду по городу, ко мне подходит девушка."
    stop sound fadeout 1.0
    show rose smile with dissolve
    u "Я тебя раньше не видела."
    show rose normal with dissolve
    u "Ты новенький?"
    c "А, да."
    c "Я Карон."
    c "Остановился у дяди на зимние каникулы."
    show rose nervous with dissolve
    u "О, так ты племянник Дэниела?"
    c "Ты его знаешь?"
    show rose normal with dissolve
    u "Да, все в городе его знают."
    show rose nervous with dissolve
    u "Он рассказал всем, что ты приедешь."
    x "Отлично. Значит, я теперь главная тема для сплетен в городе."
    show rose normal with dissolve
    u "О, точно."
    show rose smile with dissolve
    r "Я Роуз."
    show rose normal with dissolve
    r "Если тебе что-нибудь понадобится, я буду рада помочь."
    c "А, спасибо."
    show rose smile with dissolve
    r "Так что ты думаешь о городе пока?"

menu:

    "Мне нравится":
        jump iliketown

    "Мне не нравится":
        jump idontliketown

    "Не знаю":
        jump idktown

    "А тебе?":
        jump whataboutyou

label iliketown:
    $ rosepoints += 1
    c "Думаю, мне здесь нравится."
    show rose normal with dissolve
    r "Надеюсь, ты не передумаешь."
    c "Уверен, что нет."
    show rose nervous with dissolve
    r "Я расстроюсь, если ты врёшь."
    c "Обещаю, не вру."
    show rose normal with dissolve
    r "Ладно, я просто шучу."
    jump rosetownquestion

label idontliketown:
    $ rosebad += 1
    c "Мне не нравится."
    show rose frown with dissolve
    r "Что ж, это печально."
    show rose nervous with dissolve
    r "Я надеялась, что понравится."
    c "Прости."
    show rose frown with dissolve
    r "Не извиняйся."
    show rose normal with dissolve
    r "Не всем могут нравиться одни и те же вещи."
    c "..."
    jump rosetownquestion

label idktown:

    c "Не знаю."
    c "Я только вчера переехал к дяде."
    c "Думаю, потребуется время."
    show rose normal with dissolve
    r "Ладно, понимаю."
    show rose frown with dissolve
    r "Конечно, тебе не может сразу понравиться это место."
    c "Ты разочарована?"
    show rose nervous with dissolve
    r "Не особо."
    show rose normal with dissolve
    r "По крайней мере, ты не ненавидишь это место."
    c "Понятно."
    jump rosetownquestion

label whataboutyou:

    $ rosepoints += 1
    c "А тебе?"
    show rose shock with dissolve
    r "А?"
    c "Что ТЫ думаешь об этом городе?"
    c "Ты ведь тут живёшь, да?"
    show rose normal with dissolve
    r "Ну, мне тут нравится."
    show rose smile with dissolve
    r "Большинство людей добрые."
    c "Понятно."
    show rose nervous with dissolve
    r "А ты?"
    c "Я только что приехал, так что мне нужно время, чтобы разобраться."
    show rose normal with dissolve
    r "О, ладно."
    jump rosetownquestion

label rosetownquestion:

    show rose smile with dissolve
    r "Это всё, что я хотела знать."
    c "Хорошо."
    show rose normal with dissolve
    r "Уверена, мы ещё увидимся в будущем."

menu:

    "Надеюсь":
        jump ihopeso

    "Мне всё равно":
        jump idontreallycare

    "...":
        jump dotdotdot

label ihopeso:

    $ rosepoints += 1
    c "Надеюсь."
    x "Стоп. Я это вслух сказал?"
    show rose shock with dissolve
    r "Ты правда хочешь увидеться снова?"
    c "А, да."
    show rose smile with dissolve
    r "Определённо увидимся."
    show rose normal with dissolve
    r "Увидимся позже!"
    jump seeroseagain

label idontreallycare:

    $ rosebad += 1
    x "Честно говоря, мне всё равно, увидимся мы снова или нет."
    x "Скорее всего, мы пересечёмся."
    x "Впрочем, неважно, будем ли мы вообще общаться в будущем."
    show rose normal with dissolve
    r "Ну, увидимся!"
    jump seeroseagain

label dotdotdot:

    x "..."
    x "Я даже ничего не говорю."
    show rose normal with dissolve
    r "Что ж, мне пора идти."
    jump seeroseagain

label seeroseagain:

    stop music fadeout 1.0
    hide rose normal with dissolve
    play sound walkingoutside
    x "Роуз уходит."
    stop sound fadeout 1.0
    x "Эта девушка кажется очень милой."
    x "Почему бы ей не быть той, кто работает у дяди?"
##################################################################

    scene bg restaurant with fade
    play music gwentheme

    x "Я возвращаюсь в ресторан дяди и вижу ту девушку, что убежала от меня, — она ест одна за столиком."
    x "Не особо думая, я подхожу к ней."
    c "Эй."
    x "Девушка ничего не говорит и просто продолжает есть."
    show velda angry with dissolve
    v "Ты к клиентам пристаёшь?"
    c "Нет."
    show velda nervous with dissolve
    v "Почему бы тебе не оставить её в покое?"
    hide velda nervous with dissolve
    show gwen normal with dissolve
    u "Он мне не докучает."
    hide gwen normal with dissolve
    show velda normal with dissolve
    v "Правда?"
    hide velda normal with dissolve
    show gwen normal with dissolve
    u "Правда."
    show gwen nervous with dissolve
    u "Думаю…"
    c "Ты… думаешь…?"
    hide gwen nervous with dissolve
    show velda nervous with dissolve
    v "Он тебя беспокоит или нет?"
    hide velda nervous with dissolve
    show gwen shock with dissolve
    u "А!"
    show gwen frown with dissolve
    u "Ты тот парень, который столкнулся со мной раньше!"
    hide gwen frown with dissolve
    show velda angry with dissolve
    v "Карон..."
    c "Эй, это был несчастный случай."
    hide velda angry with dissolve
    show gwen normal with dissolve
    u "Подожди."
    show gwen frown with dissolve
    u "Это была моя вина…?"
    c "В-в общем, прости, что мы столкнулись."
    c "Эм. Я Карон."
    c "Я буду жить здесь какое-то время."
    show gwen normal with dissolve
    g "Гвен."
    c "А?"
    show gwen smile with dissolve
    g "Меня зовут Гвен."
    c "А."

menu:

    "Надеюсь, поладим":
        jump ihopewegetalong

    "Ты всегда ешь одна?":
        jump alwayseatalone

    "Больше не сталкивайся со мной":
        jump dontbumpintomeagain

label ihopewegetalong:

    $ gwenpoints += 1
    c "Надеюсь, мы поладим."
    show gwen normal with dissolve
    g "Я-Я тоже."
    show gwen nervous with dissolve
    g "..."
    c "..."
    show gwen normal with dissolve
    g "..."
    c "Да… э-э…"
    hide gwen normal with dissolve
    show velda nervous with dissolve
    v "Не обязательно продолжать её донимать."
    hide velda nervous with dissolve
    show gwen nervous with dissolve
    g "Я в порядке."
    jump gwenrestchoice

label alwayseatalone:
    c "Ты всегда ешь одна?"
    hide gwen smile with dissolve
    show velda nervous with dissolve
    v "Ты всегда такой любопытный?"
    hide velda nervous with dissolve
    show gwen frown with dissolve
    g "Н-не всегда."
    show gwen smile with dissolve
    g "Иногда Роуз со мной."
    c "Понятно."
    jump gwenrestchoice

label dontbumpintomeagain:
    $ gwenbad += 1
    c "Постарайся больше не сталкиваться со мной."
    x "Вельда злобно смотрит на меня."
    show gwen nervous with dissolve
    g "Я-Я постараюсь."
    x "Гвен опускает глаза."
    c "Эй, не переживай об этом слишком сильно."
    show gwen normal with dissolve
    g "..."
    c "Давай просто оставим это, ладно?"
    show gwen smile with dissolve
    g "Ладно."
    jump gwenrestchoice

label gwenrestchoice:

    c "Я дам тебе спокойно поесть."
    show gwen normal with dissolve
    g "Хорошо."
    hide gwen normal with dissolve
##################################################################
    scene bg restaurant with fade
    stop music fadeout 1.0
    play music veldatheme

    x "Дядя поставил меня работать в тот день после обеда."
    show velda nervous with dissolve
    v "Боже, ты ни на что не годишься."
    c "Эй, что это значит?"
    show velda frown with dissolve
    v "Ты что, никогда не учился убираться?"
    c "Стараюсь как могу, ладно?"
    show velda angry with dissolve
    v "И ты уже несколько раз забыл заказы."
    c "Ну, прости, что у меня не фотографическая память."
    show velda frown with dissolve
    v "Просто перестань облажаться."
    c "Прости."
    hide velda frown with dissolve
    x "Тихо беру швабру и подметаю у входной двери."
    x "Пока подметаю, чувствую лёгкое раздражение."
    x "Всё, что Вельда делала с тех пор, как я начал здесь работать, — это жаловалась."
    x "Очень надеюсь, что мне не придётся мириться с этим всё время."
    c "Эй, Вельда?"
    show velda frown with dissolve
    v "Что?"
    x "Видно, что она раздражена."
    c "Ты и мой дядя тут вдвоём работаете?"
    show velda normal with dissolve
    v "Ага."
    c "Понятно."
    c "Вы действительно справляетесь со всем сами?"
    show velda angry with dissolve
    v "Есть проблемы с этим?"
    c "Нет, просто кажется, что это тяжело."
    show velda frown with dissolve
    v "Тьфу."
    show velda normal with dissolve
    v "Я в порядке."
    show velda nervous with dissolve
    v "Не переживай за меня."
    c "Ладно, прости."
    show velda frown with dissolve
    v  "..."
    c "..."
    show velda normal with dissolve
    v "Ты нормально устроился?"
    c "Кажется, да."
    show velda nervous with dissolve
    v "Понятно."
    show velda normal with dissolve
    v "..."
    c "..."
    show velda nervous with dissolve
    v "..."
    c "Что ж, становится неловко."
    show velda frown with dissolve
    v "Просто заткнись и работай!"
    c "Д-да!"
    hide velda frown with dissolve
    stop music fadeout 1.0

###ПРОИГРЫВАНИЕ ИНТРО###
    $ renpy.movie_cutscene("video/WinterDreamOP.webm", delay=150, loops=0, stop_music=True)

##################################################################
    scene bg bedroom with fade
    x "Прошлой ночью я лёг спать довольно уставшим."
    x "Теперь, когда я отдохнул, лучше встать, пока Вельда не начала ворчать."
    show velda normal with dissolve
    v "Ты собираешься встать когда-нибудь в этом году?"
    x "Слишком поздно."
    c "Да, встаю."
    show velda smile with dissolve
    v "Хорошо."
    show velda nervous with dissolve
    v "Мне пришлось бы убить тебя, если бы не встал."
    c "П-прости."
    show velda angry with dissolve
    v "Давай, вставай уже."
    hide velda angry with dissolve
##################################################################

    scene bg living room with fade
    play music morningactivity

    d "Как прошла прогулка?"
    c "Нормально."
    d "Думаю, тебе нужно ещё время, чтобы освоиться, да?"
    c "Правда?"
    d "Это же твои каникулы."
    d "Хотел бы, чтобы у тебя была хоть какая-то свобода."
    c "О, ладно."
    d "Давай, иди."
    d "Поработаешь, когда вернёшься."
    c "Понял."

##################################################################

    scene bg street 2 day with fade
    x "Что мне делать?"
    x "Можно побыть с кем-нибудь..."
    x "Или побыть одному."

menu:

    "Побыть с Вельдой":
        jump hangoutwithvelda

    "Побыть с Гвен":
        jump hangoutwithgwen

    "Побыть с Роуз":
        jump hangoutwithrose

    "Побыть одному":
        jump spendtimebyself

label spendtimebyself:

    x "Нет, не хочу никого беспокоить."
    x "Проведу время один."
##################################################################
    scene bg street 2 day with fade
    stop music fadeout 1.0
    x "Гуляю и ни с кем не разговариваю."
    jump hangoutpart2

    label hangoutwithrose:

    x "Почему бы не пойти поискать Роуз?"
##################################################################
    scene bg street 2 day with fade
    stop music fadeout 1.0

    $ rosehangout1 = True
    x "К счастью, мне не нужно много времени, чтобы найти её."

    play music rosetheme

    show rose shock with dissolve
    r "Карон? Ты пришёл меня увидеть?"
    c "Возможно."
    c "Так что ты делаешь?"
    show rose normal with dissolve
    r "Собиралась пойти убрать мусор в парке."
    c "...Серьёзно?"
    show rose nervous with dissolve
    r "Ага."
    c "Что ты обычно делаешь?"
    show rose normal with dissolve
    r "Подобное."
    c "Правда?"
    show rose smile with dissolve
    r "Ага. Мне просто нравится помогать людям."
    show rose normal with dissolve
    r "Хочешь помочь?"

menu:

    "Помочь ей":
        jump helprosecleanpark

    "Не помогать":
        jump donthelprosecleanpark

label helprosecleanpark:

    $ rosepoints += 1
    c "Да, конечно."
    show rose smile with dissolve
    r "Спасибо."
    hide rose smile with dissolve
    scene bg park 2 day with fade
    play sound walkingoutside
    x "Когда мы добираемся до парка, она быстро начинает уборку."
    stop sound fadeout 1.0
    x "Мы разговариваем о мелочах, пока вместе собираем мусор."
    x "Через некоторое время мы заканчиваем."
    jump rosecleanover

label donthelprosecleanpark:

    $ rosebad += 1
    c "Нет, прости."
    c "Не особо хочу пачкать руки."
    show rose frown with dissolve
    r "А, ладно."
    hide rose frown with dissolve
    scene bg park 2 day with fade
    play sound walkingoutside
    x "Мы добрались до парка, и она быстро начала убираться."
    stop sound fadeout 1.0
    x "Мы разговариваем, пока она убирается."
    x "Мне немного неловко, что я ничего не делаю, но её это, похоже, не сильно беспокоит."
    x "Это занимает какое-то время, но она в конце концов заканчивает."
    jump rosecleanover

label rosecleanover:

    show rose smile with dissolve
    r "А, готово."
    c "Ну, это заняло какое-то время."
    show rose angry with dissolve
    r "Ага, люди слишком ленивы, чтобы выбрасывать мусор!"
    c "Да, раздражает, когда люди так делают."
    c "Но это всегда будет."
    show rose nervous with dissolve
    r "Наверное..."
    show rose smile with dissolve
    r "В любом случае, спасибо, что составил компанию."
    c "А, без проблем."
    hide rose smile with dissolve
    x "После этого мы расходимся."
    jump hangoutpart2

label hangoutwithgwen:

    x "Может, провести время с Гвен?"
##################################################################
    scene bg street 2 day with fade
    $ gwenhangout1 = True
    x "Нахожу Гвен на улице."
    show gwen normal with dissolve
    g "..."
    c "Эй."
    show gwen nervous with dissolve
    g "П-привет."
    c "Что делаешь?"
    show gwen normal with dissolve
    g "Гуляю."
    c "Понятно."
    show gwen smile with dissolve
    g "Гулять — это хорошо."
    c "...Ага."
    play sound meow
    show gwen shock with dissolve
    g "О, кот!"
    play sound running
    hide gwen nervous with dissolve
    x "Она начинает убегать."
    c "Эй, подожди!"
    stop sound fadeout 1.0
##################################################################

    scene bg street day with fade

    c "Зачем ты убежала?"
    show gwen nervous with dissolve
    g "А?"
    show gwen frown with dissolve
    g "О, точно."
    show gwen normal with dissolve
    g "Ты со мной разговаривал."
    show gwen smile with dissolve
    g "Эм, коты милые, да?"

menu:

    "Очень милые":
        jump catsarecute

    "Нормальные":
        jump catsareokay

    "Не особо":
        jump catsarenotcute

label catsarecute:

    $ gwenpoints += 1
    c "Да."
    c "Очень милые."
    show gwen normal with dissolve
    g "Да, правда?"
    c "Э, ага."
    jump gwencatquestion

label catsareokay:
    c "Нормальные, наверное."
    show gwen nervous with dissolve
    g "О."
    c "Я их не ненавижу, просто не схожу с ума по ним."
    jump gwencatquestion

label catsarenotcute:

    $ gwenpoints -= 1
    c "Не особо."
    show gwen frown with dissolve
    g "Не думаешь, что они милые?"
    c "Не-а."
    show gwen normal with dissolve
    g "..."
    jump gwencatquestion

label gwencatquestion:
    c "Так что там с тем котом, за которым ты убежала?"
    show gwen nervous with dissolve
    g "Каким котом?"
    c "..."
    show gwen shock with dissolve #Шок
    g "О!"
    play sound meow
    show gwen smile with dissolve
    g "Вот он!"
    play sound running
    hide gwen smile with dissolve
    x "Она снова убегает за ним."
    stop sound fadeout 1.0
    c "Эй, подожди!"
    x "Из-за Гвен мне не удавалось долго стоять на месте."
    jump hangoutpart2

label hangoutwithvelda:

    x "Хотел бы побыть с Вельдой, даже если она немного раздражает."
##################################################################
    $ veldahangout1 = True

    scene bg restaurant with fade
    play music veldatheme

    x "Она работает в ресторане."
    c "Эй."
    show velda nervous with dissolve
    v "Я работаю, придурок."
    show velda angry with dissolve
    v "Уходи."
    c "Ладно..."
    hide velda angry with dissolve
    stop music fadeout 1.0
##################################################################
    scene bg street 2 day with fade
    x "Ну, это была пустая трата времени."
    x "Подожди..."
    x "Я здесь живу."
    x "Возвращаюсь."
##################################################################

    play music veldatheme
    scene bg restaurant with fade
    c "Я вернулся!"
    show velda angry with dissolve
    v "Я же сказала тебе уйти?"
    c "Да ладно."
    c "Не будь такой."
    show velda nervous with dissolve
    v "Что ж, не хочу тебя здесь видеть."
    c "Почему?"
    show velda angry with dissolve
    v "Потому что не хочу!"

menu:

    "Я думал, мы друзья":
        jump veldafriends

    "Ты мне не особо нравишься":
        jump dontlikevelda

    "Прости, что так чувствуешь":
        jump sorryyoufeelthatway

label veldafriends:
    $ veldapoints += 1
    c "Я думал, мы друзья..."
    show velda nervous with dissolve
    v "Друзья?"
    show velda angry with dissolve
    v "Ты думаешь, я буду дружить с кем-то вроде тебя?"
    c "Так, я ошибся?"
    show velda normal with dissolve
    v "..."
    c "У тебя вообще нет друзей...?"
    show velda angry with dissolve
    v "Заткнись!"
    c "..."
    x "Странно, но она не выглядит сильно расстроенной."
    jump respondtovelda

label dontlikevelda:
    $ veldabad += 1
    c "Честно говоря, ты мне не особо нравишься."
    show velda smile with dissolve
    v "Ты мне тоже не нравишься."
    c "..."
    show velda nervous with dissolve
    v "..."
    c "..."
    show velda normal with dissolve
    v "Это всё?"
    c "Ага."
    show velda nervous with dissolve
    v "Боже, ты раздражаешь."
    c "Взаимно."
    show velda frown with dissolve
    v "Заткнись."
    jump respondtovelda

label sorryyoufeelthatway:
    $ veldapoints += 1
    c "Что ж, прости, что ты так себя чувствуешь."
    show velda normal with dissolve
    v "А я нет."
    c "Да, я почему-то так и думал."
    c "И я подумал, что тебе хотелось бы с кем-нибудь поговорить."
    c "Похоже, я ошибся."
    jump respondtovelda

label respondtovelda:
    show velda nervous with dissolve
    v "..."
    c "Что ж, я пойду."
    show velda normal with dissolve
    v "Если вернёшься, я тебя убью."
    c "Это угроза?"
    show velda angry with dissolve
    v "Просто проваливай уже."
    c "Ладно, ухожу!"
    hide velda angry with dissolve
    jump hangoutpart2

label hangoutpart2:

##################################################################

    scene bg street 2 day with fade
    stop music fadeout 1.0
    x "У меня ещё есть немного времени."
    x "С кем бы провести время?"

menu:

    "Побыть с Вельдой":
        jump hangoutwithvelda2

    "Побыть с Гвен":
        jump hangoutwithgwen2

    "Побыть с Роуз":
        jump hangoutwithrose2

    "Побыть одному":
        jump spendtimebyself2

label spendtimebyself2:

    x "Хм... хотел бы побыть один."
    x "Приятно побыть какое-то время с самим собой."
##################################################################
    scene bg street 2 day with fade
    x "Гуляю и ни с кем не разговариваю."
    $ hangoutalone = True
    jump hangoutover

label hangoutwithrose2:
    x "Хочу снова увидеться с Роуз."
##################################################################
    scene bg street 2 day with fade
    play music rosetheme
    x "Не проходит много времени, прежде чем я её нахожу."

    if rosehangout1 == True:
        jump part1rosedone
    else:
        jump part1roseoff

label part1rosedone:
    show rose smile with dissolve
    r "Ты снова пришёл меня увидеть?"
    c "Ага."
    show rose normal with dissolve
    r "Понятно."
    $ achievement.grant("Rose_Twice")
    jump rosehangchecker

label part1roseoff:
    show rose normal with dissolve
    r "Карон?"
    c "Эй."
    c "Так что ты делаешь?"
    jump rosehangchecker

label rosehangchecker:

    show rose smile with dissolve
    r "Несу еду в банк продовольствия."
    c "Ты всегда делаешь такое?"
    show rose normal with dissolve
    r "Ага."
    c "Я тебе мешаю?"
    show rose nervous with dissolve
    r "Н-нет."
    show rose frown with dissolve
    r "С чего ты взял?"
    c "Просто не хочу тебе докучать."
    show rose smile with dissolve
    r "Ты мне не докучаешь."
    show rose normal with dissolve
    r "Всё в порядке."
    show rose smile with dissolve
    r "Хочешь пойти со мной?"

menu:

    "Пойти с ней":
        jump gowithherfoodbank

    "Не идти":
        jump dontgofoodbank

label gowithherfoodbank:
    $ rosepoints += 1
    c "Ага."
    c "Пойду с тобой."
    show rose normal with dissolve
    r "Спасибо."
    hide rose normal with dissolve
    x "И затем мы вместе доставляем еду в банк продовольствия."
    jump foodbankover

label  dontgofoodbank:
    $ rosebad += 1
    c "Я пас."
    c "Прости."
    show rose frown with dissolve
    r "Не переживай."
    x "Она выглядит немного грустной..."
    c "Что ж, увидимся."
    hide rose frown with dissolve
    jump foodbankover

label foodbankover:
    stop music fadeout 1.0
    x "После этого мы расходимся."
    jump hangoutover

label hangoutwithgwen2:

    x "Хотел бы пойти и увидеться с Гвен."
##################################################################
    scene bg street 2 day with fade
    x "Не проходит много времени, прежде чем я её нахожу."
    play music gwentheme

    if gwenhangout1 == True:
        jump part1gwendone
    else:
        jump part1gwenoff

label part1gwendone:
    show gwen smile with dissolve
    g "Эй, это... как тебя зовут?"
    c "Карон."
    show gwen nervous with dissolve
    g "Ты забыл, как меня зовут?"
    c "Нет, Гвен. Не забыл."
    show gwen normal with dissolve
    g "Я переживала, что если забуду твоё, ты забудешь моё."
    c "С каких пор это так работает?"
    $ achievement.grant("Gwen_Twice")
    c "Так ты всё ещё ищешь котов?"
    jump gwenhangchecker

label part1gwenoff:
    c "Эй."
    show gwen normal with dissolve
    g "..."
    show gwen nervous with dissolve
    g "Ты...?"
    c "Уже забыла обо мне?"
    show gwen frown with dissolve
    g "П-прости."
    c "Мы встретились в ресторане дяди."
    show gwen shock with dissolve
    g "О, ты тот парень!"
    c "Единственный и неповторимый."
    c "Так чем ты занималась?"
    show gwen normal with dissolve
    g "Раньше я гонялась за котом."
    c "Ты всё ещё планируешь это делать?"
    jump gwenhangchecker

label gwenhangchecker:
    show gwen nervous with dissolve
    g "Нет."
    c "Тогда что ты делаешь?"
    show gwen smile with dissolve
    g "Считаю, сколько машин увидела."
    c "Тебе это нравится?"
    show gwen normal with dissolve
    g "Ага."
    c "Сколько уже насчитала?"
    show gwen smile with dissolve
    g "Одну!"
    x "Она выглядит такой счастливой..."
    show gwen normal with dissolve
    g "О, ещё одна!"
    show gwen nervous with dissolve
    g "Хех."
    c "Что?"
    show gwen smile with dissolve
    g "Это значит, что я выигрываю."

menu:

    "Да, выигрываешь":
        jump gweniswinning

    "Я не собираюсь тебе проигрывать":
        jump imnotlosingtoyou

    "Мне плевать":
        jump dontcareaboutgwengame

label gweniswinning:

    $ gwenpoints += 1
    c "Да, выигрываешь."
    show gwen normal with dissolve
    g "Знаю."
    c "..."
    jump gwengame

label imnotlosingtoyou:

    $ gwenpoints += 1
    c "Я не собираюсь тебе проигрывать!"
    show gwen nervous with dissolve
    g "Что ж, ты не победишь!"
    c "Правда?"
    show gwen normal with dissolve
    g "Ага!"
    jump gwengame

label dontcareaboutgwengame:

    $ gwenbad += 1
    c "Мне плевать."
    show gwen nervous with dissolve
    g "Тогда зачем ты здесь?"
    c "Не знаю."
    c "Скучно, наверное."
    jump gwengame

label gwengame:
    show gwen smile with dissolve
    g "Хочешь посчитать машин со мной?"
    c "..."
    c "А почему бы и нет?"
    hide gwen smile with dissolve
    x "И мы вдвоём считаем проезжающие машины."
    x "Неудивительно, что победила Гвен."
    x "В основном потому, что она посчитала машину, которую видела до моего прихода."
    x "Думаю, просто позволю ей выиграть..."
    stop music fadeout 1.0
    jump hangoutover

label hangoutwithvelda2:

    x "Интересно, хорошая ли идея поговорить с Вельдой..."
##################################################################

    scene bg restaurant with fade
    play music veldatheme

    if veldahangout1 == True:
        jump part1veldadone
    else:
        jump part1veldaoff

label part1veldadone:
    show velda angry with dissolve
    v "Я же сказала тебе не возвращаться?"
    show velda nervous with dissolve
    v "Хочешь умереть, да?"
    $ achievement.grant("Velda_Twice")
    c "Я просто хотел снова тебя увидеть..."
    show velda embarassed with dissolve
    v "..."
    show velda angry with dissolve
    v "У-уходи!"
    c "Нет."
    show velda nervous with dissolve
    v "Уф."
    show velda normal with dissolve
    v "Ладно..."
    show velda nervous with dissolve
    v "Думаю, тебе позволено остаться."
    jump veldahangchecker

label part1veldaoff:
    show velda normal with dissolve
    v "Чего тебе?"
    c "Побыть с тобой."
    show velda nervous with dissolve
    v "..."
    show velda angry with dissolve
    v "Проваливай!"
    c "Что?"
    c "В чём проблема?"
    show velda nervous with dissolve
    v "Я не хочу быть с ТОБОЙ."
    c "О, я как-то странно выразился?"
    c "Я просто хотел провести с тобой время."
    show velda frown with dissolve
    v "Что ж, а я нет."
    show velda nervous with dissolve
    v "Ты же знаешь, что у меня работа, да?"
    c "А ты знаешь, что я здесь живу, да?"
    show velda frown with dissolve
    v "Уф."
    show velda nervous with dissolve
    v "Думаю, не могу тебя выгнать..."
    jump veldahangchecker

label veldahangchecker:
    show velda frown with dissolve
    v "Есть причина, по которой ты хочешь меня достать?"
    c "Потому что могу."
    show velda nervous with dissolve
    v "Почему не можешь достать кого-то другого?"

menu:

    "Хочу узнать о тебе больше":
        jump knowmoreaboutvelda

    "Тебя весело доставать":
        jump youarefuntoannoy

label knowmoreaboutvelda:
    $ veldapoints += 1
    c "Потому что хочу узнать о тебе больше..."
    show velda embarassed with dissolve
    v "..."
    show velda nervous with dissolve
    v "Ты хочешь узнать... обо мне?"
    c "Ага."
    show velda frown with dissolve
    v "Что ж, особо нечего рассказать."
    c "Или ты просто не хочешь говорить."
    show velda nervous with dissolve
    v "..."
    c "Ладно. Не обязательно сегодня."
    show velda normal with dissolve
    v "..."
    jump answerveldaquestion

label youarefuntoannoy:
    $ veldabad += 1
    c "Потому что тебя весело доставать."
    show velda angry with dissolve
    v "Что это, чёрт возьми, должно значить!?"
    c "Это значит, что мне нравится тебя доставать."
    show velda frown with dissolve
    v "Оставь меня, ублюдок."
    c "Что с тобой и постоянными ругательствами?"
    show velda nervous with dissolve
    v "У тебя проблемы с тем, как я говорю?"
    c "Может быть..."
    show velda angry with dissolve
    v "Иди к чёрту!"
    c "Планирую."
    jump answerveldaquestion

label answerveldaquestion:
    c "Так... как работа?"
    show velda nervous with dissolve
    v "Нормально, пока ты не пришёл меня доставать."
    c "Ты работаешь, Вельда?"
    show velda frown with dissolve
    v "Работала, пока ты не пришёл меня доставать."
    c "Почему ты остановилась?"
    show velda angry with dissolve
    v "Заткнись!"
    hide velda angry with dissolve
    x "Поговорив с ней какое-то время, я наконец решаю оставить её в покое."
    stop music fadeout 1.0
    jump hangoutover

label hangoutover:

    scene bg street 2 evening with fade

    if hangoutalone == True:
        jump alonehangoutover
    else:
        jump nonlonerhangout

label alonehangoutover:
    x "Я уже какое-то время хожу по городу..."
    jump lonerhangoutcheck

label nonlonerhangout:
    x "После того как я провёл с ней время, решил пройтись по городу."
    jump lonerhangoutcheck

label lonerhangoutcheck:

    x "Вскоре я понимаю, сколько времени прошло."
    x "Мне нужно вернуться в ресторан."
##################################################################
    scene bg restaurant with fade
    x "Я снова работаю, и Вельда продолжает жаловаться на мои ошибки."
    x "После этого я готовлюсь ко сну."
    scene bg bedroom with fade

    if rosepoints >= 3:
        jump rosecommon
    elif gwenpoints >= 3:
        jump gwencommon
    elif veldapoints >= 2:
        jump veldacommon
    else:
        jump neutralroute

label rosecommon:
    x "С нетерпением жду, чтобы провести больше времени с Роуз в будущем."
    x "Она, честно говоря, один из самых добрых людей, которых я встречал."
    x "Если честно, она кажется немного слишком идеальной..."
    x "Что ж, у меня остаток каникул, чтобы узнать о ней больше."
    x "Пока я думаю о ней, засыпаю."
    jump roseroutestart

label gwencommon:

    x "Гвен кажется интересной девушкой."
    x "Она немного застенчивая, правда."
    x "Честно говоря, думаю, она довольно милая."
    x "В любом случае, с нетерпением жду возможности проводить с ней больше времени в будущем."
    x "Затем засыпаю."
    jump gwenroutestart

label veldacommon:

    x "Я постепенно привыкаю к тому, как Вельда разговаривает."
    x "Хотелось бы, чтобы она была чуть добрее."
    x "Думаю, прошу слишком многого."
    x "В любом случае, я хочу проводить с ней больше времени."
    x "Не проходит много времени, как я засыпаю."
    jump veldaroutestart

label neutralroute:

    x "Эти последние несколько дней были... чем-то."
    x "Просто не знаю, что чувствовать обо всём этом."
    x "Лучше просто наслаждаться остатком каникул."
    x "Быстро засыпаю."
##################################################################
    scene bg restaurant with fade
    play music regrets
    x "На следующее утро я встаю до того, как Вельда заходит в мою комнату."
    d "Ты рано встал."
    c "А, да."
    d "Тебе нужно ещё времени на улице?"
    c "Нет."
    d "Значит, ты можешь ориентироваться в городе, не теряясь?"
    c "Я бы хотел поработать."
    d "Правда?"
    c "Да. Пожалуйста, дай мне поработать."
    d "О."
    d "Что ж, ладно."
    x "Остаток зимних каникул я провожу за работой."
    x "Я не утруждал себя тем, чтобы проводить время с кем-то из тех, кого встретил."
    x "Я просто работал на дядю и не часто выходил."
    x "Все, кого я встретил, были просто ещё одним человеком в моей жизни."
    x "У них не было для меня какого-то особого значения."
    x "Возможно, если бы я сделал другой выбор, всё было бы иначе."
    x "Однако то, что сделано, уже не отменить."
    x "Это просто одна печальная правда."
    $ achievement.grant("Loner_Ending")
    x "НЕЙТРАЛЬНАЯ КОНЦОВКА — ОДИНОЧКА"
    $ renpy.movie_cutscene("video/NeutralCredits.webm", delay=100, loops=0, stop_music=True)
    #Нейтральные титры
    return
