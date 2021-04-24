#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
import time

# Create an Arc
arc = lv.arc(lv.scr_act())
arc.set_end_angle(200)
arc.set_size(150, 150)
arc.center()



