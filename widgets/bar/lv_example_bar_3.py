#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver
from lv_colors import lv_colors

LV_ANIM_REPEAT_INFINITE = -1

def set_temp(bar, temp):
    bar.set_value(temp, lv.ANIM.ON)

#
# A temperature meter example
#


style_indic = lv.style_t()

style_indic.init()
style_indic.set_bg_opa(lv.OPA.COVER)
style_indic.set_bg_color(lv_colors.RED)
style_indic.set_bg_grad_color(lv_colors.BLUE)
style_indic.set_bg_grad_dir(lv.GRAD_DIR.VER)

bar = lv.bar(lv.scr_act())
bar.add_style(style_indic, lv.PART.INDICATOR)
bar.set_size(20, 200)
bar.center()
bar.set_range(-20, 40)

a = lv.anim_t()
a.init()
a.set_time(3000)
a.set_playback_time(3000)
a.set_var(bar)
a.set_values(-20, 40)
a.set_repeat_count(LV_ANIM_REPEAT_INFINITE)
a.set_custom_exec_cb(lambda a, val: set_temp(bar,val))
lv.anim_t.start(a)

