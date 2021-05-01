#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

cw = lv.colorwheel(lv.scr_act(), True)
cw.set_size(200, 200)
cw.center()

