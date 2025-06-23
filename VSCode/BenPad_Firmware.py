import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Define row and column pins
row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
col_pins = (board.GP0, board.GP1)

# Set up the key matrix
keys = keypad.KeyMatrix(
    row_pins=row_pins,
    column_pins=col_pins,
    columns_to_anodes=False  # Diodes from switch to row
)

# Initialize keyboard HID
keyboard = Keyboard(usb_hid.devices)

# Define keymap for numbers 1–8
keymap = [
    Keycode.ONE,     # S1 (Row 1, Col 1)
    Keycode.TWO,     # S2 (Row 1, Col 2)
    Keycode.FOUR,    # S3 (Row 2, Col 2)
    Keycode.THREE,   # S4 (Row 2, Col 1)
    Keycode.FIVE,    # S5 (Row 3, Col 1)
    Keycode.SIX,     # S6 (Row 3, Col 2)
    Keycode.SEVEN,   # S7 (Row 4, Col 1)
    Keycode.EIGHT    # S8 (Row 4, Col 2)
]

pressed_keys = set()

while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            if key_number < len(keymap):
                keyboard.press(keymap[key_number])
                pressed_keys.add(key_number)
        elif event.released:
            if key_number in pressed_keys:
                keyboard.release(keymap[key_number])
                pressed_keys.remove(key_number)
    time.sleep(0.01)
