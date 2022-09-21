input.onButtonPressed(Button.A, function () {
    logging = !(logging)
    if (logging) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
let logging = false
datalogger.deleteLog(datalogger.DeleteType.Full)
logging = false
let toggle = true
music.playTone(262, music.beat(BeatFraction.Sixteenth))
basic.forever(function () {
	
})
loops.everyInterval(100, function () {
    if (logging) {
        datalogger.log(
        datalogger.createCV("Light", input.lightLevel()),
        datalogger.createCV("Temp", input.temperature())
        )
        if (toggle) {
            basic.showLeds(`
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . #
                `)
        } else {
            basic.showLeds(`
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                `)
        }
        toggle = !(toggle)
    }
})
