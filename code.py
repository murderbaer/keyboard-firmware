# pyright: reportShadowedImports=false

import board

from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
print("Starting")


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())


keyboard.row_pins = (board.GP5, board.GP7, board.GP8, board.GP9, board.GP10)
keyboard.col_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
                     board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

MOMENTARY = KC.MO(1)

keyboard.keymap = [
    [
        KC.ESCAPE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.GRAVE,

        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE,

        KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.NO, KC.ENTER, KC.PGUP,

        KC.LSHIFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.PGDOWN,

        KC.LCTRL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RALT, MOMENTARY, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT
    ],
    [
        KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEBUG,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.RESET,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.AUDIO_VOL_UP, KC.TRNS,

        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.AUDIO_VOL_DOWN, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
