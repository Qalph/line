# LINE FOLLOWER Rev A - READ THIS FIRST

The **CAD** model, laser-cut template, BOM, netlist and preliminary PCB placement are included. `pcb/line_follower_revA.kicad_sch` and `.kicad_pcb` are the starting KiCad files.

**PCB FABRICATION HOLD: Not routed, not ERC/DRC-checked, NOT safe to send to a PCB factory.** Gerber copper/drill output is deliberately **not issued**. Footprints for unknown Mini-360/JST/switch components are placeholders until measured. See `pcb/ROUTING_PENDING.md` and `docs/measurement_gates.csv`.

The generated plate and bracket STL and DXF files are 1:1 mm geometry. **Laser cut the motor and caster holes only after physically measuring hardware**; these patterns are initial estimates. The 1:1 PDF contains 50mm check bar; print with scale 100% (no fit/scale).

## File index

- `cad/line_follower_chassis.scad`: fully parametric source (`part` at top changes export: assembly, plate, sensor_bracket, plate_2d, bracket_2d).
- `cad/chassis_plate.stl`, `cad/qtr_caster_bracket.stl`: separate laser/CAD bodies; STL output is nominal geometry, not a substitute for bracket measurement.
- `cad/chassis_plate.dxf`, `cad/qtr_caster_bracket.dxf`: 2D laser cutting drawings.
- `cad/robot_assembly.stl`, `previews/chassis_assembly.png`: visual reference models including simplified off-the-shelf blocks; the combined STL contains overlapping separate shells, not a printable monolithic robot.
- `docs/chassis_1to1_A4.pdf`: A4 printable 1:1 drill/laser template, 50mm calibration bar.
- `pcb/line_follower_revA.kicad_sch`: generated schematic using embedded custom symbols and named net labels.
- `pcb/line_follower_revA.kicad_pcb`: preliminary 60x65mm module footprint placement, M3 holes, bottom GND zone **not filled**, no tracks.
- `pcb/line_follower_revA.net`: XML KiCad compatible netlist; `pcb/netlist.csv`: every net and pin; `pcb/bom_preliminary.csv`: 21 electronic placements; `docs/mechanical_bom.csv`: all mechanical parts.
- `pcb/LF.pretty` + `pcb/fp-lib-table`: provisional custom footprint library; **measure and revise**.
- `previews/pcb_top_preview.png`, `previews/pcb_bottom_preview.png`: views of **unrouted** placed pads. Also vector SVG.
- `previews/pcb_as_chassis_alternative.png` + SVG: conceptual structural-PCB chassis alternative.
- `docs/engineering_review.md`: complete explicit assumptions, dimensional calculations, pin map, manufacturing instructions, solder/multimeter order and firmware/finish-zone safety analysis.
- `docs/measurement_gates.csv`: measured-parts checklist.
- `docs/electrical_multimeter_steps.csv`: multimeter checklist and required values before ESP is fitted.
- `docs/geometry_checks.json`: CAD envelope and geometric clearance data.

## What Rev B must include

1. Actual ESP DevKit and TB carrier dimensions, Mini-360 pad pattern, selected JST/power switch/fuse footprints.
2. Correct module orientation and clearance testing (ESP antenna, ESP USB plug, ESP socket height, and QTR ribbon cable).
3. Full 2-layer routing / bottom GND fill, motor loop separation, ERC + DRC.
4. Manufacturer-specific Gerbers and NC drill verified in KiCad Gerber viewer.
5. Physical motor/caster/plate mock-up, 3mm sensor height and braking tests.

The full report includes a firmware review **of the provided algorithm summary only**; no code was pasted, so compile-time and runtime code paths have not been inspected.
