# Experiment 1 — Basic USB HID Keyboard

## Objective

Verify that the Raspberry Pi Pico running CircuitPython is recognized as a USB HID keyboard and can type a harmless test string into a focused text editor.

## Environment

Fill in these details when you run the experiment:

- Date:
- Pico model:
- CircuitPython version:
- HID library bundle version:
- Host operating system and version:
- Host keyboard layout:
- USB cable:
- Result: Not tested

## Procedure

1. Install CircuitPython and the matching `adafruit_hid` library using [setup.md](setup.md).
2. Copy `src/code.py` to the root of the `CIRCUITPY` drive.
3. Open a blank document in a plain-text editor on a computer you own or are authorized to test.
4. Connect the Pico normally and wait for the countdown.
5. Check whether the expected text appears.
6. Record the result and capture a screenshot of the text editor and/or CIRCUITPY files, avoiding personal information.

## Expected result

The text editor receives:

```text
USB HID lab: Raspberry Pi Pico keyboard test.
```

## Results

Do not mark this experiment as passed until you have run it.

- Observed behavior:
- Expected vs. actual:
- Keyboard layout:
- Errors or limitations:
- Screenshot path:
- Status: Not tested

## Security observation

A USB keyboard is generally trusted to provide input. A device that emulates a keyboard can therefore send input to the currently focused application. This demonstration is intentionally limited to a harmless line of text and should only be run in an authorized test environment.
