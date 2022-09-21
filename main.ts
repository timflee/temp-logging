input.onButtonPressed(Button.A, function () {
    logging = !(logging)
    if (logging) {
    	
    } else {
    	
    }
})
input.onButtonPressed(Button.AB, function () {
    music.playTone(247, music.beat(BeatFraction.Sixteenth))
    datalogger.deleteLog(datalogger.DeleteType.Fast)
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
})
let logging = false
logging = false
let toggle = true
basic.showIcon(IconNames.No)
music.playTone(247, music.beat(BeatFraction.Sixteenth))
loops.everyInterval(500, function () {
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
basic.forever(function () {
	
})
