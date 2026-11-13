# Line follower competition robot - Engineering design review (Rev A)

**Status: Mechanical reference design complete; preliminary electrical netlist and PCB placement provided; PCB is not routed / NOT FOR FABRICATION.** These files are a basis for measured-footprint Revision B, not permission to order a PCB. Units: millimetres unless otherwise stated.

## A. Provided requirements adopted verbatim

- Strict envelope <= 150 mm high x 200 mm wide x 300 mm long, battery <= 12 V.
- Straight course 12 m race within 13 m total; white 20 mm line on black, two 300 mm lanes, 500 mm start zone and 400 mm entirely white finish zone; must stop **with every protrusion inside**.
- 7.5 cm radius curved category, 15 mm white line, sharp corners; curved mode separate from straight mode.
- ESP-WROOM-32 classic ESP32, DOIT 30-pin DevKit V1, 2 x 15 through-hole sockets, USB on the accessible right (+X) side.
- TB6612FNG dual driver socketed; 2 x N20 6 V 1000 rpm motors with 100 nF terminal capacitors; 2S LiPo 450 mAh; Mini-360 5.00V buck; QTR-8RC at 3.3 V with bypass jumper closed.
- 42 mm diameter wheels, wheel track 90 mm, 17 mm width nominal, axle z =21 mm, body X = +/-34 mm, Y = -25..+40, nose X = +/-15 mm, Y=40..105, nose/sensor Y=95.
- Main board 60 x 65 mm two-layer, x4 mounting hole diameters 3.2 mm at (+/-26, +/-28.5) relative to PCB center, board center Y=+7.5 on chassis.
- Electrically all net names and ESP32 pin assignments agree with the supplied schematic, including D34 divider and 1x11 QTR ribbon S1 left to S8 right.

## B. Added numerical assumptions (these are not guaranteed real part specifications)

| # | Assumption used in source | Why | What to do |
|---|---|---|---|
| B01 | Chassis material is uniformly 3 mm thick | Laser-cut stock | Measure sheet thickness |
| B02 | T-outline corner radius 2.7 mm | Stress reduction | Can change |
| B03 | Axle is z=21 mm, motor envelope 12 mm tall in Z | User axle and common N20 body | Measure N20 motor and mounting orientation |
| B04 | Plate underside z=28 mm | Clears motor upper face z=27 by 1 mm | Measure motor bracket/top clearance |
| B05 | Plate top z=31 mm | 3 mm plate | Recompute if thickness changes |
| B06 | Nominal battery 55 Y x 30 X x 15 Z mm, centered at Y=0 | User estimate | Measure battery + pouch swelling / wiring |
| B07 | PCB underside z=50 mm, plate top-to-PCB 19 mm | Battery top z=46, gap 4 mm | Measure cabling and battery straps |
| B08 | ESP module envelope 51 X x 28 Y mm | Common clone | **Measure exact clone** |
| B09 | ESP socket row spacing 25.4 mm and pin pitch 2.54 mm | Common DOIT 30-pin clone | **Measure center-to-center**, verify pin 1, no blind substitution |
| B10 | ESP header location in module is centered and 15-pin row length 35.56 mm | Preliminary placement | **Measure pin-row longitudinal offset from body and USB** |
| B11 | Driver carrier is Pololu #713 20.3 x 15.2 mm and rows 12.7 mm apart | Official Pololu drawing | **Measure your carrier; clones differ** |
| B12 | Mini-360 footprint board = 17 x11 mm, four hole centers +/-6.7 X, +/-3.2 Y | Placeholder only | **Measure all four XY pad locations/polarity** |
| B13 | Battery 'JST' is 2-pad 2.54 mm JST-pigtail termination, not a mating JST jack | Actual plug series unspecified | **Identify RCY / PH / XH etc, polarity, pitch, discharge vs balance connector** |
| B14 | Inline switch J5 is 2-pin external-switch harness placeholder | Exact switch not supplied | Choose actual mechanically retained switch |
| B15 | 3 A fuse is 1206 SMD placeholder | Exact fuse type unspecified | Choose qualified part with correct I²t, voltage, interrupt and footprint |
| B16 | QTR outer mounting holes 69.85 mm apart | Official Pololu 2.75 inch hole span | Confirm actual screw diameter |
| B17 | QTR outer board is 74.93 x12.7 mm, module total height 3.175 mm | Pololu docs | Measure optical element-to-backside stack and ribbon header |
| B18 | QTR holes at optical Y=95 - 4=91 mm | Optical center-to-hole offset not specified by user | **Measure optical axis to chosen hole center** |
| B19 | Sensor cross-bracket 82 x39 x3 mm, Y=69..108 | Keeps outer QTR support points at +/-34.925 | Adjust for fastener access |
| B20 | Nose-to-bracket two M3 holes x=+/-9, y=91 | User | Verify screw head clearance |
| B21 | Caster centered Y=76 mm (~19 mm behind sensor) | Avoid housing overlap | Measure caster outer housing and QTR intersection |
| B22 | Caster ball is 13 mm; assumed mount-face-to-floor=18 mm | Ball diameter is known, assembly height not known | **Measure real height** |
| B23 | Caster housing diameter 15 mm, mounting holes +/-6 mm (12mm spacing), diameter 2.4mm | Conceptual only | **Measure actual caster holes; don't laser cut yet** |
| B24 | Caster 7 mm shim, bracket underside z=25 mm | 25-18 mm calculation | Make shim after measuring caster |
| B25 | Sensor optical bottom z=3 mm | Pololu optimum distance | Actual z must be calibrated on floor |
| B26 | QTR board top z=6.175 mm and support spacer ~18.825 mm | Uses total module thickness 3.175 mm | **Measure optical face and support faces** |
| B27 | Motor bodies 25x10x12 mm and along X, gearbox faces near X=+/-35 | Placeholder N20 geometry | **Measure motor, hub engagement and shaft protrusion** |
| B28 | Motor bracket holes x=+/-23 and Y=+/-8, 2.2 mm dia | Assumed 16 mm hole spacing | **Do not cut without tracing actual brackets** |
| B29 | Two motor-wire holes at X=+/-15, Y=+18, 6 mm diameter | User desired 6 mm | Confirm wire grommet and strength |
| B30 | Battery velcro slots 8x3.5 mm, X=+/-20, Y=+2 | No actual strap selected | Verify strap width/routing |
| B31 | ESP DevKit USB faces +X, module antenna faces -X | Common module orientation | Verify actual variant antenna keepout |
| B32 | QTR sensor body and PCB assembly are simplified blocks in 3D scene | No vendor STEP available locally | Keep model nonbinding for interference critical parts |
| B33 | Motor current 1.6A stall per motor is **example Pololu 30:1 HP** not asserted for your motors | Driver check scenario | **Confirm exact motor model and motor winding current** |
| B34 | Wheel and hub clearance is estimated from full 17mm tire width; hubs assumed not farther inboard | User width | **Measure hub projection toward motor and inboard interference** |
| B35 | ESP socket header height roughly 8-11mm, module hardware stack up to ~68mm Z | Envelope estimate | Measure if racing under low obstacles |
| B36 | PCB copper is not routed and no Gerbers are approved | Fabrication safety | Complete PCB ERC/DRC and update measured footprints |
| B37 | Conductive loads on ESP 3V3 include QTR roughly 100mA | Pololu rated sensor draw | Measure 3V3 under Wi-Fi TX and high motor current |
| B38 | Regenerative/braking supply spikes may occur | Driver/motor physics | Test 16V cap headroom on oscilloscope if available |
| B39 | Approximate mass distribution: plate 12g, bracket 6g, populated board 32g, LiPo 27g, motors 19g pair, wheels 16g pair, caster 4g, QTR 3g | First-order COM model | **Weigh actual parts and recalculate** |

## C. Mechanical clearance calculations

- Left/right wheel centers X = ±45. Wheel inner face = 45 -17/2 = 36.5. Chassis outer face =34. Nominal minimum inboard lateral **clearance = 2.5 mm**, which exceeds the 2 mm specified, **without hub/shaft protrusion**.
- Overall wheel-tip-to-wheel-tip width = 90 +17=**107 mm**, under 200 mm. Sensor bracket 82 mm wide, so wheels determine max width.
- Farthest modeled rearward item is battery at Y=-27.5; bracket front is Y=+108. Overall **length = 135.5 mm**, under 300 mm. Ensure motor wires/power switch do not project farther.
- Axle z=21mm => wheel top z=42mm; PCB underside z=50mm => 8mm above wheel tops. Populated board approx 65-70mm height, under 150mm (subject to measured headers, wires and connector heights).
- QTR optical face z=3mm by design. Plate underside z=28; sensor bracket thickness3 => bracket underside 25. QTR optical height3 + assumed PCB stack3.175 => top of QTR board6.175; **support spacer 25-6.175 = 18.825mm**. This is not a universal standoff length, only a stacking calculation.
- Caster bracket underside z=25. If caster assembly from fixing face to floor is 18mm, required shim **7 mm**; adjust to maintain level and prevent rocking.
- The wheels are directly on N20 output shafts; wheel hub thickness/axial engagement not fully represented in the assembly preview.
- Approximate COM Y = **+14 mm** from axle with assumed masses B39. It is ahead of axle and behind caster, but must be reverified by weighing parts and balance testing.

## D. Electric pin/net review

**Battery and regulators:** JST-pigtail pads J2 BAT+ -> J5 external power-switch contacts -> F1 3A fuse -> VBAT. Battery negative GND. VBAT to TB VM, 470uF/16V cap to GND at VM and Mini360 IN+. Mini360 nominal 5.00V -> ESP32 VIN and 22uF to GND. ESP DevKit 3V3 -> TB VCC, QTR VCC and 100nF ceramic to GND. 100nF at each N20 motor is soldered on motor terminals, not on controller PCB.

**Voltage divider:** VBAT -> R1 100k -> BAT_SENSE -> R2 33k -> GND, BAT_SENSE -> U1 D34. Optional C4 100nF BAT_SENSE-GND. At full pack, VADC =8.4 ×33/133 =**2.084 V**. Use ADC1 11dB attenuation (or calibrated equivalent) and verify accuracy across battery voltage; ADC nonlinearity is real. 100k/33k divider loads battery ~63uA at 8.4V.

**TB6612 control:** AIN1 D22, AIN2 D21, PWMA D19, BIN1 D18, BIN2 TX2/GPIO17, PWMB RX2/GPIO16, STBY GPIO5 via solder jumper JP1 1-2, optional JP1 2-3 tie to 3V3. STBY has R5 100k pull-down to GND. All driver GND pins to GND, motor L on AO1/AO2 and R on BO1/BO2. To truly ensure no run-on at boot, evaluate GPIO5 strapping / driver input behavior and improve the standby circuit as needed. **Do not bridge both sides of JP1 simultaneously.**

**QTR cable J1** exactly: 1=3V3, 2=GND, 3=LEDON/GPIO23, 4=S1/GPIO32, 5=S2/GPIO33, 6=S3/GPIO25, 7=S4/GPIO26, 8=S5/GPIO27, 9=S6/GPIO14, 10=S7/GPIO13, 11=S8/GPIO4. QTR 3.3V bypass is solder-closed. Never operate 3.3V bypass with 5V supply. Make the physical cable keyed and label S1 robot left.

**Controls:** D35 external 10k to3V3 and optional START switch to GND. VN/GPIO39 external 10k to3V3 and optional MODE switch to GND. Internal GPIO35/39 pull-ups are absent. DevKit D2 LED is not copied onto main PCB. Do not connect GPIO6-11, 0, 12, 15, TX0 or RX0.

**ESP32 strap risk:** GPIO5 is a strapping input sampled on boot with internal weak pull-up, as is GPIO4 sampled as strap (GPIO4 is QTR_S8). The external STBY pull-down may alter GPIO5 strap and QTR wiring might alter GPIO4 strap. Test repeated cold boots, brownout resets and uploads, with sensor on black vs white and switches in each position. For Rev B, swapping STBY to a non-strapping GPIO (e.g. D23) and LEDON to GPIO5 may be safer, but changes the specified pin map and firmware.

**TB6612 electrical limit:** A Pololu #713 carrier is rated about **1A/channel continuous** and higher pulsed current under specified duty/time limits. 6V HP 1000RPM N20 motors can have stall currents on the order of 1.6A depending exact model. Expect the two motors' combined startup current to challenge a 3A fuse and 450mAh battery; use exact measured current curves, not only nominal ratings.

## E. Two-layer PCB placement and routing instructions

The enclosed KiCad schematic, XML netlist, CSV pad map and `.kicad_pcb` are preliminary. The board file contains correct board dimensions and four M3 holes, populated connector/socket/other pad representations, silkscreen outlines and a **defined but unfilled bottom GND zone**. It contains **zero signal tracks**; neither PCB ERC nor DRC has been run because KiCad is unavailable here. No working Gerbers are supplied.

- Board rectangle X=-30..+30, local Y=-32.5..+32.5; +Y is the sensor/front edge. PCB chassis position center Y=+7.5, four M3 at (±26,-21) and (±26,+36) chassis XY.
- FRONT: J1 QTR 1x11 at Y=+28. MIDDLE: U1 horizontally across board, centered Y=+8.9; USB towards +X. REAR: U2 TB carrier centered Y=-23, U3 buck at (-20,-15.5), 470uF cap and fuse on right-rear; battery wire harness and optional switches on right-rear/left edge.
- PCB target: F/B copper 1oz recommended, FR4 1.6mm, ~0.20mm clearance, min 0.25/0.30mm logic tracks, min 1.0mm battery/driver/motor/GND tracks. For 1A continuous and startup spikes, increase to 1.5-2mm where feasible and add pours; account for thermal rise / board stackup.
- Route VBAT to C1 and U2 VM with short, wide F.Cu traces. Keep driver motor traces away from QTR header/signal fanout and from the battery divider ADC trace. Split physical **current paths**, not the low-impedance GND plane: bottom GND plane continuous, local driver decoupling close and sensor return routed quietly.
- Tie all grounds to one common board GND near the battery input/power distribution; avoid narrow ground necks. Keep high di/dt battery/driver current loops away from the ESP antenna and sensor returns.
- Observe WROOM antenna keepout near the end opposite USB. Avoid copper and metal directly beneath antenna in the final design, and test antenna Wi-Fi performance after mounting.
- Keep silk pin1 markings, + and - electrolytic pads, QTR S1-to-S8, and MOTOR L/R. Verify module swaps via headers under physical chassis constraints.
- With near-full mechanical packing, a single-sided hand-etched 60x65mm board would need many jumper wires and would be fragile for pulsed 1-3A motor currents. **Not recommended**. A larger PCB and wired modules can make single-sided possible but less reliable.

## F. Pre-assembly soldering and multimeter procedure

1. **Print and verify mechanical fit before soldering.** Print PDF at 100%, measure red 50mm calibration bar; dry-fit N20 brackets, caster and QTR against paper. Do not cut guessed motor/caster hole patterns without measuring hardware.
2. **Inspect bare PCB (once routed/fabricated).** Confirm no plating burrs, all pin1 legends, M3 insulation, and no copper short to holes. Continuity from VBAT to GND should be open/high resistance with no components installed.
3. **Install low-profile passives:** R1=100k; R2=33k; R3/R4=10k; R5=100k; C2=22uF; C3=100nF; optional C4=100nF; F1 qualified fuse; JP1 default **GPIO5->STBY**, not 3V3. Verify R1+R2 resistance ~133k from VBAT to GND and divider tap to ground 33k (without other power loads, tolerance expected).
4. **Fit battery/power/switch connections and Mini360 ONLY, no ESP/TB/QTR.** Confirm polarity with battery unplugged. With a current-limited bench supply at 7.4V, turn on and adjust Mini360 **with a multimeter** to 5.00V OUT+ to GND. Do not adjust it with ESP connected.
5. **Confirm 5V rail.** At U1 VIN socket, expected 5.0V ± buck tolerance. Verify no 5V on the U1 3V3 socket. With ESP still absent, 3V3 is unpowered (unless externally supplied for a bench test). Check C1 + to GND positive, − to GND.
6. **Install ESP socket and DevKit only, keep driver + sensor unplugged.** With battery and USB power not simultaneously applied unless clone's power path is confirmed, measure U1 3V3 to GND about 3.3V. Check reset/reboot, serial and Wi-Fi at 5V input, monitor regulator temperature. Verify U1 D34 reads battery divider ~2.08V at 8.4V VBAT and uses ADC1 attenuation/calibration.
7. **Install sensor only.** Verify J1 3V3, GND and LEDON; close QTR 3V3 bypass, **never** use 5V. Confirm S1 left and S8 right, white/black decay times on all eight inputs. Ensure no boot issue from GPIO4.
8. **Install TB module with motors disconnected.** Confirm 3V3 at VCC, VBAT at VM. On reset STBY should read LOW; after firmware enables it, HIGH. Confirm A/B PWM pins safe until start. Test motor output polarity with a scope or brief DMM duty checks before attaching motors.
9. **Connect motors, wheels lifted.** Very low PWM first, monitor battery current, compare left/right direction, inspect 100nF motor suppression caps. Verify no ESP brownouts or J2 heating.
10. **Low-speed floor test then brake calibration.** Ramp up speed, repeatedly measure travel over known distances and 0.4m finish-zone stop locations. Log actual loop interval, black/white RC delays, battery under load, measured launch and braking deceleration, drift, and end-stop coordinates. Test with full and depleted batteries, bumps/slopes, and cold resets.

## G. Straight-race finish stop logic review

### A guarded 400mm finish zone

Because the actual rearward battery edge is Y=-27.5 and bracket forward edge Y=+108, sensor is +95, the sensor-to-rear distance is **122.5mm** and sensor-to-front distance is **13mm**. If optical sensor first encounters finish zone at s=0, whole body is inside only when sensor reference coordinate s is in [122.5, 387] mm. Add 50 mm buffer at both ends: target stop sensor coordinate **[172.5, 337] mm**. If `allWhiteConfirmed` after s≈60mm of white, remaining protected braking displacement must be in **[112.5, 277]mm**.

At v=1.3m/s, ideal d=v²/(2a): 3m/s² =>282mm (5mm beyond 50mm-buffer upper limit); 4m/s² =>211mm; 5m/s² =>169mm; 6m/s² =>141mm. Thus a 4-6 m/s² **measured, reproducible** brake profile is a workable starting region; not a guarantee on bumps/slopes. At 2.3m/s, d=661mm even at a=4m/s², so entering the zone at full speed is not acceptable.

### Required race states

`IDLE` -> `LAUNCH_RAMP` -> `FAST_TRACK` -> `PRE_FINISH_SLOW` -> `FINISH_CANDIDATE` -> `FINAL_BRAKE` -> `HOLD_BRAKE` -> `STOPPED`.

- During `FAST_TRACK`, track line using PD feedback and record verified control-loop timing; continuously integrate a conservative distance estimate from calibrated measured actual velocities (and uncertainty) rather than commanded PWM only.
- Start pre-finish slowdown sufficiently early for worst-case **negative odometry bias**. For instance, slow to <=1.2-1.3m/s within the last 1.5-2.0m **estimated** distance, calibrate this threshold from >30 measured runs, and don't accelerate again just because all-white detection has not yet occurred.
- Require every QTR channel reflectance to be confidently white for a robust run of samples; white 20mm line cannot cover 66.675mm sensor span when perpendicular (even though yaw and track artifacts need testing). Use temporal filtering, ambient-compensated thresholding, and a minimum time/estimated distance before declaring finish.
- When confirmed, **don't switch off motors or throw TB STBY low**: that usually coasts. Command controlled deceleration while still making modest steering corrections, then engage TB motor short-brake and hold until fully stationary.
- Quantify distance-to-rest online using measured v and a ranges. A post-confirmation brake plan should land sensor at ~245-285mm into zone, keeping both ends in the white region. Avoid driving more than 337mm or stopping short of 172.5mm sensor coordinate (for 50mm margins).
- At least 10 low/high voltage and slope runs need to verify worst-case stopping displacement after finish confirmation. Reject the setup if an entire-body stop is not achieved for those tests.
- If `allWhite` flickers, do not return to full-speed: remain slow and use line tracking; a true finish is wide and durable. If line completely disappears, reduce speed and recover rather than accelerating on last known heading.
- Use a monotonic clock and `dt` for derivative: filter slope and cap wheel voltage. State whether `kd=0.08` applies to `error[k]-error[k-1]` per tick or `(error[k]-error[k-1])/dt` per second. These coefficients differ by ~1000x at 1kHz; retune after defining actual units.

### Lane keeping and curved-track checks

- 300mm lane with 107mm wheel-tip width gives centered robot 96.5mm geometric lateral clearance per side. Allow an extra 30mm margin for yaw, line deviations, bump deflections and body protrusions: keep centerline error under about 66.5mm. The 8 QTR sensors span 7*9.525=66.675mm; line detection may be lost before the robot reaches its lane edge.
- Max speed 2.3m/s on a 75mm radius curve requires centripetal acceleration 2.3²/0.075=70.5m/s² (~7.2g), impossible for conventional small-wheel traction. At friction mu~0.6 and g=9.81, a nominal theoretical turn speed is sqrt(mu*g*0.075)~0.66m/s before transient and margin; start curved mode at ~0.4-0.6m/s.
- QTR `readLine()` pulse timeouts up to 1000us can consume ~1ms each, **before Wi-Fi, Serial, and PD computation**. Measure true end-to-end loop period, e.g. with GPIO oscilloscope toggle, not an assumed 1kHz.
- Motor model `mmPerSecPerVolt=310` at 7.4V implies 2.29m/s but rated 6V no-load predicts 2.20m/s; that model cannot be presumed accurate at load, transients and battery sag. Fit steady-state speed vs voltage using 3-5m measured runs and estimate uncertainty and delay; use overground tape/video if no encoders.
- A voltage cap of 7.4V for motors rated 6V is an aggressive short-duration use case; test temperature and current. At VBAT<7.4, a 7.4V voltage command is physically unattainable (PWM 100% saturates), so account for saturation and reduced launch/brake control authority.
- The nominal 45 V/s launch ramp reaches 7.4V in 0.164s. This does not guarantee an acceleration force profile independent of battery, traction and load.

## H. PCB-as-chassis alternative (same T shape)

Reuse T plate outline as a **thicker 2.0-2.4mm FR4** PCB outline; mount N20 brackets from underside (insulating washers), and carry battery over axle on top. Keep QTR bar on separate lateral 82mm cross-bracket attached at Y=91 because 30mm nose is narrower than its mounting span. Motor traces are short but carry vibration/shock current loops. Reinforce/avoid copper under bracket holes, use non-plated M3 mounting holes and protective battery pad, strain relief and antenna clearances.

**Pros:** lighter system from eliminating wood/acrylic plate and 4-PCB standoffs, compact wiring, less assembly complexity. **Cons:** larger more expensive irregular PCB, higher prototype rework cost, risk of FR4 flex/cracks on bumps, copper damage near motors/screws and more motor EMI coupling into sensor traces. Easier to prototype first with the separate chassis and smaller controller PCB, then integrate once wiring and speed control are validated.

## I. References used for non-user facts

- Pololu QTR-8RC #961 and user guide: https://www.pololu.com/product/961 and https://www.pololu.com/docs/0J12/all
- Pololu TB6612 #713 specifications and drawing: https://www.pololu.com/product/713/specs and https://www.pololu.com/file/0J1724/tb6612fng-dual-motor-driver-carrier-dimensions.pdf
- ESP32 boot strapping: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/schematic-checklist.html and https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html
- Typical 30-pin DOIT pinout: https://openlabbench.gwark.dev/pinouts/esp32-devkit-v1/ - match to physical board before purchase.

