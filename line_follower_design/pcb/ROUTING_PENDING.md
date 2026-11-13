# Preliminary PCB, REV A - DO NOT ORDER

These KiCad source files are an electrical pin map and preliminary physical placement, **not a routed/manufacturable board**. The `.kicad_pcb` contains 0 copper tracks; the bottom-layer GND copper pour is defined but not filled.

**No Gerbers/drill manufacturing package is provided intentionally:** generating them for a board with unmapped module clones, unverified JST polarity, missing routing and no Electrical Rules Check (ERC) or Design Rules Check (DRC) would create a dangerous false ready-to-fabricate signal. Do not manufacture until all items below are resolved.

1. Verify ESP32 30-pin outer dimensions, exact 25.4mm header-row spacing, x-offset of pin 1, USB clearance, module antenna free space.
2. Measure actual Mini-360 four-hole XY spacing and orientation, and board side component keepout.
3. Choose exact mating battery JST type (RCY, PH, XH, etc), pitch, pin orientation and wire polarity. The current J2 is a PTH pad **for a JST pigtail**, not a certified mating footprint.
4. Confirm TB6612 Pololu #713 versus other carrier; pin order and board outline.
5. Choose rated 3A fuse (time-current curve, package), power switch and side controls, and suitable motor wire connectors.
6. Decide whether QTR header requires shrouded / keyed connector and precise ribbon orientation.
7. Route every signal and power track, clear 0.2mm minimum copper spacing, wider battery/VM/motor returns, add vias and refill B.Cu GND.
8. Run KiCad ERC, DRC, 3D/courtyard collision review; board fab outputs only after checks are clean.

Traces required: >=1.0mm on battery/VM/motor GND; signal 0.25-0.30mm. Net names and pin maps are documented in `netlist.csv`.
