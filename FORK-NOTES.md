# RESIN-V1: fork notes (Formlabs SLA variant)

This branch (`resin-v1`) carries a variant of this case for Formlabs SLA resin
printers. Everything on `main` is upstream; only the files below differ.

## Provenance

- Upstream: `clawdbotatg/clawd-pico-case` (GitHub), commit `b7024a88847314481a9450f4539fe98d7243e32e` (2026-10-15)
- License: MIT, Copyright (c) 2026 Austin Griffith. Retained; this variant is a
  downstream fork, not part of Austin's mainline process (see `PROCESS.md`),
  and it is **CAD-validated but not physically tested**.
- Author of the variant changes: MidnightOnMars (2026-10-23).

## What changed vs upstream `stl/current` (v1.9+J24)

| File | Change |
|---|---|
| `cad/v1_7_lock.py` | `HOOK` 0.5 -> 0.45 mm; closing ramp `Z_RAMP_TOP` +2.4 -> +3.0 (28 deg -> 18.8 deg from vertical); lid catch pocket 0.55 -> 0.50 deep, skin 0.85 -> 0.90 |
| `cad/resin_v1_assemble.py` | new: assembles the resin set, uses the J24-B full-flange joystick |
| `stl/resin-v1/` | lid, base, joystick (J24-B: full 0.40 mm flange, was 0.24 mm thin edge), button (byte-identical to tested v1.0), full-set, `resin-v1.json` (hashes) |
| `stl/resin-v1/README.md` | print sheet: material per part, PreForm steps, wash/cure |

Nothing else changed: outer dimensions identical (33.04 x 58.6 x 18.67 mm), and
the untouched parts are byte-identical to upstream's tested exports.

## Validation

Repo checks all pass (6 catches, single solids, joystick caught-on-pull with
5.1 deg minimum tilt clearance, <=45 deg overhangs, hardware clearances).
Independent mesh measurement: joystick min thickness 0.400 mm (was 0.240),
lid min wall 0.89 mm (was 0.85), all parts watertight.

## Why these changes

Resin SLA parts are stiffer and more notch-sensitive than PETG FDM parts, and
they are dimensionally more accurate. The thin 0.24 mm joystick flange was the
weakest feature (below Formlabs' 0.2 mm minimum guidance and load-bearing); the
snap was eased because the clear resin lid skirt is the flexing member and
resin does not yield like PETG.

## Rebuild

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python cad/v1_7_lock.py   # base + lid, validated
.venv/bin/python cad/v1_9.py        # v1.9 lid + joystick reference
.venv/bin/python cad/joystick_j24.py # A and B joysticks, validated
.venv/bin/python cad/resin_v1_assemble.py  # writes stl/resin-v1/
```

## Printing

See `stl/resin-v1/README.md`. One Form Studio 1: Alpha Clear lid and base, Tough
2000 V2 joystick, Flexible 80A V2 buttons (x4). All three resins are Form Studio 1
compatible.
