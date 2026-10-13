**To print a case, use [`current/`](current/README.md). Nothing else here.**

**"Buttons" means `button.stl`** (the four front caps by the screen). The RESET button is a different part, only for the Atomic Wedgie. Don't print it unless someone asks for the Atomic Wedgie or the RESET button by name.

Every other file and folder in `stl/` is an old test, kept as the design
record. `print/` and the loose STLs in this folder are the first prototype
(2026-09-25), not the current case.

Old prototype notes below. `stl/current/` is built by `cad/current.py`;
`print/` and the loose STLs by `cad/build.py`. Never hand-edit meshes. MIT, like the original source.

`print/` holds base, lid, four button caps, and default joystick cap in print
orientation. Separate button solids on the bed. `fit_samples/` holds alternate
joystick caps named for socket width; try largest first without forcing.
Top-level STL/STEP uses assembled positions and includes illustrative hardware.
`manifest.json` records source/output SHA-256 hashes and tool version.
R4 is an unprinted prototype; print/assembly details in REPORT.md.
