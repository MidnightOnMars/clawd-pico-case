# Clawd Pico Case, RESIN-V1 (for Formlabs SLA)

Resin variant of the repo's `v1.9+J24` case (Austin's tested PETG design), generated
from the build123d source. CAD-validated by the repo's own checks plus independent
mesh measurement. **Not physically tested.** The repo's `stl/current/` PETG files
remain the tested state; this is a parallel set for resin.

## Files

| File | Material | Copies |
|---|---|---|
| `lid.stl` | Alpha Clear Resin (Form Studio 1) | 1 |
| `base.stl` | Alpha Clear Resin (Form Studio 1) | 1 |
| `joystick.stl` | Tough 2000 Resin V2 (grey) | 1 |
| `button.stl` | Flexible 80A Resin V2 (black) | 4 |
| `full-set.stl` | single-color test set (all 7 parts, one material) | 1 |

All three resins are Form Studio 1 compatible (Alpha Clear is FS1-only; Tough 2000 V2
and Flexible 80A V2 also run on Form 4 series). One Form Studio 1 can print the whole
set: three prints, three tank swaps (lid + base together in Alpha Clear, joystick,
buttons).

Suggested first build: `full-set.stl` in Tough 2000 V2 (grey) to validate fit with one
print, then the multi-material set.

## PreForm (per print)

1. Import the part STL. Select printer: Form Studio 1 (or Form 4 if that is the
   machine in the tank) and the resin; PreForm applies the material profile.
2. Keep the orientation as shipped (lid face down, base floor down, caps flange down).
   The parts were designed flat-on-platform, which means the fewest supports.
3. Auto-generate supports. Expect supports under the joystick ball underside and under
   the base catch tips; scars are small and hidden under the lid. Flexible supports
   pull off by hand; rigid ones clip with flush cutters.
4. Leave layer height at the material default (Alpha Clear: 100 um).
5. Arrange one part per plate (or use the full-set for the single-material test).

## Post-processing

- Alpha Clear / Alpha Black: wash in >= 90% IPA or Formlabs Resin Washing Solution,
  air dry at least 30 min. Post-cure optional but recommended for full strength; use
  the Alpha preset on Form Studio Wash+Cure or Form Cure.
- Tough 2000 V2: wash and post-cure required; use the material preset.
- Flexible 80A V2: wash and post-cure required; use the material preset. Keep wash
  time short for thin features (the 0.4 mm button flange can absorb IPA).
- Clear lid and base: the platform-side faces print frosted (the base floor bottom and
  the lid's outer top). Functional as-is; wet-sand and polish for a glassier look.
  Expect visible layer lines and small support scars on the base's outer wall at the
  catch line (the catch undersides get supports; they are invisible on a black base).
  Wash thoroughly and dry; a clear case shows any IPA residue or dust inside.

## Fit notes

- The design's inter-part clearances are 0.15-0.30 mm. Resin holds ~+/-0.06 mm on
  33-80 mm features (Form 4 design guide), so fits will be at least as good as PETG,
  probably slightly snugger. The mating gap is 0.2 mm; if the lid is stiff to close,
  it is the snap, not the fit (below).
- Snap closure: catches now hook 0.45 mm with an 18.8 deg closing ramp (was 0.5 mm /
  28 deg) so the clear lid skirt flexes less and closes with less force. It may still
  feel firm. Open with the pry slot.

## Changes vs stl/current (v1.9+J24)

| Part | Change | Why |
|---|---|---|
| joystick | thin flange edge 0.24 mm -> full 0.40 mm (repo's J24-B variant) | the 0.24 mm edge was below resin design guidance and is the weakest feature |
| base + lid | catch hook 0.5 -> 0.45 mm; closing ramp 28 deg -> 18.8 deg; lid pocket 0.55 -> 0.50 deep, skin 0.85 -> 0.90 | resin lid skirt is less forgiving of repeated flex |
| button | byte-identical to tested v1.0 | flexible resin makes it crack-proof as-is |
| everything else | unchanged; outer dims identical (33.04 x 58.6 x 18.67 mm) | |

Validation: repo checks all pass (6 catches, single solids, joystick caught-on-pull and
5.1 deg min tilt clearance, <=45 deg overhangs). Independent measurement: joystick min
thickness 0.400 mm (was 0.240), lid min wall 0.89 mm (was 0.85), all parts watertight.

SHA-256 (see `resin-v1.json`):

- lid.stl 320b1b5c805f3ccd7dca36babd7ce32cd979a75e6a53f065cf1cf1bc0472461f
- base.stl 6340c52aa5e2ed8435e5e54cab5423ce64022424ccf0877b84c6a1c75cece7b7
- joystick.stl b9aef37b9e904ebaeb01d91eab3b81e4484c120a50061f5e768cff38971c0b24
- button.stl c5f2f4a37f8facaa3bd96ad248d94c85154113100936c166ac9365a7ae35d69a (same as PETG)
- full-set.stl 8c6efd319e1bbd4f78b7a59e8390d561b720c0890adfdca03de1376eccfb9a1c

## Reproducing

The variant was built from a copy of the repo at commit `main` (2026-10-23) with two
edits, both in `cad/v1_7_lock.py` (see `cad-changes/`): `HOOK=.45` and
`Z_RAMP_TOP=S.SEAM+3.0`. Build order: `cad/v1_7_lock.py`, `cad/v1_9.py`,
`cad/joystick_j24.py` (exports both A and B; the set uses B), then
`cad/resin_v1_assemble.py` (writes `stl/resin-v1/`). Environment: Python 3.13 venv with
`requirements.txt` (build123d 0.13.0).
