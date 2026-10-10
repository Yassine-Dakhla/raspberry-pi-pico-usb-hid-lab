"""Basic Raspberry Pi Pico USB HID keyboard demonstration.

Target: Raspberry Pi Pico running CircuitPython.
Before use: open a plain-text editor on a computer you own or are
authorized to test, then connect the Pico and wait for the countdown.

This demo only types a harmless line of text. It does not run commands,
download files, or change system settings.
"""

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Give yourself time to focus a text editor after connecting the Pico.
COUNTDOWN_SECONDS = 5
DEMO_TEXT = "USB HID lab: Raspberry Pi Pico keyboard test."

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

print("USB HID demo started.")
print("Focus a plain-text editor. Typing begins in 5 seconds.")

for remaining in range(COUNTDOWN_SECONDS, 0, -1):
    print(remaining)
    time.sleep(1)

layout.write(DEMO_TEXT + "\n")
keyboard.release_all()

print("Demo complete.")
