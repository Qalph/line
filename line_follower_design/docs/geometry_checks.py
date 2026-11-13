import json, math
from pathlib import Path
import trimesh
cad=Path(__file__).resolve().parents[1]/'cad'
wheel_d=42; width=17; track=90; body_w=68; body_rear=-25; front=105
inner_face=track/2-width/2; clearance=inner_face-body_w/2
wheel_width_envelope=track+width
battery_rear=-55/2; bracket_front=108
sensor_pos=95; rear=min(body_rear,battery_rear)
optical_to_rear=sensor_pos-rear; optical_to_front=bracket_front-sensor_pos
all_white_finish=400; whole_body_stop_window=[optical_to_rear,all_white_finish-optical_to_front]
protected_finish_stop_window=[whole_body_stop_window[0]+50,whole_body_stop_window[1]-50]
qtr_top=3+3.175; bracket_under=28-3
standoff=bracket_under-qtr_top
caster_shim=bracket_under-18
battery_top=28+3+15;pcb_underside=50
assembly=trimesh.load(cad/'robot_assembly.stl',force='mesh')
model_bounds=assembly.bounds.tolist()
res={'wheel_to_body_nominal_clearance_mm':clearance,'overall_width_mm':wheel_width_envelope,
'overall_length_mm':bracket_front-rear,'height_from_assembly_stl_mm':model_bounds[1][2]-model_bounds[0][2],
'model_stl_bounds_mm':model_bounds,'qtr_optical_face_height_mm':3,'sensor_nominal_support_spacer_mm':standoff,
'caster_shim_nominal_mm':caster_shim,'battery_top_z_mm':battery_top,'pcb_underside_z_mm':pcb_underside,
'board_above_wheel_top_clearance_mm':pcb_underside-wheel_d,
'sensor_to_rearmost_body_mm':optical_to_rear,'sensor_to_frontmost_body_mm':optical_to_front,
'full_body_stop_sensor_window_mm':whole_body_stop_window,
'full_body_stop_50mm_margin_sensor_window_mm':protected_finish_stop_window,
'braking_displacement_after_60mm_detection_for_50mm_margins_mm':[protected_finish_stop_window[0]-60,protected_finish_stop_window[1]-60],
'competition_width_pass':wheel_width_envelope<=200,'competition_length_pass':bracket_front-rear<=300,
'competition_height_MODEL_ONLY_pass':model_bounds[1][2]<=150,'min_side_clearance_pass':clearance>=2,
'model_qtr_standoff_positive':standoff>0,'model_caster_shim_positive':caster_shim>0}
assert all(res[k] for k in ['competition_width_pass','competition_length_pass','competition_height_MODEL_ONLY_pass','min_side_clearance_pass','model_qtr_standoff_positive','model_caster_shim_positive'])
out=Path(__file__).resolve().parent/'geometry_checks.json'
out.write_text(json.dumps(res,indent=2))
for k,v in res.items():print(k,v)
