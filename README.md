# Raspberry Pi Pico USB HID Security Lab

A hands-on lab exploring USB Human Interface Device (HID) behavior using a Raspberry Pi Pico. The project focuses on keyboard emulation, keyboard-layout compatibility, safe testing, and the security implications of trusted USB peripherals.

## Objectives

- Understand how USB HID keyboards are recognized by host systems.
- Build and test a simple CircuitPython HID demonstration.
- Observe how keyboard layouts affect typed characters.
- Record reproducible results on Linux and Windows where available.
- Document security lessons and limitations using evidence from real tests.

## Hardware and software

**Hardware**
- Raspberry Pi Pico (original Pico supported by the chosen firmware)
- USB data cable
- A computer you own or are authorized to test

**Software**
- CircuitPython firmware for the exact Pico model
- Matching Adafruit CircuitPython Library Bundle
- A plain-text editor on the host computer

See [Setup Guide](docs/setup.md) for installation instructions.

## Repository structure

```text
raspberry-pi-pico-usb-hid-lab/
├── README.md
├── src/
│   └── code.py
├── payloads/
│   └── README.md
├── docs/
│   ├── setup.md
│   ├── test-plan.md
│   └── experiment-log-template.md
├── images/
└── LICENSE
```

## Experiments

### Experiment 1 — Basic USB HID keyboard

The starter program in `src/code.py` waits five seconds, then types a harmless informational line into the currently focused application. It does not execute commands or change system settings.

**Status: Implementation added; hardware test not yet confirmed.**

1. Follow the [Setup Guide](docs/setup.md).
2. Copy `src/code.py` to the root of the Pico's `CIRCUITPY` drive as `code.py`.
3. Focus a blank text editor on your test computer.
4. Connect the Pico normally and wait for the countdown.
5. Record the result using the [Experiment 1 test plan](docs/test-plan.md).

### Experiment 2 — Keyboard-layout compatibility

Compare the expected output with the actual output on different host keyboard layouts (for example, US QWERTY and French AZERTY). Record the host layout and any character differences. This experiment should only be marked complete after testing.

### Experiment 3 — Cross-platform behavior

When available, repeat the basic test on authorized Linux and Windows systems. Record the operating system version, firmware, library version, and observed behavior.

## Methodology

1. Define the experiment and expected outcome.
2. Prepare a controlled environment.
3. Run the demonstration on an authorized test computer.
4. Record the actual result and any errors.
5. Capture screenshots that do not expose personal information.
6. Document limitations and follow-up questions.

Use [docs/experiment-log-template.md](docs/experiment-log-template.md) to record additional experiments.

## Current status

| Item | Status |
|---|---|
| Repository structure | Added |
| CircuitPython setup guide | Added |
| Basic HID demo code | Added; not yet hardware-verified |
| Experiment 1 test plan | Added |
| Keyboard-layout testing | Planned |
| Linux/Windows comparison | Planned |
| Screenshots and evidence | To be added after testing |

## Safety and scope

This is an educational project for systems owned by the author or explicitly authorized for testing. The initial demo types one visible, harmless line of text. Do not use this project to collect credentials, execute unauthorized commands, evade security controls, or interfere with other people's systems.

## Author

**Yassine Dakhla**  
Cybersecurity student interested in Linux, networking, infrastructure, and security research.

## License

Released under the MIT License. See [LICENSE](LICENSE).
