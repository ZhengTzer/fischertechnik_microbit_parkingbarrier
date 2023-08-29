function closeGate () {
    // while switch is open
    while (pins.digitalReadPin(DigitalPin.P0) == 0) {
        pins.digitalWritePin(DigitalPin.P15, 0)
        // main gear turn anti-clockwise, gate close
        pins.digitalWritePin(DigitalPin.P16, 1)
    }
    // when switch is close, turn 0
    // 
    pins.digitalWritePin(DigitalPin.P16, 0)
}
function openGate () {
    // while switch is open
    while (pins.digitalReadPin(DigitalPin.P2) == 0) {
        // main gear turn clockwise, gate open
        pins.digitalWritePin(DigitalPin.P15, 1)
        pins.digitalWritePin(DigitalPin.P16, 0)
    }
    // when switch is close, turn 0
    // 
    pins.digitalWritePin(DigitalPin.P15, 0)
}
basic.showIcon(IconNames.SmallHeart)
pins.digitalWritePin(DigitalPin.P14, 1)
// init gate closing
closeGate()
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P1) < 500) {
        openGate()
    } else {
        // wait vehicle pass through
        basic.pause(3000)
        closeGate()
    }
})
