#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

# show symbol

panel = lv.obj(lv.scr_act())
label = lv.label(panel)
label.set_text(lv.SYMBOL.ENVELOPE)

label.align(lv.ALIGN.CENTER,0,0)
