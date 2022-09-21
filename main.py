def on_button_pressed_a():
    global logging
    logging = not (logging)
    if logging:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play_tone(247, music.beat(BeatFraction.SIXTEENTH))
    datalogger.delete_log(datalogger.DeleteType.FAST)
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

logging = False
logging = False
toggle = True
music.play_tone(247, music.beat(BeatFraction.SIXTEENTH))
datalogger.mirror_to_serial(True)

def on_every_interval():
    global toggle
    if logging:
        datalogger.log(datalogger.create_cv("Light", input.light_level()),
            datalogger.create_cv("Temp", input.temperature()))
        if toggle:
            basic.show_leds("""
                . . . . .
                                . . . . #
                                . . . # .
                                # . # . .
                                . # . . #
            """)
        else:
            basic.show_leds("""
                . . . . .
                                . . . . #
                                . . . # .
                                # . # . .
                                . # . . .
            """)
        toggle = not (toggle)
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
