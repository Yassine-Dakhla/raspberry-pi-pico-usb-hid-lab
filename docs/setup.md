# Setup Guide

This guide prepares a Raspberry Pi Pico for the first USB HID experiment.

## Requirements

- Raspberry Pi Pico (the original Pico is sufficient)
- A USB data cable
- A computer you own or are explicitly authorized to test
- A plain-text editor
- CircuitPython firmware for the exact Pico board
- The Adafruit CircuitPython HID library bundle matching your CircuitPython version

## 1. Install CircuitPython

1. Download the current stable CircuitPython UF2 for your exact Pico model from the official CircuitPython downloads page: https://circuitpython.org/downloads
2. Disconnect the Pico.
3. Hold the **BOOTSEL** button while connecting the Pico to USB.
4. Release BOOTSEL when the **RPI-RP2** drive appears.
5. Copy the downloaded UF2 file to that drive.
6. Wait for the board to reboot. It should appear as a **CIRCUITPY** drive.

Do not use firmware intended for a different board model.

## 2. Install the HID library

1. Download the Adafruit CircuitPython Library Bundle that matches your CircuitPython major/minor version: https://circuitpython.org/libraries
2. Extract the bundle on your computer.
3. Copy the `adafruit_hid` folder from the bundle's `lib` directory into the Pico's `CIRCUITPY/lib/` directory.
4. Confirm these files exist:
   - `CIRCUITPY/lib/adafruit_hid/keyboard.mpy`
   - `CIRCUITPY/lib/adafruit_hid/keyboard_layout_us.mpy`

The exact file extension or bundle contents can vary by library release; use the matching bundle documentation if the paths differ.

## 3. Copy the demo

1. Copy this repository's `src/code.py` to the root of the `CIRCUITPY` drive.
2. Open a plain-text editor on your own test computer and click in the empty document.
3. Connect the Pico normally, without holding BOOTSEL.
4. Wait for the five-second countdown. The Pico should type one harmless line.

**Important:** HID input goes to whichever application has keyboard focus. Save your work and close sensitive windows before testing. If the wrong characters appear, check the target computer's keyboard layout; this initial example uses a US layout.

## Troubleshooting

- **No CIRCUITPY drive:** confirm the UF2 is for the correct board and repeat the BOOTSEL procedure.
- **ImportError for adafruit_hid:** check that the library folder is inside `CIRCUITPY/lib/` and matches the installed CircuitPython version.
- **Nothing is typed:** check that the text editor has focus, USB HID is enabled by the firmware, and the board has no errors on its serial console.
- **Wrong punctuation:** the example uses US keyboard mapping. Host keyboard layouts can affect the displayed characters.

## Safety

Use only on systems you own or have permission to test. Do not adapt the demo to execute commands, collect credentials, evade security controls, or modify another person's system.
