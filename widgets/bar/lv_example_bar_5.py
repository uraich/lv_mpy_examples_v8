#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
#
# Bar with LTR and RTL base direction
#

bar_ltr = lv.bar(lv.scr_act())
bar_ltr.set_size(200, 20)
bar_ltr.set_value(70, lv.ANIM.OFF)
bar_ltr.align(lv.ALIGN.CENTER, 0, -30)

bar_rtl = lv.bar(lv.scr_act())
bar_rtl.set_base_dir(lv.BIDI_DIR.RTL)
bar_rtl.set_size(200, 20)
bar_rtl.set_value(70, lv.ANIM.OFF)
bar_rtl.align(lv.ALIGN.CENTER, 0, 30)

