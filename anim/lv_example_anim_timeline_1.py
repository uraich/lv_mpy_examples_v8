#!/opt/bin/lv_mp -i
import time
import lvgl as lv
import display_driver

def set_width(var, v):
    var.set_width(v)


def set_height(var, v):
    var.set_height(v)


def event_handler(e):
    print("event_handler")

    anim_timeline = [{"start_time" : 0,
                        "var" : obj1,
                        "exec_cb" : set_width,
                        "start_value" : 0,
                        "end_value" : obj_width,
                        "duration" : 300,
                        "path_cb" : lv.anim_t.path_overshoot},

                     {
                         "start_time" : 0,
                         "var" : obj1,
                         "exec_cb" : set_height,
                         "start_value" : 0,
                         "end_value" : obj_height,
                         "duration" : 300,
                         "path_cb" : lv.anim_t.path_ease_out},
                     {
                         "start_time" : 200,
                         "var" : obj2,
                         "exec_cb" :  set_width,
                         "start_value" : 0,
                         "end_value" : obj_width,
                         "duration" : 300,
                         "path_cb" : lv.anim_t.path_overshoot},
                     {
                         "start_time": 200,
                         "var" : obj2,
                         "exec_cb" : set_height,
                         "start_value" : 0,
                         "end_value:" : obj_height,
                         "duration" : 300,
                         "path_cb" : lv.anim_t.path_ease_out},
                     {
                         "start_time" : 400,
                         "var" : obj3,
                         "exec_cb" : set_width,
                         "start_value" : 0,
                         "end_value" : obj_width,
                         "duration" :  300,
                         "path_cb" :  lv.anim_t.path_overshoot},
                     {
                         "start_time" : 400,
                         "var" : obj3,
                         "exec_cb" :  set_height,
                         "start_value" : 0,
                         "end_value" : obj_height,
                         "duration" :  300,
                         "path_cb" : lv.anim_t.path_ease_out},
                     {
                         "start_time" : -1}]


    obj = e.get_target()

    if obj == btn:
        playback = btn.has_state(lv.STATE.CHECKED)
        lv.anim_timeline_t.start(anim_timeline,playback)

    elif obj == slider:
        progress = slider.get_value()
        lv.anim_timeline_t.set_progress(anim_timeline,progress)
            
#
# Create an animation timeline
#
par = lv.scr_act()
par.set_flex_flow(lv.FLEX_FLOW.ROW)
par.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)

btn = lv.btn(par)
btn.add_event_cb(event_handler, lv.EVENT.VALUE_CHANGED, None)
btn.add_flag(lv.obj.FLAG.IGNORE_LAYOUT)
btn.add_flag(lv.obj.FLAG.CHECKABLE)
btn.align(lv.ALIGN.BOTTOM_LEFT, 30, -18)

slider = lv.slider(par)
slider.add_event_cb(event_handler, lv.EVENT.VALUE_CHANGED, None)
slider.add_flag(lv.obj.FLAG.IGNORE_LAYOUT)
slider.align(lv.ALIGN.BOTTOM_RIGHT, -20, -20)
slider.set_range(0, 65535)

obj1 = lv.obj(par)
obj2 = lv.obj(par)
obj3 = lv.obj(par)

obj_width = obj1.get_style_width(0)
obj_height = obj1.get_style_height(0)

