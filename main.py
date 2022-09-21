def on_button_pressed_a():
    global logging
    logging = not (logging)
    if not (logging):
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play_tone(247, music.beat(BeatFraction.SIXTEENTH))
    datalogger.delete_log(datalogger.DeleteType.FAST)
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

logging = False
tempDeg = 0
maxtempDeg = -100
mintempDeg = 200
tempADC = 0
logging = False
toggle = True
strip = neopixel.create(DigitalPin.P8, 13, NeoPixelMode.RGB)
strip.set_brightness(50)
strip.clear()
strip.show()
basic.show_icon(IconNames.NO)
resistance = [157.2,
    148.1,
    139.4,
    131.3,
    123.7,
    116.6,
    110,
    103.7,
    97.9,
    92.5,
    87.43,
    82.79,
    78.44,
    74.36,
    70.53,
    66.92,
    63.54,
    60.34,
    57.33,
    54.5,
    51.82,
    49.28,
    46.89,
    44.62,
    42.48,
    40.45,
    38.53,
    36.7,
    34.97,
    33.33,
    31.77,
    30.25,
    28.82,
    27.45,
    26.16,
    24.94,
    23.77,
    22.67,
    21.62,
    20.63,
    19.68,
    18.78,
    17.93,
    17.12,
    16.35,
    15.62,
    14.93,
    14.26,
    13.63,
    13.04,
    12.47,
    11.92,
    11.41,
    10.91,
    10.45,
    10,
    9.575,
    9.17,
    8.784,
    8.416,
    8.064,
    7.73,
    7.41,
    7.106,
    6.815,
    6.538,
    6.273,
    6.02,
    5.778,
    5.548,
    5.327,
    5.117,
    4.915,
    4.723,
    4.539,
    4.363,
    4.195,
    4.034,
    3.88,
    3.733,
    3.592,
    3.457,
    3.328,
    3.204,
    3.086,
    2.972,
    2.863,
    2.759,
    2.659,
    2.564,
    2.472,
    2.384,
    2.299,
    2.218,
    2.141,
    2.066,
    1.994,
    1.926,
    1.86,
    1.796,
    1.735,
    1.677,
    1.621,
    1.567,
    1.515,
    1.465,
    1.417,
    1.371,
    1.326,
    1.284,
    1.243,
    1.203,
    1.165,
    1.128,
    1.093,
    1.059,
    1.027,
    0.9955,
    0.9654,
    0.9363,
    0.9083,
    0.8812,
    0.855,
    0.8297,
    0.8052,
    0.7816,
    0.7587,
    0.7366,
    0.7152,
    0.6945,
    0.6744,
    0.6558,
    0.6376,
    0.6199,
    0.6026,
    0.5858,
    0.5694,
    0.5535,
    0.538,
    0.5229,
    0.5083,
    0.4941,
    0.4803,
    0.4669,
    0.4539,
    0.4412,
    0.429,
    0.4171,
    0.4055,
    0.3944,
    0.3835]
temp = [-30,
    -29,
    -28,
    -27,
    -26,
    -25,
    -24,
    -23,
    -22,
    -21,
    -20,
    -19,
    -18,
    -17,
    -16,
    -15,
    -14,
    -13,
    -12,
    -11,
    -10,
    -9,
    -8,
    -7,
    -6,
    -5,
    -4,
    -3,
    -2,
    -1,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120]
music.play_tone(247, music.beat(BeatFraction.SIXTEENTH))
def interpolate(value: number, x: List[number] = [], y: List[number] = []):
    # return value + x +y
    # find the index in x array that is smaller than x
    index = 0
    for test_x in x:
        if test_x < value:
            break
        index += 1
    return Math.map(value, x[index - 1], x[index], y[index - 1], y[index])
temperature = Math.map(5, 5, -365, 16, 4)
temperature2 = interpolate(150, resistance, temp)

def on_every_interval():
    global tempADC, tempDeg, toggle, mintempDeg, maxtempDeg
    if logging:
        tempADC = pins.analog_read_pin(AnalogPin.P1)
        tempDeg = interpolate(10 / (1023 / tempADC - 1), resistance, temp)
        
        #determine if we have new max and min temps
        mintempDeg = min(mintempDeg, tempDeg)
        maxtempDeg = max(maxtempDeg, tempDeg)
        
        datalogger.log(datalogger.create_cv("Light", input.light_level()),
            datalogger.create_cv("Temp", input.temperature()),
            datalogger.create_cv("Temp_Thermistor", tempDeg))
        strip.clear()
        #strip.set_pixel_color(Math.map(input.temperature(), 25, 30, 0, 12),
        #    neopixel.colors(NeoPixelColors.VIOLET))
        
        strip.set_pixel_color(Math.map(tempDeg, mintempDeg, maxtempDeg, 0, 12),
                        neopixel.colors(NeoPixelColors.VIOLET))

        strip.show()
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
    else:
        strip.clear()
        strip.show()
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval2():
    global tempADC, tempDeg
    tempADC = pins.analog_read_pin(AnalogPin.P1)
    tempDeg = interpolate(10 / (1023 / tempADC - 1), resistance, temp)
loops.every_interval(3600000, on_every_interval2)
