#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

#
# Using the Arc style properties
#
style = lv.style_t()
style.init()

style.set_arc_color(lv.palette_main(lv.PALETTE.RED))
style.set_arc_width(4)

# Create an object with the new style
obj = lv.arc(lv.scr_act())
obj.add_style(style, 0)
obj.center()


