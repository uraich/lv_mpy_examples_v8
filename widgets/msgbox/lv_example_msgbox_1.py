#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def event_cb(e):
    mbox = lv.msgbox.__cast__(e.get_current_target())
    print("Button " + mbox.get_active_btn_text() + " clicked")

btns = ["Apply", "Close", ""]

mbox1 = lv.msgbox(lv.scr_act(), "Hello", "This is a message box with two buttons.", btns, True)
mbox1.add_event_cb(event_cb, lv.EVENT.VALUE_CHANGED, None)
mbox1.center()

