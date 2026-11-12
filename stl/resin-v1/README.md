# resin-v1 print sheet (Formlabs SLA)

Resin variant of the repo's `v1.9+J24` case (Austin's tested PETG design), generated
from the build123d source. **CAD-validated, not physically tested.** Provenance and
change log: [`FORK-NOTES.md`](../../FORK-NOTES.md).

**Treat the first print as a fit test.** Every fit in this case was tuned on an FDM
printer in PETG, and some of them depend on the process. They will not come out the
same on an SLA printer. The print list below carries the spares and variants that
cover them, and [First fit](#first-fit) says what to check and what to do when a fit
is off.

## One case

| File | Per case | Colour | Resin |
|---|---|---|---|
| `lid.stl` | 1 | Clear | Alpha Clear Resin |
| `base.stl` | 1 | Clear | Alpha Clear Resin |
| `joystick-j24-a.stl` or `joystick.stl` | 1 | Dark grey | Tough 2000 Resin V2 |
| `button.stl` | 4 | Black | Flexible 80A Resin V2 |

The two joystick files are the same cap with different flanges. `joystick-j24-a.stl`
is J24-A, the cap Austin chose in PETG: its flange thins to 0.24 mm over the outer
1 mm. `joystick.stl` is J24-B: 0.40 mm throughout. Austin printed both on 2026-10-02
and found B "a little bit too clunky" ([log](../../prints/2026-10-02-joystick-j24.md)).
B is in this set because a 0.24 mm edge is close to the 0.2 mm minimum wall in
Formlabs' design guide. Print both and choose by feel.

## Print list for the first run

Three prints, three resins, one Form Studio 1.

| Print | Resin | File | Copies |
|---|---|---|---|
| 1 | Alpha Clear Resin | `lid.stl` | 2 |
| 1 | Alpha Clear Resin | `base.stl` | 2 |
| 2 | Tough 2000 Resin V2 | `joystick-j24-a.stl` | 3: one each at 100 %, 98.5 % and 97 % scale |
| 2 | Tough 2000 Resin V2 | `joystick.stl` | 3: one each at 100 %, 98.5 % and 97 % scale |
| 2 | Tough 2000 Resin V2 | `button.stl` | 4, rigid spares |
| 3 | Flexible 80A Resin V2 | `button.stl` | 6: four plus two spare |

Why the extras:

- **Second lid and base.** The clear lid is the part most likely to mark or crack on
  its first close. A second set also lets one lid be fitted as printed and the other
  with its ribs eased (see First fit).
- **Joystick scale ladder.** The cap grips a 1.86 mm square stem with a 1.90 mm
  socket. That worked in PETG, where small holes print tight. On an SLA printer the
  socket may come out nearer its drawn size and sit loose. Upstream's
  [PETG joystick sheet](https://github.com/clawdbotatg/clawd-pico-case/blob/main/stl/current/JOYSTICK-PRINT.md)
  (2026-11-10) shows how sensitive this fit is: there the socket's size depends on
  the first-layer settings, six or more caps are printed, and one is picked by fit
  on the stem. Scaling the whole cap in
  PreForm (Size, Scale) gives 1.90, 1.87 and 1.84 mm sockets. Do not go below 97 %:
  the 3.1 mm socket mouth has to clear a 2.94 mm collar at the base of the stem, and
  at 97 % only 0.03 mm per side is left. Tell the caps apart by flange diameter:
  10.0, 9.85 and 9.7 mm. If the plate has room, print two of each.
- **Rigid spare buttons.** The lid holds each button by a lip of 0.08 mm along each
  long side and 0.20 mm at each end. That is enough for a rigid cap. A rubber cap may
  pull out.

`full-set.stl` is all seven parts on one plate in one colour, with the J24-B joystick,
for a single rigid resin. Print it or the list above, not both. Its joystick cap sits
flange down, so do not print the plate directly on the build platform (see Print
setup).

All three resins are listed by Formlabs for the Form Studio 1. Alpha Clear is Form
Studio 1 only; on a Form 4 series use Clear Resin V5 for the clear parts. Formlabs
lists Tough 2000 V2 on the Form Studio 1 with the Resin Tank Pro. The STLs are
printer-agnostic geometry: a Form 2 or Form 3 needs the equivalent older resins.

## Print setup

Orientation and supports are the operator's call, with one exception: **do not print
the joystick caps flange down directly on the build platform.** The reason is in the
table further down. The STLs are exported the way the FDM version prints (lid face
down, base floor down, caps flange down). That is the export orientation, not a
requirement. Layer height: the material default (Alpha Clear: 100 um).

What each part needs:

| Part | Functional surfaces: protect these first | Show surfaces |
|---|---|---|
| Lid | Inside of the skirt, the last 3 mm before the rim: six snap pockets and twelve crush ribs. The rim. The four button holes (4.7 x 5.9) and the joystick hole (8.0). Four small pads in the inside corners that sit just above the LCD board. | Outer top face and bezel. |
| Base | Six catches on the outside of the tongue, each with a flat underside 0.65 mm proud that hooks the lid. The tongue's outer face. The shoulder the lid rim lands on. The tops of the two rails the LCD board rests on. The USB opening. | Outer walls and floor. |
| Joystick cap | The socket in the underside: a 3.1 mm round mouth, then a 1.90 mm square. The flange: 0.40 mm thick, and on J24-A the outer 1 mm is 0.24 mm. | The ball. |
| Button | Flange 0.8 mm thick, post 4.2 x 5.4. | Post top. |

Function comes first. A touchpoint on a plain outer wall sands and polishes out. One
in a pocket, on a catch underside or in the joystick socket does not.

Three things to weigh before printing a part directly on the platform:

- **Early layer merging.** Formlabs says parts printed
  [directly on the platform](https://formlabs.com/support/Printing-directly-on-the-build-platform-in-PreForm/)
  come out about 0.1 mm short in Z, and that PreForm merges the first 0.75 mm of
  such a print into one combined shape. Merging the same 0.75 mm of each STL as
  exported gives the table below. It is computed from the meshes (2026-11-12), not
  test-printed: check it in PreForm's layer view.

  | Part as exported | First 0.75 mm as drawn | After merging |
  |---|---|---|
  | Joystick cap, flange down | Flange 0.40 mm thick (J24-A: 0.24 mm at the rim). Socket mouth 3.10 mm for 0.35 mm, then a funnel down to the square. | Flange a 0.75 mm slab, the same on both caps. The mouth is reshaped too: taken as a union of the solid it closes to about 2.3 mm, less than the 2.94 mm collar. |
  | Lid, face down | Skin 0.64 mm over the button pocket and 0.70 mm over the joystick pocket. Rounded outer edge. Bevelled window and joystick hole. | Skin 0.75 mm: 0.11 mm less room over the button flanges and 0.05 mm less over the joystick flange. Edge and bevels squared off for the first 0.75 mm. |
  | Base, floor down | Plain floor, constant section for 1.2 mm. | No change. |
  | Button, flange down | Flange 0.80 mm, constant section. | No change. |

  So the joystick caps go on supports, clear of the platform, whichever way up. Trim
  every support nub on a cap's flange flush: upstream found that anything left on
  the flange keeps it from sitting flat under the lid. The base and the buttons are
  not changed by the merge. The lid is a trade: on the
  platform it gets a frosted face, a squared edge and slightly shallower pockets; on
  supports it gets touchpoints.
- **The lid and base are five-sided shells.** Face down or floor down on the platform,
  the open end faces the tank and the openings in the face (window, button and
  joystick holes, the 4 mm hole in the base floor) are closed off by the platform.
  Formlabs' [orientation guide](https://formlabs.com/support/Model-Orientation/) warns
  that hollow shapes can act as a suction cup.
- **XY at the platform.** The same guide says the bottom layers of a part printed on
  the platform are often oversized in XY.

## Post-processing

Fit nothing until every part is washed, dry and post-cured.

- Alpha Clear: wash in >= 90% IPA or Formlabs Resin Washing Solution, air dry at
  least 30 min. Post-cure with the **default** Alpha schedule (5 min in Form Studio
  Wash+Cure). Formlabs' data sheet gives 32 % elongation at break for the default
  cure against 21 % for the max-strength cure, and the snap needs the give.
- Tough 2000 V2: wash in IPA (Formlabs does not recommend Resin Washing Solution for
  the Tough resins; it can leave them tacky). Air dry at least 10 min. Post-cure
  required; use the material preset.
- Flexible 80A V2: wash in IPA. Formlabs' support articles list this resin as not
  compatible with Resin Washing Solution, although the product page mentions it.
  Post-cure required; the support article describes two steps, first submerged in
  water, then in air. Use the material preset.
- Clear lid and base: any face printed against the platform comes out frosted, and
  support marks show in a clear part. Functional as-is; wet-sand and polish for a
  glassier look. Wash thoroughly and dry; a clear case shows any IPA residue or dust
  inside.

## First fit

Bring the LCD board, the Pico and a USB-C cable, plus a sharp blade, a flat needle
file and calipers. Start with the empty shells, before any electronics go in.

1. **Close one lid on one base.** Start the rim square and press evenly. It should
   seat with firm thumb pressure, click at the catches, and sit with the rim down on
   the base all the way round. Do not force it.
2. **If it stops short or needs force, it is the crush ribs.** Twelve ribs inside the
   lid skirt (four per long side, two per end), 0.6 mm wide, stand 0.35 mm off the
   wall and press 0.15 mm into the base tongue. Austin added them in PETG to stop
   rattle, where they give. In resin they may not. Take about 0.1 mm off each rib tip
   with a flat needle file or a blade and try again. With two lids, keep one as
   printed for comparison.
3. **If it seats but does not click, or sits proud at the seam, it is the catches.**
   They have 0.04 mm of free play by design, less than one layer. Trim the flat
   underside of each of the six catches with a blade, a little at a time.
4. **Look at the skirt.** After closing, and again after opening, check the clear
   skirt around the six pockets for white marks or cracks. The skirt is 0.9 mm thick
   there.
5. **Open it at the pry slot** on the long side of the base, with a thumbnail or a
   thin flat tool. The catches do not release by pulling. Ease it; do not lever hard
   against the clear rim.
6. **Now with the boards in.** The LCD board rests on the two base rails and sits
   0.05 mm under four small pads in the lid's inside corners, with 0.14 mm of play
   end to end. If the case closed empty but will not seat or click with the boards
   in, the board is pinched: trim the four pads with a blade, or ease the inside of
   the lid's end walls with the file, a little at a time.
7. **Plug in the cable.** The opening leaves 0.10 mm under the connector, and the
   recess around it was sized for one cable. File the opening if the plug will not
   seat.
8. **Choose the joystick cap on the bare stick.** The right one pushes on by hand,
   sits firm with no wobble, and stays on with the board upside down. Start with
   100 %. Then try it in the closed case: a direction push must not also click the
   centre. Expect J24-B to touch the lid sooner than J24-A.
9. **Buttons.** Fit the four rubber caps. If one pulls out through the lid or the
   click feels vague, use the rigid spares. If the buttons sit pressed and will not
   click freely, the pocket above them is too shallow (a lid printed face down on the
   platform loses 0.11 mm there): take about 0.1 mm off the flange face of the rigid
   spares on fine paper and use those.

Then assemble as in [`assembly/ASSEMBLY.md`](../../assembly/ASSEMBLY.md), and record
what fit in [`prints/2026-11-12-resin-v1-first-article.md`](../../prints/2026-11-12-resin-v1-first-article.md).

## Fit notes

- Most clearances in the design are 0.15 to 0.30 mm and the lid-to-base gap is
  0.20 mm. The tight ones are the crush ribs (0.15 mm interference), the joystick
  socket (0.02 mm per side on the stem), the catch free play (0.04 mm), the pads over
  the LCD board (0.05 mm), the board's end play (0.14 mm) and the gap under the USB
  connector (0.10 mm). All of them were settled by trial on an FDM printer.
- Form 4 generation dimensional tolerance is +-0.2% (lower limit +-0.06 mm) on 31-80 mm
  features, so across the case's 58.6 mm length expect about +-0.12 mm (Form 4 design
  guide, Grey V5, XY features). Not checked for the Form Studio 1.
- Snap closure: the catches hook 0.45 mm with an 18.8 deg closing ramp (PETG: 0.5 mm,
  28 deg), a longer and gentler ramp so the clear skirt closes with less force.
  Upstream noted on 2026-11-10 that PETG cases get easy to open after a while, and is
  testing a base that holds harder: a 0.54 mm hook, wider catches and a stiffer
  tongue. This variant went the other way, so watch how firmly the resin case stays
  shut. If it is too weak there are two fixes. Raising `HOOK` in `cad/v1_7_lock.py`
  deepens the lid pockets with it, so the lid and the base are both reprinted.
  Stiffening the tongue, which upstream calls the bigger lever, changes the base
  only.
- Upstream bases do not drop into this lid. Its pockets are 0.50 mm deep (PETG lids:
  0.55 mm), so upstream's 0.5 mm hooks have no spare in them, and the 0.54 mm hook
  of the Wedgie Plus test base is 0.04 mm too deep.
- Alpha Clear heat deflection is 57 C (default cure): keep the case out of hot cars
  and prolonged direct sun. Indoor and handheld use is fine.
- Board: the base is the v1.7 base, for the USB-C or micro-USB Pico. The RP2040-Plus
  needs a different base: upstream's Atomic Wedgie base (with a battery) or its
  Wedgie Plus test base (no battery, 2026-11-10). Neither has a resin version here.

## Files

SHA-256 of every STL in this directory: `resin-v1.json` (same format as
`stl/current/current.json`). `joystick-j24-a.stl` is byte-identical to
`stl/current/joystick.stl`, the cap Austin tested. `button.stl` is byte-identical to
the tested v1.0 button.

## Rebuild

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python cad/v1_7_lock.py    # base + lid, validated
.venv/bin/python cad/v1_9.py         # v1.9 lid + joystick reference
.venv/bin/python cad/joystick_j24.py # A and B joysticks, validated
.venv/bin/python cad/resin_v1_assemble.py  # writes stl/resin-v1/
```

The first two scripts rewrite `stl/v1.7`, `stl/v1.9` and `renders/` with the resin
snap constants. Those folders hold Austin's tested PETG files: restore them with
`git checkout -- stl/v1.7 stl/v1.9 renders` after a rebuild, and do not commit them.
