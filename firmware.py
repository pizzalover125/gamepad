import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.keys import KC

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

direct_gpio_pins = [
    board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8
]

direct_scanner = KeysScanner(
    pins=direct_gpio_pins,
    value_when_pressed=False,
    pull=True
)


keyboard.matrix = [direct_scanner]

keyboard.keymap = [
    [
        KC.W, KC.D, KC.S, KC.A, KC.UP, KC.RIGHT, KC.DOWN, KC.LEFT
    ]
]

if __name__ == '__main__':
    keyboard.go()
