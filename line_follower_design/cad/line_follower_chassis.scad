// Line-following robot chassis REV A - units mm.
// +X to right, +Y forward, +Z up. Axle center: (0,0,21).
// Top-level selection from command line: -D 'part="plate"' etc.
// Verify every 'MEASURE' parameter before laser cutting / 3D printing.
part = "assembly"; // [assembly,plate,sensor_bracket,pcb_kinematic,plate_2d,bracket_2d]
$fn=56;
// REQUIRED USER PARAMETERS
wheel_diameter=42;
wheel_width=17;
wheel_track=90;
plate_thickness=3;
sensor_distance=95;
battery_length=55;
battery_width=30;
battery_height=15;
motor_bracket_hole_spacing=16; // MEASURE center-to-center, THIS IS A PLACEHOLDER
pcb_width=60;
pcb_length=65;
// Other mechanical parameters (all mm)
axle_height=wheel_diameter/2;
corner_radius=2.7;
body_width=68;
body_rear_y=-25;
body_shoulder_y=40;
body_nose_width=30;
body_front_y=105;
pcb_center_y=7.5;
pcb_hole_inset=4;
pcb_hole_dia=3.2;
plate_underside_z=28; // chosen: above assumed 12-mm-high N20 motor at axle z=21 by 1mm
plate_top_z=plate_underside_z+plate_thickness;
pcb_underside_z=50; // clears 15 mm battery on plate with 4 mm gap
sensor_bracket_thickness=3;
sensor_bracket_width=82;
sensor_bracket_rear_y=69;
sensor_bracket_front_y=108;
sensor_bracket_center_y=(sensor_bracket_rear_y+sensor_bracket_front_y)/2;
sensor_bracket_to_nose_x=9;
sensor_bracket_to_nose_y=sensor_distance-4;
qtr_outer_hole_span=69.85;  // Pololu: 2.75 inch, outer-hole CENTER distance
qtr_mount_y=sensor_distance-4; // MEASURE QTR hole-to-sensor optical axis offset!
qtr_board_length=74.93;
qtr_board_depth=12.7;
qtr_module_thickness=3.175; // approximate maximum module thickness, inspect exact sensor face
sensor_optical_face_z=3;
qtr_board_top_z=sensor_optical_face_z+qtr_module_thickness;
sensor_bracket_underside_z=plate_underside_z-sensor_bracket_thickness;
sensor_standoff_length=sensor_bracket_underside_z-qtr_board_top_z; // ~18.825
caster_y=sensor_distance-19; // shifted aft to avoid 13mm-ball housing colliding with QTR board
caster_ball_diameter=13;
caster_housing_diameter=15; // MEASURE real housing outer diameter
caster_mount_to_floor=18; // MEASURE real ball caster height from mount face to floor
caster_shim_height=sensor_bracket_underside_z-caster_mount_to_floor;
// MEASURE N20 body and bracket details; model motor bodies are ENVELOPES ONLY
n20_body_length=25; n20_body_width=10; n20_body_height=12;
// laser drill assumptions
motor_mount_hole_dia=2.2; // MEASURE screws and bracket
qtr_hole_dia=2.3; // #2 screw/M2 clearance, MEASURE
caster_mount_spacing=12; // MEASURE caster mounting-hole centers before making this bracket
caster_mount_hole_dia=2.4;
strap_slot_length=8; strap_slot_width=3.5;
wire_hole_dia=6;

// Flattened, rounded outline. The T is 68 mm wide, with a 30 mm nose.
module plate_outline_2d(){
  offset(r=corner_radius) offset(delta=-corner_radius)
    polygon(points=[[-body_width/2,body_rear_y],[body_width/2,body_rear_y],
      [body_width/2,body_shoulder_y],[body_nose_width/2,body_shoulder_y],
      [body_nose_width/2,body_front_y],[-body_nose_width/2,body_front_y],
      [-body_nose_width/2,body_shoulder_y],[-body_width/2,body_shoulder_y]]);
}
module slot_2d(len,w){ hull(){translate([-(len-w)/2,0]) circle(d=w); translate([(len-w)/2,0]) circle(d=w);}}
module main_plate_2d(){ difference(){plate_outline_2d();
  // Four PCBA M3 mounting holes at +/-26, Y=-21,+36.
  for(x=[-pcb_width/2+pcb_hole_inset,pcb_width/2-pcb_hole_inset])
    for(y=[pcb_center_y-pcb_length/2+pcb_hole_inset,pcb_center_y+pcb_length/2-pcb_hole_inset])
      translate([x,y]) circle(d=pcb_hole_dia);
  // Two motor brackets (hole pattern is a placeholder pending measurement).
  for(side=[-1,1]) for(y=[-motor_bracket_hole_spacing/2,motor_bracket_hole_spacing/2])
    translate([side*23,y]) circle(d=motor_mount_hole_dia);
  // Two 6-mm motor-wire access holes.
  for(x=[-15,15]) translate([x,18]) circle(d=wire_hole_dia);
  // Two slots for one continuous Velcro strap; positions are adjustable.
  for(x=[-20,20]) translate([x,2]) rotate(90) slot_2d(strap_slot_length,strap_slot_width);
  // Fixed bracket mounting at Y=91, +/-9.
  for(x=[-sensor_bracket_to_nose_x,sensor_bracket_to_nose_x])
    translate([x,sensor_bracket_to_nose_y]) circle(d=pcb_hole_dia);
}}
module sensor_bracket_2d(){difference(){
  offset(r=2) offset(delta=-2)
    translate([-sensor_bracket_width/2,sensor_bracket_rear_y])
      square([sensor_bracket_width,sensor_bracket_front_y-sensor_bracket_rear_y]);
  for(x=[-sensor_bracket_to_nose_x,sensor_bracket_to_nose_x])
    translate([x,sensor_bracket_to_nose_y]) circle(d=3.2);
  for(x=[-qtr_outer_hole_span/2,qtr_outer_hole_span/2])
    translate([x,qtr_mount_y]) circle(d=qtr_hole_dia);
  // caster mounts: DO NOT CUT UNTIL MEASURED; currently assumes two M2 holes 12 mm apart.
  for(x=[-caster_mount_spacing/2,caster_mount_spacing/2])
    translate([x,caster_y]) circle(d=caster_mount_hole_dia);
}}
module plate(){linear_extrude(height=plate_thickness) main_plate_2d();}
module bracket(){linear_extrude(height=sensor_bracket_thickness) sensor_bracket_2d();}
module standoff(x,y,z0,z1,od=5,ID=3.2){
 if(z1>z0) translate([x,y,z0]) difference(){cylinder(h=z1-z0,d=od); translate([0,0,-.1]) cylinder(h=z1-z0+.2,d=ID);}
}
module wheel_assy(side){
  color("#222222") translate([side*wheel_track/2,0,axle_height]) rotate([0,90,0])
  difference(){cylinder(h=wheel_width, d=wheel_diameter,center=true);
    cylinder(h=wheel_width+.2, d=3,center=true);}
  color("#c5cbd3") translate([side*(wheel_track/2-wheel_width/2-1.5-n20_body_length/2),0,axle_height])
   cube([n20_body_length,n20_body_width,n20_body_height],center=true);
}
module qtr_assy(){
  color("#c92f34") translate([0,qtr_mount_y,qtr_board_top_z-0.8])
    cube([qtr_board_length,qtr_board_depth,1.6], center=true);
  // 8 equally spaced sensor packages, centered on the optical line, x pitch=9.525.
  for(i=[0:7]) color("black") translate([(i-3.5)*9.525,sensor_distance,sensor_optical_face_z+1.2])
    cube([4.0,3.2,2.4],center=true);
}
module caster_assy(){
  color("#9098a5") translate([0,caster_y,caster_ball_diameter/2]) sphere(d=caster_ball_diameter);
  color("#4a5362") translate([0,caster_y,caster_ball_diameter+1])
    cylinder(h=3,d=caster_housing_diameter,center=true);
  color("#999999") translate([0,caster_y,sensor_bracket_underside_z-caster_shim_height/2])
    cylinder(h=caster_shim_height,d=14,center=true);
}
module pcb_assy(){
  // Approximate assembly only. See separate *.kicad_pcb layout for copper and exact holes.
  color("#126657") translate([0,pcb_center_y,pcb_underside_z+0.8])
    difference(){cube([pcb_width,pcb_length,1.6],center=true);
      for(x=[-pcb_width/2+pcb_hole_inset,pcb_width/2-pcb_hole_inset])
      for(y=[-pcb_length/2+pcb_hole_inset,pcb_length/2-pcb_hole_inset])
        translate([x,y,-2])cylinder(d=3.2,h=4);}
  // ESP, oriented horizontally; its USB faces +X.
  color("#151d2a") translate([0,pcb_center_y+8.9,pcb_underside_z+11]) cube([51,28,1.6],center=true);
  color("#b6bdc7") translate([26,pcb_center_y+8.9,pcb_underside_z+11]) cube([6,7,3.5],center=true);
  // TB6612 small green carrier, to rear.
  color("#167040") translate([0,pcb_center_y-23,pcb_underside_z+9]) cube([20.3,15.2,1.2],center=true);
}
module assembly(){
 color("#c8a77e") translate([0,0,plate_underside_z]) plate();
 color("#c8a77e") translate([0,0,sensor_bracket_underside_z]) bracket();
 for(side=[-1,1]) wheel_assy(side);
 color("#3152b2") translate([0,0,plate_top_z+battery_height/2]) cube([battery_width,battery_length,battery_height],center=true);
 for(x=[-pcb_width/2+pcb_hole_inset,pcb_width/2-pcb_hole_inset])
 for(y=[pcb_center_y-pcb_length/2+pcb_hole_inset,pcb_center_y+pcb_length/2-pcb_hole_inset])
 color("#aab5bf") standoff(x,y,plate_top_z,pcb_underside_z);
 pcb_assy();
 for(x=[-sensor_bracket_to_nose_x,sensor_bracket_to_nose_x])
 color("#aab5bf") standoff(x,sensor_bracket_to_nose_y,sensor_bracket_underside_z+sensor_bracket_thickness,plate_underside_z,5,3.2);
 for(x=[-qtr_outer_hole_span/2,qtr_outer_hole_span/2])
 color("#aab5bf") standoff(x,qtr_mount_y,qtr_board_top_z,sensor_bracket_underside_z,4.2,2.2);
 qtr_assy(); caster_assy();
}
if(part=="assembly") assembly();
else if(part=="plate") plate();
else if(part=="sensor_bracket") bracket();
else if(part=="plate_2d") main_plate_2d();
else if(part=="bracket_2d") sensor_bracket_2d();
else if(part=="pcb_kinematic") pcb_assy();
