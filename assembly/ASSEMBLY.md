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

## 8. Same on the other row: black and red

Push black into socket 6 and red into socket 7. Tape over them. Poke the holes open with the jumper wire.

![Black and red, with guide](photos/08-black-red-guide.jpg)
![Black and red in the header](photos/08-black-red-in-header.jpg)
![Black and red taped](photos/08-black-red-taped.jpg)

## 9. Header ready

All 4 wires in, taped, holes open. Ready for the Pico W.

![Header ready for the Pico](photos/09-header-ready.jpg)

## 10. Stack the boards

Wedge the Trust M board in between the Pico and the screen board. Push the Pico all the way into the header so it's flush. No pins or wires sticking out, chip fully inside.

If anything sticks out, do it again. It won't fit the case.

![Stacked, from the top](photos/10-stacked-top.jpg)
![Chip wedged in between](photos/10-chip-wedged.jpg)
![Headers flush](photos/10-headers-flush.jpg)

## 11. Test the boards

Hold BOOTSEL and plug in the USB. Go to wedgie.dev/test and click Test it. Don't unplug while it runs.

Wait for the first 3 to go green: Board, Firmware, Chip. That means everything is connected. Unplug it. The other 3 (Shake, Buttons, Colors) come after the case is on.

![Hold BOOTSEL, plug in](photos/11-bootsel.jpg)
![Test page](photos/11-test-page.jpg)
![Wiping, putting MicroPython on](photos/11-test-wiping.jpg)
![Installing the firmware](photos/11-test-firmware.jpg)

## 12. Pick the base

- Red: Pico W with a battery (the Atomic wedgie)
- Black: Trust M chip
- Gray: ATECC608 chip

This build is Trust M, so black.

![The three bases](photos/12-bases.jpg)

## 13. Peel the screen protector

Pull the blue tab.

![Screen protector off](photos/13-screen-protector.jpg)

## 14. Case parts

White lid, black base, joystick cap, 2 gray buttons, 1 green, 1 red.

![Case parts](photos/14-case-parts.jpg)

## 15. Joystick cap

Line up the square hole with the joystick and press hard until it snaps. It takes more force than you'd think.

Check: it stays on upside down, and it clicks up, down, left, right and in. The cap sits flat with a small gap under its rim. The gap is on purpose, so it can tilt.

![Joystick cap, side](photos/15-joystick-side.jpg)
![The gap under the rim](photos/15-joystick-gap.jpg)
![Joystick cap on](photos/15-joystick-on.jpg)

## 16. Buttons into the lid

Lay the lid face down at the edge of the mat, so the buttons can hang out the front. Drop the buttons in with tweezers: green, gray, gray, red.

<!-- TODO: confirm green sits over A and red over Y -->

![Placing buttons with tweezers](photos/16-buttons-tweezers.jpg)
![Buttons placed](photos/16-buttons-placed.jpg)
![Lid, boards and base ready](photos/16-ready.jpg)

## 17. Boards into the base

Push the stacked boards into the black base. The screen board lies flat across the base's rails. The USB port is centered in the hole, so a cable plugs in cleanly.

![USB centered in the hole](photos/17-usb-centered.jpg)
![Boards in the base](photos/17-in-base.jpg)

## 18. Close the case

Lower the base, screen side down, into the lid. Line it up. Keep it upside down and press lid and base together, hard, until they snap. It's tight on purpose, so it won't fall apart.

![Lowering into the lid](photos/18-lower-into-lid.jpg)
![Pressed closed](photos/18-press-closed.jpg)
![Closed](photos/18-closed.jpg)
![USB port, closed](photos/18-closed-usb.jpg)

## 19. Check the feel

Press every button. Push the joystick every way and straight in. Each one should click. Look for anything off: a tilted joystick, a stuck button.

## 20. Full test

Plug it in. Go to wedgie.dev/test and click Test only (skips the wipe and firmware). Press green on the wedgie to let the computer in.

- Chip: wait for the green check.
- Shake: shake, tap, squeeze, lightly drop it on each side until the counter stops. It hammers the chip and the Pico to catch loose wires.
- Buttons: press each one it asks for. The joystick must not hit the wrong button.
- Colors: each press shows a color. Check for scratches, dead pixels, or a line of printer plastic. Clean it off.

PASS, then "No software" on the screen: done. Unplug it.

<!-- TODO: the red FULL CONTROL screen (photo 20-full-control): what should a builder press? -->

![Plugged in](photos/20-booted.jpg)
![Test only](photos/20-test-only.jpg)
![Press green](photos/20-press-green.jpg)
![Full control warning](photos/20-full-control.jpg)
![Shake it](photos/20-shake.jpg)
![Button test](photos/20-buttons.jpg)
![Color test](photos/20-colors.jpg)
![PASS on the wedgie](photos/20-pass.jpg)
![PASS on the page](photos/20-pass-page.jpg)
![No software](photos/20-no-software.jpg)

## 21. Box it

Put it in the box. Build the next one. To use it: wedgie.dev/connect.

![In the box](photos/21-box.jpg)
