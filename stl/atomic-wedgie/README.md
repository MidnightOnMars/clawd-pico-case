# Atomic Wedgie: print this

For a Waveshare RP2040-Plus with a battery. Same case as `stl/current/`, with
a different base: a channel in the end wall (away from the USB) for the
battery plug and wire, a BOOT pin hole, and a RESET plunger (`aw-reset-plunger.stl`).

**`aw-reset-plunger.stl` is not a front button.** It is the small RESET plunger that sits in this base only. If someone asks for "buttons", they mean the four front caps, `../current/button.stl`. Print the RESET button only for an Atomic Wedgie, one per base.

| File | Copies | Colour |
|---|---|---|
| `base.stl` (this folder) | 1 | Red |
| `aw-reset-plunger.stl` (this folder) | 1 | Black |
| `../current/lid.stl` | 1 | White |
| `../current/joystick.stl` | 1 | Grey |
| `../current/button.stl` | 4 | 2 grey (middle two), 1 green (top right), 1 red (bottom right) |

All PETG. 0.16 mm layers, 4 walls, no supports, no brim, no raft. Don't
rotate the parts (base floor down, caps flange down).

Assembly: drop the RESET plunger into its hole from inside the base, flange
up, before the board goes in.

Source: base `cad/aw2_base.py`, RESET plunger `cad/aw_reset_v3.py`.
