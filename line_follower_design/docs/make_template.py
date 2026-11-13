from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
import ezdxf, os
root=os.path.dirname(os.path.dirname(__file__))
out=os.path.join(root,'docs','chassis_1to1_A4.pdf')
c=canvas.Canvas(out,pagesize=A4)
w,h=A4
c.setFont('Helvetica-Bold',14)
c.drawString(17*mm,h-17*mm,'LINE FOLLOWER - 1:1 LASER / DRILL TEMPLATE')
c.setFont('Helvetica',8)
c.drawString(17*mm,h-22*mm,'REV A  |  Print at 100%, no fit-to-page  |  Verify the 50 mm calibration bar')
# Draw with world mm origin at (page x, page y), user Y-axis points UP

def from_dxf(name, ox_mm, oy_mm, scale=1):
    doc=ezdxf.readfile(os.path.join(root,'cad',name))
    c.setStrokeColor(HexColor('#1C334D'))
    c.setLineWidth(0.38)
    c.saveState()
    c.translate(ox_mm*mm,oy_mm*mm)
    c.scale(scale,scale)
    for entity in doc.modelspace():
        if entity.dxftype()=='LINE':
            a=entity.dxf.start;b=entity.dxf.end
            c.line(a.x*mm,a.y*mm,b.x*mm,b.y*mm)
    c.restoreState()
# Main plate bottom at Y -25, top +105; origin at y position 121mm from bottom.
from_dxf('chassis_plate.dxf',55,147)
c.setFillColor(HexColor('#18324D'))
c.setFont('Helvetica-Bold',11)
c.drawString(18*mm,263*mm,'A. MAIN PLATE - 3 mm plywood/acrylic')
c.setFont('Helvetica',8)
c.drawString(18*mm,258*mm,'Cut external outline; drill/laser inner contours. Approx. 68 x 130 mm.')
# Bracket position drawing translate origin relative to actual y69-108
from_dxf('qtr_caster_bracket.dxf',104,-37)
c.setFont('Helvetica-Bold',10)
c.drawString(18*mm,89*mm,'B. QTR + CASTER BRACKET')
c.setFont('Helvetica',8)
c.drawString(18*mm,84*mm,'82 x 39 mm; outer holes for QTR mounting. Hole patterns must be checked.')
# calibration: 50 mm horizontal
c.setStrokeColor(HexColor('#8c1b1b'));c.setLineWidth(.9)
c.line(17*mm,22*mm,67*mm,22*mm)
for x in [17,67]: c.line(x*mm,19*mm,x*mm,25*mm)
c.setFillColor(HexColor('#8c1b1b'));c.setFont('Helvetica-Bold',9)
c.drawString(18*mm,26*mm,'50.00 mm SCALE CHECK')
c.setFillColor(HexColor('#364654')); c.setFont('Helvetica',7)
c.drawString(18*mm,11*mm,'MEASURE before cutting: motor bracket holes, caster holes, QTR sensor offset, and screw fit.')
c.showPage();c.save();print(out)
