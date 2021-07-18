#!/opt/bin/lv_mp -i
import time
import lvgl as lv
import display_driver

obj_width = 120
obj_height = 200

def set_width(obj, v):
    # obj = lv.obj.__cast__(a.user_data)
    obj.set_width(v)


def set_height(obj, v):
    # obj = lv.obj.__cast__(a.user_data)
    obj.set_height(v)


def event_handler(e):
    obj = e.get_target()
    
    if obj == btn :
        reverse = btn.has_state(lv.STATE.CHECKED)
        lv.anim_timeline_set_reverse(anim_timeline,reverse)
        lv.anim_timeline_start(anim_timeline)
    elif obj == slider:
        progress = slider.get_value()
        lv.anim_timeline_set_progress(anim_timeline, progress)


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
btn.align(lv.ALIGN.BOTTOM_LEFT, 20, -20)

slider = lv.slider(par)
slider.add_event_cb(event_handler, lv.EVENT.VALUE_CHANGED, None)
slider.add_flag(lv.obj.FLAG.IGNORE_LAYOUT)
slider.align(lv.ALIGN.BOTTOM_RIGHT, -20, -20)
slider.set_range(0, 65535)

obj1 = lv.obj(par)
obj1.set_size(obj_width, obj_height)

obj2 = lv.obj(par)
obj2.set_size(obj_width, obj_height)

obj3 = lv.obj(par)
obj3.set_size(obj_width, obj_height)


# obj1 
a1 = lv.anim_t()
a1.init()
a1.set_values(0, obj_width)
a1.set_early_apply(False)
a1.set_custom_exec_cb(lambda a,v: set_width(obj1,v))
a1.set_path_cb(lv.anim_t.path_overshoot)
a1.set_time(300)
#a1.user_data = obj1

a2 = lv.anim_t()
a2.init()
a2.set_values(0, obj_height)
a2.set_early_apply(False)
a2.set_custom_exec_cb(lambda a,v: set_height(obj1,v))
a2.set_path_cb(lv.anim_t.path_ease_out)
a2.set_time(300)
#a2.user_data = obj1

# obj2 
a3=lv.anim_t()
a3.init()
a3.set_values(0, obj_width)
a3.set_early_apply(False)
a3.set_custom_exec_cb(lambda a,v: set_width(obj2,v))
a3.set_path_cb(lv.anim_t.path_overshoot)
a3.set_time(300)
#a3.user_data = obj2

a4 = lv.anim_t()
a4.init()
a4.set_values(0, obj_height)
a4.set_early_apply(False)
a4.set_custom_exec_cb(lambda a,v: set_height(obj2,v))
a4.set_path_cb(lv.anim_t.path_ease_out)
a4.set_time(300)
#a4.user_data = obj2

# obj3 
a5 = lv.anim_t()
a5.init()
a5.set_values(0, obj_width)
a5.set_early_apply(False)
a5.set_custom_exec_cb(lambda a,v: set_width(obj3,v))
a5.set_path_cb(lv.anim_t.path_overshoot)
a5.set_time(300)
#a5.user_data = obj3

a6 = lv.anim_t()
a6.init()
a6.set_values(0, obj_height)
a6.set_early_apply(False)
a6.set_custom_exec_cb(lambda a,v: set_height(obj3,v))
a6.set_path_cb(lv.anim_t.path_ease_out)
a6.set_time(300)
#a6.user_data = obj3
               
# Create anim timeline 
anim_timeline = lv.anim_timeline_create()
lv.anim_timeline_add(anim_timeline, 0, a1)
lv.anim_timeline_add(anim_timeline, 0, a2)
lv.anim_timeline_add(anim_timeline, 200, a3)
lv.anim_timeline_add(anim_timeline, 200, a4)
lv.anim_timeline_add(anim_timeline, 400, a5)
lv.anim_timeline_add(anim_timeline, 400, a6)


