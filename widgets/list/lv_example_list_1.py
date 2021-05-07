#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def event_handler(evt):
    print("Clicked")
    code = evt.get_code()
    obj = lv.btn.__cast__(e.get_target())
    if code == lv.EVENT.CLICKED:
            print("Clicked: list1." + list1.get_btn_text(obj))

# Create a list
list1 = lv.list(lv.scr_act())
list1.set_size(180, 220)
list1.center()

# Add buttons to the list
list1.add_text("File")
list1.add_btn(lv.SYMBOL.FILE, "New",event_handler)
#list1.add_btn(lv.SYMBOL.DIRECTORY, "Open", event_handler)
#list1.add_btn(lv.SYMBOL.SAVE, "Save", event_handler)
#list1.add_btn(lv.SYMBOL.CLOSE, "Delete", event_handler)
#list1.add_btn(lv.SYMBOL.EDIT, "Edit", event_handler)
list1.add_text("Connectivity")
#list1.add_btn(lv.SYMBOL.BLUETOOTH, "Bluetooth", event_handler)
#list1.add_btn(lv.SYMBOL.GPS, "Navigation", event_handler)
#list1.add_btn(lv.SYMBOL.USB, "USB", event_handler)
#list1.add_btn(lv.SYMBOL.BATTERY_FULL, "Battery", event_handler)
list1.add_text("Exit")
#list1.add_btn(lv.SYMBOL.OK, "Apply", event_handler)
#list1.add_btn(LV_SYMBOL.CLOSE, "Close", event_handler)

