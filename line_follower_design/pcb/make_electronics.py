"""Line Follower REV A preliminary KiCad 6/7 source generator.
Genuine connectivity, editable schematic, explicit 60x65 footprint placement.
DO NOT FABRICATE before measuring module footprints and PCB DRC/routing.
"""
import os,csv,math,uuid,html,json,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PRJ='line_follower_revA'
PINS={}; VAL={}; LIB={}; FOOT={}; POS={}; FP_DIMS={}; NOTES={}

def comp(ref,value,lib,foot,pos,plist,shape=None,note=''):
    VAL[ref]=value;LIB[ref]=lib;FOOT[ref]=foot;POS[ref]=pos;PINS[ref]=plist;FP_DIMS[ref]=shape;NOTES[ref]=note

def pins(names,netmapping):
    return [(i+1,p,netmapping.get(p,'')) for i,p in enumerate(names)]
ESP_LEFT=['EN','VP','VN','D34','D35','D32','D33','D25','D26','D27','D14','D12','D13','GND','VIN']
ESP_RIGHT=['D23','D22','TX0','RX0','D21','D19','D18','D5','TX2','RX2','D4','D2','D15','GND','3V3']
ESP=ESP_LEFT+ESP_RIGHT
emap={
 'D34':'BAT_SENSE','D35':'START','D32':'QTR_S1','D33':'QTR_S2','D25':'QTR_S3','D26':'QTR_S4',
 'D27':'QTR_S5','D14':'QTR_S6','D13':'QTR_S7','VIN':'+5V','D23':'QTR_LEDON',
 'D22':'AIN1','D21':'AIN2','D19':'PWMA','D18':'BIN1','D5':'STBY_GPIO',
 'TX2':'BIN2','RX2':'PWMB','D4':'QTR_S8','3V3':'+3V3','GND':'GND',
 'VN':'MODE',
}
# Kicad pad numbers on ESP footprint correspond to symbol pins in 2 parallel 15-pin rows.
comp('U1','DOIT ESP32 DevKit V1 (30 pin)','LF:ESP32_30','LF:ESP32_30',(0,8.9),pins(ESP,emap),(51,28),'PIN 1 LOCATION AND ROW GAP 25.4 MUST BE MEASURED; USB to +X')
tb_l=['PWMA','AIN2','AIN1','STBY','BIN1','BIN2','PWMB','GND']
tb_r=['GND','VCC','AO1','AO2','BO2','BO1','VM','GND']
tmap={'PWMA':'PWMA','AIN2':'AIN2','AIN1':'AIN1','STBY':'STBY','BIN1':'BIN1','BIN2':'BIN2','PWMB':'PWMB','GND':'GND','VCC':'+3V3','AO1':'ML_1','AO2':'ML_2','BO1':'MR_1','BO2':'MR_2','VM':'VBAT'}
comp('U2','TB6612FNG Pololu carrier','LF:TB6612_Pololu_713','LF:TB6612_Pololu_713',(0,-23),pins(tb_l+tb_r,tmap),(20.3,15.2),'Pololu #713 footprint: rows 12.70mm, 8 pins 2.54mm apart; verify pin 1')
comp('U3','Mini360 MP2307','LF:Mini360_MEASURE','LF:Mini360_MEASURE',(-20,-15.5),pins(['IN+','IN-','OUT+','OUT-'],{'IN+':'VBAT','IN-':'GND','OUT+':'+5V','OUT-':'GND'}),(17,11),'Four holes are NONSTANDARD across Mini-360 clones - measurement required')
qtr=['3V3','GND','IR_LEDON']+['S'+str(i) for i in range(1,9)]
qtrmap={'3V3':'+3V3','GND':'GND','IR_LEDON':'QTR_LEDON',**{'S'+str(i):'QTR_S'+str(i) for i in range(1,9)}}
comp('J1','QTR-8RC RIBBON 1x11','LF:Conn_1x11','LF:Conn_1x11',(0,28),pins(qtr,qtrmap),(28,3.5),'Order is controller header only; QTR sensor module orientation to be verified; S1 at robot left')
comp('J2','JST 2S BAT pigtail pads P2.54','LF:JST_PIGTAIL_MEASURE','LF:JST_PIGTAIL_MEASURE',(23,-10),[(1,'BAT+','BAT_RAW'),(2,'BAT-','GND')],(5,8),'NOT a verified JST mating connector; 2.54 PTH pads for JST pigtail pending choice of actual connector')
comp('J3','MOTOR LEFT','LF:Conn_1x02','LF:Conn_1x02',(-19,-27.5),[(1,'M+','ML_1'),(2,'M-','ML_2')],(5,6),'Motor leads require adequate strain relief')
comp('J4','MOTOR RIGHT','LF:Conn_1x02','LF:Conn_1x02',(14,-18),[(1,'M+','MR_1'),(2,'M-','MR_2')],(5,6),'Right motor connector offset inward due to rear power crowding')
comp('J5','BAT POWER SWITCH 2 pin','LF:Conn_1x02','LF:Conn_1x02',(26,-18),[(1,'IN','BAT_RAW'),(2,'OUT','BAT_SWITCHED')],(5,6),'External in-line switch 2-pad footprint: replace with matching on-board switch after measuring')
comp('F1','3A fuse verify time-current','LF:Fuse_1206','LF:Fuse_1206',(24,-25),[(1,'IN','BAT_SWITCHED'),(2,'OUT','VBAT')],(3.6,2.0),'3A 1206 fuse selection not final; measure stall/inrush, choose voltage interrupt rating')
comp('C1','470uF 16V low-ESR','LF:CP_Radial_D8_P3.5','LF:CP_Radial_D8_P3.5',(17,-26),[(1,'+','VBAT'),(2,'-','GND')],(8,8),'Polarity + to VBAT; at TB6612 VM')
comp('C2','22uF 10V','LF:C_0805','LF:C_0805',(-20,-7.5),[(1,'+','+5V'),(2,'-','GND')],(2.0,1.25),'Choose low-ESR X7R or appropriate 10V rating')
comp('C3','100nF 10V','LF:C_0603','LF:C_0603',(-15,-7.5),[(1,'+','+3V3'),(2,'-','GND')],(1.6,.8),'3V3 decoupling; route close to output/ESP')
comp('R1','100k 1% battery divider top','LF:R_0603','LF:R_0603',(7,-10),[(1,'TOP','VBAT'),(2,'BOTTOM','BAT_SENSE')],(1.6,.8),'ADC1_GPIO34')
comp('R2','33k 1% battery divider bottom','LF:R_0603','LF:R_0603',(11,-10),[(1,'TOP','BAT_SENSE'),(2,'BOTTOM','GND')],(1.6,.8),'ADC calibrate against multimeter')
comp('C4','100nF optional ADC filter','LF:C_0603','LF:C_0603',(15,-10),[(1,'+','BAT_SENSE'),(2,'-','GND')],(1.6,.8),'Optional/DNP; filter with source impedance')
comp('R3','10k START pullup','LF:R_0603','LF:R_0603',(-27,3),[(1,'+','+3V3'),(2,'-','START')],(1.6,.8),'Required input-only D35 external pull-up')
comp('R4','10k MODE pullup','LF:R_0603','LF:R_0603',(-27,14),[(1,'+','+3V3'),(2,'-','MODE')],(1.6,.8),'Required input-only VN/GPIO39 external pull-up')
comp('SW1','START optional','LF:SW_SMD_MEASURE','LF:SW_SMD_MEASURE',(-28.3,7),[(1,'D35','START'),(2,'GND','GND')],(3,3.2),'Optional side-edge SMD switch: choose real footprint')
comp('SW2','MODE optional','LF:SW_SMD_MEASURE','LF:SW_SMD_MEASURE',(-28.3,19),[(1,'VN','MODE'),(2,'GND','GND')],(3,3.2),'Optional side-edge SMD switch: choose real footprint')
comp('R5','100k STBY pulldown','LF:R_0603','LF:R_0603',(4,-10),[(1,'STBY','STBY'),(2,'GND','GND')],(1.6,.8),'Keeps motors in standby at ESP32 reset')
comp('JP1','STBY SOURCE (1-2 GPIO5,2-3 3V3)','LF:SJ_3','LF:SJ_3',(0,-10),[(1,'GPIO5','STBY_GPIO'),(2,'STBY','STBY'),(3,'3V3','+3V3')],(3.2,1.6),'Default bridge 1-2; only use 2-3 when safe to energize on boot')
# Pin index netlist exported below.
NETS=collections.defaultdict(list)
for ref,pl in PINS.items():
    for pin,name,net in pl:
        if net: NETS[net].append((ref,pin,name))
NET_IDS={name:i+1 for i,name in enumerate(sorted(NETS))}

# write BOM and connector netlist CSV and netlist XML format compatible with KiCad importer
with open(ROOT/'bom_preliminary.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['Ref','Value','Footprint','Quantity','Status / measurement required'])
    for ref in sorted(PINS):w.writerow([ref,VAL[ref],FOOT[ref],1,NOTES[ref]])
with open(ROOT/'netlist.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['Net','Reference','Pin','Pad Name'])
    for net,links in sorted(NETS.items()):
        for ref,pin,pname in links:w.writerow([net,ref,pin,pname])
# KiCad XML netlist standalone, pins and components all named
from xml.sax.saxutils import escape
xml=['<?xml version="1.0" encoding="utf-8"?>','<export version="E">','<design><source>line_follower_revA.kicad_sch</source><date>2026-11-13</date><tool>LineFollower RevA script</tool></design>','<components>']
for ref in sorted(PINS):
    xml += [f'<comp ref="{escape(ref)}"><value>{escape(VAL[ref])}</value><footprint>{escape(FOOT[ref])}</footprint><libsource lib="LF" part="{escape(LIB[ref].split(":")[1])}" description="custom module"/></comp>']
xml += ['</components><nets>']
for net,links in sorted(NETS.items()):
    xml.append(f'<net code="{NET_IDS[net]}" name="{escape(net)}">')
    for ref,pin,name in links:xml.append(f'<node ref="{ref}" pin="{pin}" pinfunction="{escape(name)}"/>')
    xml.append('</net>')
xml+=['</nets></export>']
(ROOT/'line_follower_revA.net').write_text('\n'.join(xml))
(ROOT/'connectivity.json').write_text(json.dumps({'components':{r:{'value':VAL[r],'footprint':FOOT[r],'position_xy_mm':POS[r],'pins':PINS[r],'note':NOTES[r]} for r in PINS},'nets':NETS},indent=2))

# KiCad footprint placement. Coordinates: X positive right, board-local Y positive forward.
# KiCad +Y downward; parent board center=(100,100), use (100+x,100-y).

def quote(s):return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'

def q_xy(x,y): return f'{100+x:.4f} {100-y:.4f}'

def circle_edges(points,size): pass

# IMPORTANT: PTH footprints are copper rings. SMD pads created as placeholders for real chosen parts.

def footprints_for(ref):
    """pad (number, x-relative, y-relative as KiCad down, shape, drill, copper net)"""
    if ref=='U1':
        pad=[]
        for i,pname,net in PINS[ref]:
            x=(-17.78+2.54*(i-1)) if i<=15 else (-17.78+2.54*(i-16))
            # ESP row: 1..15 rear; 16..30 front. USB to +X.
            y=+12.7 if i<=15 else -12.7
            pad.append((i,x,y,'thru_hole',1.7,.9))
        return pad
    if ref=='U2':
        pad=[]
        for i,name,net in PINS[ref]:
            x=(-8.89+2.54*(i-1)) if i<=8 else (-8.89+2.54*(i-9))
            y=+6.35 if i<=8 else -6.35
            pad.append((i,x,y,'thru_hole',1.75,.92))
        return pad
    if ref=='U3':return [(1,-6.7,-3.2,'thru_hole',1.7,.9),(2,-6.7,+3.2,'thru_hole',1.7,.9),(3,6.7,-3.2,'thru_hole',1.7,.9),(4,6.7,3.2,'thru_hole',1.7,.9)]
    if ref=='J1':return [(i,-12.7+(i-1)*2.54,0,'thru_hole',1.7,.9) for i in range(1,12)]
    if ref in ['J2','J3','J4','J5']:return [(1,0,-1.27,'thru_hole',1.8,1),(2,0,1.27,'thru_hole',1.8,1)]
    if ref=='C1':return [(1,-1.75,0,'thru_hole',2.0,.9),(2,1.75,0,'thru_hole',2.0,.9)]
    if ref=='JP1':return [(1,-1.2,0,'smd',1.0,0),(2,0,0,'smd',1.0,0),(3,1.2,0,'smd',1.0,0)]
    if ref.startswith('SW'):return [(1,0,-1.3,'smd',.8,0),(2,0,1.3,'smd',.8,0)]
    if ref=='F1':return [(1,-1.55,0,'smd',1.05,0),(2,1.55,0,'smd',1.05,0)]
    if ref=='C2':return [(1,-.95,0,'smd',1.05,0),(2,.95,0,'smd',1.05,0)]
    return [(1,-.75,0,'smd',.8,0),(2,.75,0,'smd',.8,0)]

# one custom footprint per reference: schematic can update from netlist without requiring external library
# rectangle is only outline guideline: module-only dimension (not pad size or connector housing)
def fp(ref,x,y):
    dx,dy=FP_DIMS[ref]
    kind='through_hole' if any(z[3]=='thru_hole' for z in footprints_for(ref)) else 'smd'
    out=[f'(footprint {quote(FOOT[ref])} (layer "F.Cu") (tedit 00000000) (at {q_xy(x,y)}) (attr {kind})',
        f' (fp_text reference {quote(ref)} (at 0 {-dy/2-1.3:.2f}) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.16))))',
        f' (fp_text value {quote(VAL[ref])} (at 0 {dy/2+1.6:.2f}) (layer "F.Fab") (effects (font (size .6 .6) (thickness .12))))',
        f' (fp_rect (start {-dx/2:.3f} {-dy/2:.3f}) (end {dx/2:.3f} {dy/2:.3f}) (stroke (width 0.12) (type default)) (fill none) (layer "F.SilkS"))',
        f' (fp_circle (center {-dx/2:.3f} {-dy/2:.3f}) (end {-dx/2+.75:.3f} {-dy/2:.3f}) (stroke (width .16) (type default)) (fill none) (layer "F.SilkS"))']
    for i,px,py,t,sz,drill in footprints_for(ref):
        if t=='thru_hole':
            out.append(f' (pad "{i}" thru_hole circle (at {px:.3f} {py:.3f}) (size {sz:.3f} {sz:.3f}) (drill {drill:.3f}) (layers "*.Cu" "*.Mask")'+ (f' (net {NET_IDS[PINS[ref][i-1][2]]} {quote(PINS[ref][i-1][2])})' if PINS[ref][i-1][2] else '')+')')
        else:
            out.append(f' (pad "{i}" smd roundrect (at {px:.3f} {py:.3f}) (size {sz:.3f} {max(.7,sz):.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio .2)'+(f' (net {NET_IDS[PINS[ref][i-1][2]]} {quote(PINS[ref][i-1][2])})' if PINS[ref][i-1][2] else '')+')')
    out.append(')');return '\n'.join(out)

board=['(kicad_pcb (version 20240108) (generator pcbnew)', '(general (thickness 1.6))','(paper "A4")',
  '(layers (0 "F.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user) (37 "F.SilkS" user) (38 "B.Mask" user) (39 "F.Mask" user) (40 "Dwgs.User" user) (44 "Edge.Cuts" user) (45 "Margin" user) (48 "B.Fab" user) (49 "F.Fab" user))',
  '(setup (pad_to_mask_clearance 0))','(net 0 "")']
for net,i in sorted(NET_IDS.items(),key=lambda kv:kv[1]):board.append(f'(net {i} {quote(net)})')
for ref,(x,y) in POS.items():board.append(fp(ref,x,y))
# Board dimensions 60x65. Board coordinates x70..130, y67.5..132.5.
board.append('(gr_rect (start 70 67.5) (end 130 132.5) (stroke (width 0.05) (type default)) (fill none) (layer "Edge.Cuts"))')
for x in [74,126]:
 for y in [71.5,128.5]:
  board.append(f'''(footprint "LF:MountingHole_M3" (layer "F.Cu") (at {x} {y}) (attr exclude_from_pos_files exclude_from_bom)
   (fp_text reference "H_{int(x)}_{int(y)}" (at 0 -3.1) (layer "F.SilkS") (effects (font (size .8 .8) (thickness .12))))
   (fp_text value "M3" (at 0 3) (layer "F.Fab") (effects (font (size .7 .7) (thickness .1))))
   (pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu" "*.Mask")) )''')
# Bottom ground pour zone declaration ONLY, KiCad fills when opened (not filled in this preview).
board.append(f'''(zone (net {NET_IDS['GND']}) (net_name "GND") (layer "B.Cu") (hatch edge 0.5)
(connect_pads (clearance .3)) (min_thickness .25) (fill yes (thermal_gap .35) (thermal_bridge_width .5))
(polygon (pts (xy 70.3 67.8) (xy 129.7 67.8) (xy 129.7 132.2) (xy 70.3 132.2))))''')
board.append(')')
(ROOT/(PRJ+'.kicad_pcb')).write_text('\n'.join(board)+'\n')

# Schematic symbols built-in locally and joined by net labels. Each symbol uses its pad names.
# Unlike a block-diagram, this is an electrical KiCad schematic and net names are exportable.
# Pins are on the left and right sides; all labels are directly at pin connection points.
# KiCad .kicad_sch format v6. Last model pin = physical pad number.

def uid():return str(uuid.uuid4())
SHEET_ID=uid()
libsymbols=[]
for ref,pads in sorted(PINS.items()):
    key='LF_'+ref; cnt=len(pads); rows=(cnt+1)//2
    w=17.78; H=(rows+1)*2.54
    out=[f'(symbol "LF:{key}" (pin_names (offset .8)) (in_bom yes) (on_board yes)',
         f'(property "Reference" {quote(ref[0])} (at 0 {H/2+3.81:.3f} 0) (effects (font (size 1.27 1.27))))',
         f'(property "Value" {quote(VAL[ref])} (at 0 {-H/2-3.81:.3f} 0) (effects (font (size 1 1))))',
         f'(property "Footprint" {quote(FOOT[ref])} (at 0 0 0) (effects (font (size 1 1)) (hide yes)))',
         f'(symbol "{key}_0_1" (rectangle (start {-w:.3f} {H/2:.3f}) (end {w:.3f} {-H/2:.3f}) (stroke (width .254) (type default)) (fill (type background))))',
         f'(symbol "{key}_1_1"']
    for j,(pnum,pname,net) in enumerate(pads):
        left=j<rows; index=j if left else j-rows
        y=(rows-1)*1.27-index*2.54
        # schematic pin electrically neutral by default
        ptype='input' if ref in ['U1','J1'] else 'passive'
        xx=-w-3.81 if left else w+3.81; rot=0 if left else 180
        out.append(f' (pin {ptype} line (at {xx:.3f} {y:.3f} {rot}) (length 3.81) (name {quote(pname)} (effects (font (size 1 1)))) (number "{pnum}" (effects (font (size 1 1)))))')
    out+=[')',')'];libsymbols.append('\n'.join(out))

sch=['(kicad_sch (version 20211123) (generator eeschema)',f'(uuid {SHEET_ID})','(paper "A3")',f'(lib_symbols {" ".join(libsymbols)})']
# Group schematic symbols in columns; 3 columns x 8 rows. Leave room for labels extending 5.08mm.
reforder=['U1','U2','U3','J1','J2','J3','J4','J5','F1','C1','C2','C3','R1','R2','C4','R3','R4','SW1','SW2','R5','JP1']
# many rows at 28 mm spacing; A3 420x297; explicit placement compressed rows, 3 cols
for idx,ref in enumerate(reforder):
    col=idx//7;row=idx%7
    x=67+col*135; y=31+row*37
    pads=PINS[ref];cnt=len(pads);rows=(cnt+1)//2;w=17.78
    sid=uid(); key='LF_'+ref
    sch.append(f'''(symbol (lib_id "LF:{key}") (at {x:.3f} {y:.3f} 0) (unit 1) (in_bom yes) (on_board yes) (dnp no) (uuid {sid})
 (property "Reference" {quote(ref)} (at {x:.3f} {y-22:.3f} 0) (effects (font (size 1.0 1.0))))
 (property "Value" {quote(VAL[ref])} (at {x:.3f} {y-25:.3f} 0) (effects (font (size .85 .85))))
 (property "Footprint" {quote(FOOT[ref])} (at {x:.3f} {y:.3f} 0) (effects (font (size .65 .65)) (hide yes)))
 (instances (project "{PRJ}" (path "/{SHEET_ID}" (reference "{ref}") (unit 1)))))''')
    for j,(pin,pname,net) in enumerate(pads):
        if not net:continue
        left=j<rows;index=j if left else j-rows
        yp=y-((rows-1)*1.27-index*2.54)
        # external endpoint x +/- (box half width + 3.81 pin) = +/- 21.59.
        # Label directly at pin electrical end. Orientation 0 on left and 180 on right.
        ex=x-21.59 if left else x+21.59
        # net labels anchor to pin endpoint without a wire (must be exact endpoint). KiCad label connection should be live.
        sch.append(f'(label {quote(net)} (at {ex:.3f} {yp:.3f} {0 if left else 180}) (effects (font (size .8 .8)) (justify left bottom)) (uuid {uid()}))')
sch.append(')')
(ROOT/(PRJ+'.kicad_sch')).write_text('\n'.join(sch)+'\n')
(ROOT/(PRJ+'.kicad_pro')).write_text('{}\n')

# Local custom footprints library: an exact copy of placement geometry, not verified physical module envelopes
pretty=ROOT/'LF.pretty';pretty.mkdir(exist_ok=True)
for ref in PINS:
    src=fp(ref,0,0)
    # remove world translation, strip nets and reference name for generic reuse? use full footprint in library without pads' net fields
    import re
    src=re.sub(r' \(net \d+ "[^"]*"\)', '', src)
    ftname=FOOT[ref].split(':')[-1]
    src=src.replace(f'"LF:{ftname}"',f'"{ftname}"')
    (pretty/(ftname+'.kicad_mod')).write_text(src+'\n')
(ROOT/'fp-lib-table').write_text('(fp_lib_table (lib (name "LF") (type "KiCad") (uri "${KIPRJMOD}/LF.pretty") (options "") (descr "Preliminary line follower footprints - check before fabrication")))\n')

# SVG board preview (physical +Y forward), top/bottom grouped; show pad net IDs, low-opacity connection ratsnest.
from xml.sax.saxutils import escape as xe
import cairosvg
S=8.0; pad=40
def sx(x):return (30+x)*S+pad
def sy(y):return (32.5-y)*S+pad

def svg_layer(layer):
    W=60*S+2*pad;H=65*S+2*pad
    bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
          '<rect width="100%" height="100%" fill="#e8eef3"/>',
          f'<rect x="{pad}" y="{pad}" width="{60*S}" height="{65*S}" rx="4" fill="{ "#24603c" if layer=="top" else "#52744e" }" stroke="#1b2630" stroke-width="2"/>']
    if layer=='bottom':
        bits.append(f'<rect x="{pad+2}" y="{pad+2}" width="{60*S-4}" height="{65*S-4}" fill="#b78824" opacity=".37"/>')
    # outlines only for top layer; bottom all THT pads and flipped annotation as appropriate
    if layer=='top':
      for ref,(x,y) in POS.items():
        dx,dy=FP_DIMS[ref]
        bits.append(f'<rect x="{sx(x-dx/2):.1f}" y="{sy(y+dy/2):.1f}" width="{dx*S:.1f}" height="{dy*S:.1f}" fill="none" stroke="#eeeeb1" stroke-width="1.5"/>')
        bits.append(f'<text x="{sx(x):.1f}" y="{sy(y+dy/2)+9:.1f}" fill="#ffffff" text-anchor="middle" font-size="11" font-family="Arial" font-weight="bold">{xe(ref)}</text>')
    for ref,(x,y) in POS.items():
      for i,rx,ry,typ,sz,drill in footprints_for(ref):
        if layer=='bottom' and typ!='thru_hole':continue
        X=sx(x+rx);Y=sy(y-ry)
        bits.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{sz*S/2:.1f}" fill="#dca943" stroke="#f4ca56" stroke-width="1"/>')
        if typ=='thru_hole':bits.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{drill*S/2:.1f}" fill="#162928"/>')
    for x in [-26,26]:
      for y in [-28.5,28.5]:
        bits.append(f'<circle cx="{sx(x)}" cy="{sy(y)}" r="{3.2*S/2}" fill="#e8eef3" stroke="#ddd" stroke-width="1.5"/>')
    bits.append(f'<text x="{pad+7}" y="{pad-12}" font-size="16" font-family="Arial" fill="#273342" font-weight="bold">{layer.upper()} | 60 x 65 mm | PLACEMENT ONLY - NO ROUTING</text>')
    bits.append(f'<text x="{pad+7}" y="{H-12}" font-size="11" font-family="Arial" fill="#424c57">Front = +Y (top)  |  ESP32 USB faces +X  |  Not for fabrication</text>')
    bits.append('</svg>')
    svg='\n'.join(bits)
    (ROOT.parent/'previews'/f'pcb_{layer}_preview.svg').write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(ROOT.parent/'previews'/f'pcb_{layer}_preview.png'),output_width=1000,output_height=1000*H/W)
for layer in ['top','bottom']:svg_layer(layer)

(ROOT/'ROUTING_PENDING.md').write_text('''# Preliminary PCB, REV A - DO NOT ORDER\n\nThese KiCad source files are an electrical pin map and preliminary physical placement, **not a routed/manufacturable board**. The `.kicad_pcb` contains 0 copper tracks; the bottom-layer GND copper pour is defined but not filled.\n\n**No Gerbers/drill manufacturing package is provided intentionally:** generating them for a board with unmapped module clones, unverified JST polarity, missing routing and no Electrical Rules Check (ERC) or Design Rules Check (DRC) would create a dangerous false ready-to-fabricate signal. Do not manufacture until all items below are resolved.\n\n1. Verify ESP32 30-pin outer dimensions, exact 25.4mm header-row spacing, x-offset of pin 1, USB clearance, module antenna free space.\n2. Measure actual Mini-360 four-hole XY spacing and orientation, and board side component keepout.\n3. Choose exact mating battery JST type (RCY, PH, XH, etc), pitch, pin orientation and wire polarity. The current J2 is a PTH pad **for a JST pigtail**, not a certified mating footprint.\n4. Confirm TB6612 Pololu #713 versus other carrier; pin order and board outline.\n5. Choose rated 3A fuse (time-current curve, package), power switch and side controls, and suitable motor wire connectors.\n6. Decide whether QTR header requires shrouded / keyed connector and precise ribbon orientation.\n7. Route every signal and power track, clear 0.2mm minimum copper spacing, wider battery/VM/motor returns, add vias and refill B.Cu GND.\n8. Run KiCad ERC, DRC, 3D/courtyard collision review; board fab outputs only after checks are clean.\n\nTraces required: >=1.0mm on battery/VM/motor GND; signal 0.25-0.30mm. Net names and pin maps are documented in `netlist.csv`.\n''')
print('Wrote',len(PINS),'components,',len(NETS),'electrical nets; KiCad, XML, CSV, SVG, PNG files')
