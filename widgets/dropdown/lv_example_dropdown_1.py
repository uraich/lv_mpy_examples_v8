#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def event_handler(e):
    code = e.get_code()
    obj = lv.dropdown.__cast__(e.get_target())
    if code == lv.EVENT.VALUE_CHANGED: 
        option = " "*10 # should be large enough to store the option
        obj.get_selected_str(option, len(option))
        # .strip() removes trailing spaces
        print("Option: \"%s\"" % option.strip())

# Create a normal drop down list
dd = lv.dropdown(lv.scr_act())
dd.set_options("\n".join([
    "Apple\n"
    "Banana\n"
    "Orange\n"
    "Cherry\n"
    "Grape\n"
    "Raspberry\n"
    "Melon\n"
    "Orange\n"
    "Lemon\n"
    "Nuts\n"]))

dd.align(lv.ALIGN.TOP_MID, 0, 20)
dd.add_event_cb(event_handler, lv.EVENT.ALL, None)

