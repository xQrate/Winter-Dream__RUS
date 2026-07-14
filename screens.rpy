# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    tag menu
    add "ui/titlevisualmenubar.png"
    #add "ui/menus/mainmenu/flower.png"

    imagemap:

        ground "ui/menus/mainmenu/mm_ground.png"
        idle "ui/menus/mainmenu/mm_ground.png"
        hover "ui/menus/mainmenu/mm_hover.png"
        alpha False
        cache False


        hotspot (10,550,280,160) action Start() at buttonfade
        hotspot (335,550,280,160) action ShowMenu('load') at buttonfade
        hotspot (640, 550, 280, 160) action ShowMenu("preferences") at buttonfade
        hotspot (980,550,280,160) action Quit(confirm=False) at buttonfade




##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Вернуться") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить") action ShowMenu("save")
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Помощь") action Help()
        textbutton _("Выход") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
screen file_picker:

    imagemap:
            ground "ui/menus/saveload/sl_ground.png"
            hover "ui/menus/saveload/sl_hover.png"


            idle "ui/menus/saveload/sl_ground.png"
            selected_idle "ui/menus/saveload/sl_hover.png"
            selected_hover "ui/menus/saveload/sl_hover.png"


            add "ui/menus/saveload/sl_ground.png"


            cache False
            alpha False

            hotspot (100,460,100,130) at buttonfade action FilePagePrevious()
            hotspot (850,460,100,130) at buttonfade action FilePageNext(max=5)


            #hotspot (100, 460, 100, 130) at buttonfade clicked FilePage("auto")
            hotspot (205, 460, 100, 130) at buttonfade clicked FilePage("1")
            hotspot (305, 460, 100, 130) at buttonfade clicked FilePage("2")
            hotspot (450, 460, 100, 130) at buttonfade clicked FilePage("3")
            hotspot (590, 460, 100, 130) at buttonfade clicked FilePage("4")
            hotspot (730, 460, 100, 130) at buttonfade clicked FilePage("5")

            hotspot(920,260,290,72) action MainMenu()
            hotspot(920,330,290,72) action Quit(confirm=True)

            hotspot(50,590,400,200) action Return() at buttonfade


            hotspot (140,160,250,300) clicked FileAction(1):
                use load_save_slot(number=1)
                key "save_delete" action FileDelete(1)
            hotspot (395,160,250,300)   clicked FileAction(2):
                use load_save_slot(number=2)
                key "save_delete" action FileDelete(2)
            hotspot (650,160,250,300)   clicked FileAction(3):
                use load_save_slot(number=3)
                key "save_delete" action FileDelete(3)

            add "ui/menus/saveload/sl_overlay.png"




screen save:

    # This ensures that any other menu screen is replaced.
    tag menu


    use file_picker

    add "ui/menus/saveload/add_save_label.png"



screen load:

    # This ensures that any other menu screen is replaced.
    tag menu


    use file_picker

    add "ui/menus/saveload/add_load_label.png"


##############################################
#############                   ################
##############  LOAD SAVE SLOTS  #################
#############                   ################
##############################################



screen load_save_slot:
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 3),
                        FileTime(number, empty=_("Пустой слот")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 11 ypos 38
    text file_text xpos 55 ypos 225 size 23 drop_shadow [(1, 2)] #font "palooka-bb.regular.ttf"




init -2 python:

    #config.thumbnail_width = 237
    #config.thumbnail_height = 250

    config.thumbnail_width = 228
    config.thumbnail_height = 200

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:


    tag menu

    add "ui/background.png"



    imagemap:

            ground "ui/menus/prefs/pm_ground.png"
            hover "ui/menus/prefs/pm_hover.png"
            selected_idle "ui/menus/prefs/pm_hover.png"
            alpha False
            cache False

            hotspot(145,206,250,85) action Preference("display", "window") at buttonfade
            hotspot(395,206,255,87) action Preference("display", "fullscreen") at buttonfade

            hotspot(145,345,250,75) action Preference("skip", "seen") at buttonfade
            hotspot(395,345,250,75) action Preference("skip", "all") at buttonfade

            hotspot(145,425,250,75) action Preference("after choices", "skip") at buttonfade
            hotspot(395,425,250,75) action Preference("after choices", "stop") at buttonfade

            hotspot(800,500,290,65) action MainMenu()
            hotspot(800,565,160,65) action ShowMenu("сохранить")
            hotspot(1000,565,160,65) action ShowMenu("загрузить")

            hotspot(50,580,400,200) action Return() at buttonfade

            bar pos (900, 155) value Preference("music volume") style "pref_slider"
            bar pos (900, 230) value Preference("sound volume") style "pref_slider"
            bar pos (900, 300) value Preference("text speed") style "pref_slider"
            bar pos (900, 375) value Preference("auto-forward time") style "pref_slider"


init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.left_bar = "ui/menus/prefs/bar_full.png"
    style.pref_slider.right_bar = "ui/menus/prefs/bar_empty.png"
    style.pref_slider.hover_left_bar = "ui/menus/prefs/bar_full.png"
    style.pref_slider.ymaximum = 50
    style.pref_slider.xmaximum = 250
    style.pref_slider.thumb = "ui/menus/prefs/thumb.png"


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    #on "show" action With(dissolve)

    #modal True

    add "ui/background.png"

    imagemap:
        ground 'ui/menus/yesno/yesno_ground.png'
        idle 'ui/menus/yesno/yesno_idle.png'
        hover 'ui/menus/yesno/yesno_hover.png'


        hotspot (400,350,235,150) action yes_action at buttonfade
        hotspot (640,350,235,150) action no_action at buttonfade



    if message == layout.ARE_YOU_SURE:
        add "ui/menus/yesno/yesno_are_you_sure.png"

    elif message == layout.DELETE_SAVE:
        add "ui/menus/yesno/yesno_delete_save.png"

    elif message == layout.OVERWRITE_SAVE:
        add "ui/menus/yesno/yesno_overwrite_save.png"

    elif message == layout.LOADING:
        #add "ui/menus/yesno/yesno_loading.png"
        add "ui/menus/yesno/yesno_are_you_sure.png"


    elif message == layout.QUIT:
        add "ui/menus/yesno/yesno_quit.png"

    elif message == layout.MAIN_MENU:
        add "ui/menus/yesno/yesno_main_menu.png"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    imagemap:
        xpos 25
        ypos 398
        alpha False
        cache False
        ground "ui/menus/quickmenu/qm_ground.png"
        idle "ui/blank.png"
        hover "ui/menus/quickmenu/qm_hover.png"
        selected_idle "ui/menus/quickmenu/qm_hover.png"
        selected_hover "ui/menus/quickmenu/qm_hover.png"


        hotspot (745,250,100,80) action ShowMenu('сохранить') at buttonfade
        hotspot (850,250,50,80) action ShowMenu('загрузить') at buttonfade
        hotspot (910,250,50,80) action Preference("auto-forward", "toggle") at buttonfade
        hotspot (970,250,50,80) action ShowMenu('настройки') at buttonfade


transform buttonfade:

    on idle:
        alpha 1.0
    on hover:
            alpha 0.0
            linear 0.1 alpha 1.0
    on selected_hover:
            alpha 0.0
            linear 0.1 alpha 1.0
