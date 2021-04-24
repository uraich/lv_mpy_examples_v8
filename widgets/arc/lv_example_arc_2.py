#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver

#
# An `lv_timer` to call periodically to set the angles of the arc
#
def arc_loader(tim):
    a = 270
    a+=5;

    #arc.set_end_angle(t->user_data, a);

    if a >= 270 + 360:
        lv.timer.delete(tim)

def timer_cb(src):
    print(type(src))

#
# Create an arc which acts as a loader.
#

# Create an Arc
arc = lv.arc(lv.scr_act())
arc.set_bg_angles(0, 360)
arc.set_angles(270, 270)
arc.center()

# Create an `lv_timer` to update the arc.

timer = lv.timer_create_basic()
timer.set_period(500)
timer.set_cb(timer_cb())
  

