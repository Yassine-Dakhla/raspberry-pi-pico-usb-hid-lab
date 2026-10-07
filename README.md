# Raspberry Pi Pico USB HID Security Lab

A hands-on security lab using a Raspberry Pi Pico as a USB Human Interface Device (HID).

This project explores USB HID behavior, keyboard emulation, keyboard-layout compatibility, and the security implications of trusted USB peripherals.

## Objectives

- Understand how USB HID devices work
- Experiment with Raspberry Pi Pico keyboard emulation
- Test HID behavior on Linux and Windows
- Investigate keyboard-layout compatibility
- Build safe and controlled HID demonstrations
- Document security risks related to untrusted USB devices

## Hardware

- Raspberry Pi Pico
- USB cable
- Test computer

## Software

The exact software and libraries used for each experiment will be documented alongside the implementation.

Testing may include:

- Linux
- Windows
- Raspberry Pi Pico firmware and HID libraries

## Project Structure

```text
raspberry-pi-pico-usb-hid-lab/
├── README.md
├── src/
├── payloads/
├── docs/
├── images/
└── LICENSE
```

## Experiments

### 1. Basic USB HID

Configure the Raspberry Pi Pico to identify as a USB keyboard and send controlled keystrokes to a test machine.

### 2. Keyboard Layout Compatibility

Investigate how keyboard layouts can affect HID input.

Layouts of interest include:

- QWERTY
- AZERTY
- QWERTZ

The goal is to understand why identical HID keystrokes can produce different characters depending on the target system's keyboard configuration.

### 3. Cross-Platform Testing

Test HID behavior in controlled environments running Linux and Windows.

Compatibility issues, observations, and limitations will be documented as the experiments are completed.

### 4. Security Considerations

Explore why USB HID devices can present a security risk when an attacker has physical access to a computer.

Testing is limited to systems owned by or explicitly authorized by the tester.

## Lab Methodology

1. Define the experiment
2. Prepare an isolated test environment
3. Connect the Raspberry Pi Pico
4. Run a controlled HID demonstration
5. Record the results
6. Document problems and limitations
7. Improve the implementation

## Current Status

**Project status:** In development

| Experiment | Status |
|---|---|
| Pico setup | In progress |
| Basic USB HID | Planned |
| Keyboard-layout testing | Planned |
| Linux testing | Planned |
| Windows testing | Planned |
| Documentation | In progress |

## Security Disclaimer

This project is intended for educational purposes and authorized security testing.

Only use the device and associated software on systems you own or have explicit permission to test. Do not use the techniques documented here to access, modify, or interfere with systems without authorization.

## Author

**Yassine Dakhla**

Cybersecurity student interested in Linux, networking, infrastructure, and security research.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
