input.onButtonPressed(Button.A, function () {
    logging = !(logging)
    if (logging) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
let logging = false
logging = false
basic.forever(function () {
	
})
loops.everyInterval(100, function () {
    if (logging) {
        datalogger.log(
        datalogger.createCV("Light", input.lightLevel()),
        datalogger.createCV("Temp", input.temperature())
        )
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `)
    }
})
