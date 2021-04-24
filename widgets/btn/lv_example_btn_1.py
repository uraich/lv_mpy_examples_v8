#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def event_handler(evt,source):
    code = evt.get_code()

    if code == lv.EVENT.CLICKED:
        if source == btn1:
            print("btn1 Clicked")
        else:
            print("btn2 Toggled")
    elif code == lv.EVENT.VALUE_CHANGED:
        print("Value changed seen")
        
log_level=["Trace", "Info", "Warning", "Error", "User"]
lv.log_register_print_cb(lambda level,filename,line,func,msg: print('LOG: %s, file: %s in %s, line %d: %s' % (log_level[level], filename, func, line, msg)))           

#lv.log_add("User","Hello")
# create a simple button
btn1 = lv.btn(lv.scr_act())

# attach the callback
btn1.add_event_cb(lambda evt: event_handler(evt,btn1),lv.EVENT.ALL, None)

btn1.align(lv.ALIGN.CENTER,0,-40)
label=lv.label(btn1)
label.set_text("Button")

# create a toggle button
btn2 = lv.btn(lv.scr_act())

# attach the callback
#btn2.add_event_cb(event_handler,lv.EVENT.VALUE_CHANGED,None)
btn2.add_event_cb(lambda evt: event_handler(evt,btn2),lv.EVENT.ALL, None)

btn2.align(lv.ALIGN.CENTER,0,40)
btn2.add_flag(lv.obj.FLAG.CHECKABLE)
btn2.set_height(lv.SIZE.CONTENT)

label=lv.label(btn2)
label.set_text("Toggle")
label.center()
