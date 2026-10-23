# resin-v1 print sheet (Formlabs SLA)

Resin variant of the repo's `v1.9+J24` case (Austin's tested PETG design), generated
from the build123d source. **CAD-validated, not physically tested.** Provenance and
change log: [`FORK-NOTES.md`](../../FORK-NOTES.md).

## Parts

| File | Copies | Colour | Resin | Printer |
|---|---|---|---|---|
| `lid.stl` | 1 | Clear | Alpha Clear Resin | Form Studio 1 |
| `base.stl` | 1 | Clear | Alpha Clear Resin | Form Studio 1 |
| `joystick.stl` | 1 | Dark grey | Tough 2000 Resin V2 | Form Studio 1 or Form 4 |
| `button.stl` | 4 | Black | Flexible 80A Resin V2 | Form Studio 1 or Form 4 |
| `full-set.stl` | 1 set | single colour (fit test) | Tough 2000 Resin V2 recommended | any |

All three resins are Form Studio 1 compatible. One Form Studio 1 prints the whole
case in three prints, three tank swaps: (1) lid + base in Alpha Clear, (2) joystick
in Tough 2000, (3) buttons x4 in Flexible 80A. Suggested first build: `full-set.stl`
in Tough 2000 V2 to validate every fit with one print; the joystick from that print
is the real part, keep it.

## PreForm (per print)

1. Import the part STL. Select printer: Form Studio 1 (or Form 4 if that is the
   machine in the tank) and the resin; PreForm applies the material profile.
2. Keep the orientation as shipped (lid face down, base floor down, caps flange
   down). The parts were designed flat-on-platform, which means the fewest supports.
3. Auto-generate supports. Expect supports under the joystick ball underside and
   under the base catch tips; scars are small and hidden under the lid. Flexible
   supports pull off by hand; rigid ones clip with flush cutters.
4. Leave layer height at the material default (Alpha Clear: 100 um).
5. Arrange one part per plate, or use the full-set for the single-material test.

## Post-processing

- Alpha Clear: wash in >= 90% IPA or Formlabs Resin Washing Solution, air dry at
  least 30 min. Post-cure optional but recommended for full strength; use the Alpha
  preset on Form Studio Wash+Cure or Form Cure.
- Tough 2000 V2: wash and post-cure required; use the material preset.
- Flexible 80A V2: wash and post-cure required; use the material preset. Keep wash
  time short for thin features (the 0.4 mm button flange can absorb IPA).
- Clear lid and base: the platform-side faces print frosted (the base floor bottom
  and the lid's outer top). Functional as-is; wet-sand and polish for a glassier
  look. Expect visible layer lines and small support scars on the base's outer wall
  at the catch line (the catch undersides get supports; they are invisible on a
  black base). Wash thoroughly and dry; a clear case shows any IPA residue or dust
  inside.

## Fit notes

- The design's inter-part clearances are 0.15-0.30 mm. Resin holds ~+/-0.06 mm on
  33-80 mm features (Form 4 design guide), so fits will be at least as good as PETG,
  probably slightly snugger. The mating gap is 0.2 mm; if the lid is stiff to close,
  it is the snap, not the fit (below).
- Snap closure: catches now hook 0.45 mm with an 18.8 deg closing ramp (was 0.5 mm /
  28 deg) so the clear lid skirt flexes less and closes with less force. It may still
  feel firm. Open with the pry slot.
- Alpha Clear heat deflection is 57 C: keep the case out of hot cars and prolonged
  direct sun. Indoor/handheld use is fine.

## Files

SHA-256 of every STL in this directory: `resin-v1.json` (same format as
`stl/current/current.json`). `full-set.stl` is all seven parts on one plate in one
colour.

## Rebuild

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python cad/v1_7_lock.py    # base + lid, validated
.venv/bin/python cad/v1_9.py         # v1.9 lid + joystick reference
.venv/bin/python cad/joystick_j24.py # A and B joysticks, validated
.venv/bin/python cad/resin_v1_assemble.py  # writes stl/resin-v1/
```
