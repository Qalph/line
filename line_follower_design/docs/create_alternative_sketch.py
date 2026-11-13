import ezdxf
from pathlib import Path
import svgwrite,cairosvg
root=Path(__file__).resolve().parents[1]; out=root/'previews'/'pcb_as_chassis_alternative.svg'
scale=5.0;margin=70; W=900; H=970
# origin center chassis at x450, y~530, front +Y points up
def P(x,y):return (450+scale*x,765-scale*y)
dwg=svgwrite.Drawing(str(out),size=(W,H),viewBox=f'0 0 {W} {H}')
dwg.add(dwg.rect(insert=(0,0),size=(W,H),fill='#f1f5f8'))
dwg.add(dwg.text('ALTERNATIVE: STRUCTURAL FR4 PCB AS T-CHASSIS',insert=(40,46),font_family='Arial',font_size=23,font_weight='bold',fill='#20344b'))
dwg.add(dwg.text('Concept only - not a routed PCB; motor brackets under FR4, QTR on separate cross-bar',insert=(40,76),font_family='Arial',font_size=15,fill='#526478'))
# main chassis T polygon exact envelope
points=[(-34,-25),(34,-25),(34,40),(15,40),(15,105),(-15,105),(-15,40),(-34,40)]
dwg.add(dwg.polygon(points=[P(*pt) for pt in points],fill='#187454',stroke='#193c32',stroke_width=3))
# continuous bottom GND area visual only
body=[(-30,-21),(30,-21),(30,35),(11,35),(11,101),(-11,101),(-11,35),(-30,35)]
dwg.add(dwg.polygon(points=[P(*pt) for pt in body],fill='#d0c182',opacity='.23',stroke='#e3c76e',stroke_width=1.4,stroke_dasharray='4,5'))
# electronics footprint area
a=P(-30,-25);b=P(30,40)
dwg.add(dwg.rect(insert=(a[0],b[1]),size=(b[0]-a[0],a[1]-b[1]),fill='#2c9f72',stroke='#e0ffea',stroke_width=2))
dwg.add(dwg.text('ESP32 + TB6612',insert=P(-22,8),fill='white',font_family='Arial',font_size=17,font_weight='bold'))
dwg.add(dwg.text('Power distribution',insert=P(-22,-9),fill='white',font_family='Arial',font_size=14))
# nose trace routing conceptual
for x in [-7,0,7]:
 dwg.add(dwg.line(P(x,42),P(x,91),stroke='#c7ed7e',stroke_width=2,stroke_dasharray='4,4'))
# wheels
for x in [-45,45]:
 pt=P(x,0)
 dwg.add(dwg.rect(insert=(pt[0]-17*scale/2,pt[1]-42*scale/2),size=(17*scale,42*scale),fill='#24292c',stroke='#171717',stroke_width=2,rx=15))
 dwg.add(dwg.circle(center=pt,r=5,fill='#cbd3d9'))
# Sensor cross-bar physically wider than nose
p0=P(-41,88); p1=P(41,103)
dwg.add(dwg.rect(insert=(p0[0],p1[1]),size=(p1[0]-p0[0],p0[1]-p1[1]),fill='#d3a36a',stroke='#866341',stroke_width=2,rx=7))
# QTR sensor array, blue line
start=P(-37.46,95);end=P(37.46,95)
dwg.add(dwg.line(start,end,stroke='#fe5456',stroke_width=7))
for i in range(8):
 pt=P((i-3.5)*9.525,95);dwg.add(dwg.circle(center=pt,r=6,fill='#171f29'))
# Hole pairs and underbody mounts
for x in [-26,26]:
 for y in [-21,36]:
  dwg.add(dwg.circle(center=P(x,y),r=8.16,fill='#f1f5f8',stroke='#d5c682',stroke_width=2))
for x in [-23,23]:
 for y in [-8,8]: dwg.add(dwg.circle(center=P(x,y),r=5.6,fill='#e9f1e9',stroke='#132f27',stroke_width=2))
# label arrows
for t,xy in [('MOTOR BRACKETS UNDERNEATH', (500,830)),('QTR CROSS-BRACKET (SEPARATE)',(485,218)),('NO COPPER NEAR M3 HOLES',(500,920))]:
 dwg.add(dwg.text(t,insert=xy,font_size=15,font_family='Arial',fill='#30495c'))
dwg.add(dwg.text('Benefits: lower mass and no separate plate. Costs: large PCB, high-current EMI, flex and harder repairs.',insert=(40,960),font_size=14,font_family='Arial',fill='#34495e'))
dwg.save()
cairosvg.svg2png(url=str(out),write_to=str(root/'previews'/'pcb_as_chassis_alternative.png'))
print('created',out)
