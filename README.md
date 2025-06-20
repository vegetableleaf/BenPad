# BenPad
## Overview & Key Features
Hey guys, this is my first project for Hack Club's Highway program. For my HackPad, I decided to opt for an 8-key macropad, placed in a 4x2 arrangement. The keys correspond to the numbers 1-8, from left to right then top to bottom, with their output being displayed on an OLED screen.

## CAD Designs
The case is made from PLA plastic & consists 2 pieces: a (carefully carved out) base and a lid.
### Full build
Different angles of the complete build are shown below:
![Screenshot 2025-06-20 020106](https://github.com/user-attachments/assets/676d0f33-ce54-4ab9-895d-a3c643ae27d7)
![Screenshot 2025-06-20 020157](https://github.com/user-attachments/assets/af87bf48-1e46-44ec-a660-8e7382286ac6)
![image](https://github.com/user-attachments/assets/77e6594c-66c0-42a1-b51b-2123151a8c13)

### Exploded View
This better shows how all the different components fit together. The circuitry sits snugly inside the base, with the lid resting right on top. 4 M3x16mm screws are driven downwards through the lid and base, and secured by M3x5x4 heatset inserts
![image](https://github.com/user-attachments/assets/e3cd45a2-cafa-4575-acbf-d06d620cee0e)


## BOM
- 1 Seeed XIAO RP2040 Microcontroller (as required by Hack Club, not much of a choice there)
- 1 0.91-inch 4-pin 128x32 OLED screen
- 8 DO-35 Diodes
- 8 Cherry MX switches
- 4 M3x16mm screws
- 4 M3x5x4 heatset inserts
- 1 Case -#(see above) 
- 1 PCB Board! -#(details below)

## Schematic & PCB
I designed both the Schematic and PCB using KiCad.

### Schematic
![Screenshot 2025-06-20 014516](https://github.com/user-attachments/assets/04378f10-3f18-4e6c-b5da-f31b66053820)

### PCB
![image](https://github.com/user-attachments/assets/31aa3373-1d73-4120-a343-781981b3436b)

## Firmware
The BenPad uses KMK for firmware (attached in the repo)
