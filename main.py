def closeGate():
    while pins.digital_read_pin(DigitalPin.P0) == 0:
        pins.digital_write_pin(DigitalPin.P15, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
    pins.digital_write_pin(DigitalPin.P16, 0)
def openGate():
    while pins.digital_read_pin(DigitalPin.P2) == 0:
        pins.digital_write_pin(DigitalPin.P15, 1)
        pins.digital_write_pin(DigitalPin.P16, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
basic.show_icon(IconNames.SMALL_HEART)
pins.digital_write_pin(DigitalPin.P14, 1)
closeGate()
basic.show_icon(IconNames.HEART)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P1) < 500:
        openGate()
    else:
        basic.pause(5000)
        closeGate()
basic.forever(on_forever)

def on_in_background():
    if pins.digital_read_pin(DigitalPin.P0) == 1 or pins.digital_read_pin(DigitalPin.P2) == 1:
        while True:
            basic.show_icon(IconNames.SQUARE)
            basic.pause(500)
            basic.show_icon(IconNames.SMALL_SQUARE)
            basic.pause(500)
    else:
        basic.show_icon(IconNames.YES)
control.in_background(on_in_background)
