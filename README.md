# 7SegGearDisplay

## Goal
This project aims to fully design a PCB board and device to display a 7-segment number.\
This will display the gear I am using for my manual transmission car. 

## Step 1 - Initial design of the PCB (Jan 23, 2025)
Using my pi5 and Python, I needed to create a display and light pattern for the 7-segment display. Because the Pi5 is new, a lot of libraries are incompatible with the GPIO pins. Thus I had to experiment. I finally came across GPIOzero which worked great. After implementing the library, I was able to successfully blink LED's. The patterns were then super easy to code. 

<br>
Components used:
<ul><li>7x Red LED</li><li>7x 100 Ohm Resistors</li><li>Raspberry pi</li></ul>

![Initial PCB design with lights](https://github.com/user-attachments/assets/7263fc55-0d7c-4f9b-ae6c-17341c92e7a7)

Note: This was a proof of concept. This must be reprogrammed in a lower-level language on an embedded microcontroller.
