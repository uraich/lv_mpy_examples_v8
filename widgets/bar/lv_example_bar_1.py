#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

bar1 = lv.bar(lv.scr_act())
bar1.set_size(200, 20)
bar1.center()
bar1.set_value(70, lv.ANIM.OFF)

