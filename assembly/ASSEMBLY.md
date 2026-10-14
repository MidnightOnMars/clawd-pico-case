# Assembly

Photos in order. Draft. This becomes a one-page guide later.

## 1. Cable and tools

You need a 4-wire cable with a small plug on one end, plus wire cutters and strippers.

![Cable and strippers](photos/01-cable-and-strippers.jpg)

## 2. Plug the cable into the Trust M board

Wire order across the plug, top to bottom in the photo: white, yellow, black, red.

![Cable plugged into Trust M](photos/02-cable-into-trust-m.jpg)

## 3. Cut and strip the wires

Cut the cable short, leaving the plug end. Strip the tip of each of the 4 wires.
<!-- TODO: how long to cut, how much to strip -->

![Cut and stripped](photos/03-cut-and-stripped-a.jpg)
![Cut and stripped, other view](photos/03-cut-and-stripped-b.jpg)

## 4. Lay out the screen board and the wiring guide

Take out the LCD board. Turn it face down so the header pins point at you, USB at the top.

Each wire goes into the header socket shown. No solder. Count from the USB end.

| Wire | Signal | Pico pin |
|---|---|---|
| White | GND | 3rd on the USB-side row (pin 38) |
| Yellow | 3.3 V | 5th on that row (pin 36) |
| Black | SDA | 6th on the other row (pin 6, GP4) |
| Red | SCL | 7th on the other row (pin 7, GP5) |

<!-- TODO: redraw the wiring guide as a clean diagram for the one-pager -->

![Board face down with wiring guide](photos/04-board-and-wiring-guide.jpg)

## 5. Push in white and yellow

Twist the strands at each wire tip tight, so each tip acts like one solid wire.

Push white into socket 3 (GND) and yellow into socket 5 (3V3) on the USB-side row. Do both together.

![White and yellow in the header](photos/05-white-yellow-in-header.jpg)

## 6. Tape over the wires

Put a small piece of electrical tape over the sockets, right on top of the wires, to hold them in.

![Tape over white and yellow](photos/06-tape-over-wires.jpg)

## 7. Poke the holes open

Push a stiff breadboard jumper wire through the tape into each covered socket. This opens the holes so the Pico pins fit later. The tape still holds the wires.

![Poking holes through the tape](photos/07-poke-holes-through-tape.jpg)
