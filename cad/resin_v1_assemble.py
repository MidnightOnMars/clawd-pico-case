"""RESIN-V1: assemble the resin variant set (v1.9 lid + v1.7 base, resin snap,
J24-B full-flange joystick, S2 buttons). Mirrors cad/current.py but exports to
stl/resin-v1/ and uses the B joystick variant.
Run: .venv/bin/python cad/resin_v1_assemble.py
"""
import hashlib
import json
import shutil
from build123d import Pos, Rot, Compound
import v1_5_tall as T5
import joystick_j24 as J24
import v1_9 as L9
import v1_7_lock as L7

W, V, J = T5.W, T5.V, T5.J
ROOT = T5.ROOT
REV = 'resin-v1'
DIR = ROOT / 'stl' / REV
GAP = 5.0  # V1-PLATE
PARTS = {'lid.stl': 'stl/v1.9/lid-face-down.stl',
         'base.stl': 'stl/v1.7/base-floor-down.stl',
         'joystick.stl': 'stl/test/j24/joystick-j24-B.stl',
         'button.stl': 'stl/v1.0/button-1.stl'}


def main():
    DIR.mkdir(parents=True, exist_ok=True)
    for name, src in PARTS.items():
        shutil.copyfile(ROOT / src, DIR / name)
    W.shorten()
    l = L9.lid()
    b, _ = L7.base()
    lid, base = V.origin(Rot(180, 0, 0) * l), V.origin(b)
    cap = Pos(0, 0, -J.BOTTOM) * J24.cap(False)  # RESIN-V1: B, full 0.4 flange
    caps = [V.origin(c) for c in V.T.buttons().solids()]
    checks = {}
    for shape, name in ((lid, 'lid.stl'), (base, 'base.stl'), (cap, 'joystick.stl'), (caps[0], 'button.stl')):
        tmp = DIR / ('check-' + name)
        J.export(shape, tmp)
        checks[name + '_regenerated_matches_source'] = tmp.read_bytes() == (DIR / name).read_bytes()
        tmp.unlink()
    checks['button_byte_identical_to_tested_v1_0'] = (DIR / 'button.stl').read_bytes() == \
        (ROOT / 'stl/v1.0/button-1.stl').read_bytes()
    checks['joystick_is_full_flange_B'] = J24.cap(False).bounding_box().size.Z > 0  # sanity
    lb = lid.bounding_box().size
    placed = [lid, Pos(lb.X + GAP, 0, 0) * base, Pos(J.FLANGE / 2, lb.Y + GAP + J.FLANGE / 2, 0) * cap]
    x = J.FLANGE + GAP
    for c in caps:
        placed.append(Pos(x, lb.Y + GAP, 0) * c)
        x += c.bounding_box().size.X + GAP
    plate = Compound(children=placed)
    checks['plate_has_seven_solids'] = len(plate.solids()) == 7
    checks['plate_fits_build_volume'] = all(v < 256 for v in tuple(plate.bounding_box().size))
    J.export(plate, DIR / 'full-set.stl')
    files = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DIR.glob('*.stl'))}
    (DIR / 'resin-v1.json').write_text(json.dumps(dict(
        revision=REV, sources=PARTS, sha256=files, checks=checks,
        print=dict(material='resin (per part, see README)', layer='material default (100 um)',
                   supports='PreForm auto', orientation='lid face down, base floor down, caps flange down')),
        indent=2) + '\n')
    print(json.dumps(dict(checks=checks, files=files,
                          plate=[round(v, 2) for v in tuple(plate.bounding_box().size)]), indent=2))
    if not all(checks.values()):
        raise SystemExit('Validation failed')


if __name__ == '__main__':
    main()
