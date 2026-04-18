print("Starting")

import board
import busio

# TODO:
# - Add macros

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

## Keyboard Configuration:

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())
keyboard.modules = [layers, holdtap, encoder_handler]

keyboard.col_pins = (board.GP20, board.GP19, board.GP18)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

## OLED Configuration:
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(i2c=i2c_bus)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

display.entries = [
    ImageEntry(image="img.bmp", x=0, y=0),
]
keyboard.extensions.append(display)

## Macro Definitions and Keymaps:

MSG1 = KC.MACRO("GGWP")
MSG2 = KC.MACRO("Care flank, enemies behind you")

encoder_handler.pins = (
    # regular direction encoder
    (board.D6, board.D7, None,),
    )

keyboard.keymap = [
    [KC.MUTE, KC.MNXT, KC.MPRV, KC.MPLY, KC.MSTP, MSG1, MSG2, KC.H, KC.I, KC.J, KC.K, KC.L]
]

encoder_handler.map = [ ((KC.UP, KC.DOWN),),]

if __name__ == '__main__':
    keyboard.go()
    