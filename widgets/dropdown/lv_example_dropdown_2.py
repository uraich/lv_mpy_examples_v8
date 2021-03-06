#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver

#
# Create a drop down, up, left and right menus
#

opts = "\n".join([
    "Apple\n"
    "Banana\n"
    "Orange\n"
    "Melon\n"
    "Grape\n"
    "Raspberry"])

dd = lv.dropdown(lv.scr_act())
dd.set_options_static(opts)
dd.align(lv.ALIGN.TOP_MID, 0, 10)
dd = lv.dropdown(lv.scr_act())
dd.set_options_static(opts)
dd.set_dir(lv.DIR.BOTTOM)
dd.set_symbol(lv.SYMBOL.UP)
dd.align(lv.ALIGN.BOTTOM_MID, 0, -10)

dd = lv.dropdown(lv.scr_act())
dd.set_options_static(opts)
dd.set_dir(lv.DIR.RIGHT)
dd.set_symbol(lv.SYMBOL.RIGHT)
dd.align(lv.ALIGN.LEFT_MID, 10, 0)

dd = lv.dropdown(lv.scr_act())
dd.set_options_static(opts)
dd.set_dir(lv.DIR.LEFT)
dd.set_symbol(lv.SYMBOL.LEFT)
dd.align(lv.ALIGN.RIGHT_MID, -10, 0)


