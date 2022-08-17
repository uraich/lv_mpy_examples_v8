#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver

# Define a message ID
MSG_INC            = 1
MSG_DEC            = 2
MSG_SET            = 3
MSG_UPDATE         = 4
MSG_UPDATE_REQUEST = 5

def value_handler(m):

    value = 10
    old_value = value
    id = m.get_id()
    if id == MSG_INC:
        if value < 100:
            value +=1
    elif id == MSG_DEC:
        if value > 0:
            value -=1
    elif id == MSG_SET:
        new_value = m.get_payload()
        print("value_handler: type of new_value: ",type(new_value))
        v = lv.C_Pointer()
        v = new_value
        print("value_handler: new value: {:d}".format(new_value.uint_val))
        value = new_value.uint_val
    elif id == MSG_UPDATE_REQUEST:
        v_ptr = lv.C_Pointer()
        v_ptr.uint_val = value
        lv.msg_send(MSG_UPDATE, v_ptr)
        
def btn_event_cb(e):

    btn = e.get_target()
    code = e.get_code()
    if code == lv.EVENT.CLICKED or code == lv.EVENT.LONG_PRESSED_REPEAT:
        if btn.get_index() == 0:      # rst object is the dec. button
            lv.msg_send(MSG_DEC, None)
        else :
            lv.msg_send(MSG_INC, None)

def label_event_cb(e):
    label = e.get_target()
    code = e.get_code(e)
    if code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg()
        if lv.msg_get_id(m) == MSG_UPDATE:
            v = m.get_payload()
            print("label_event: value: {:d}".format(v))
            label.set_text("{:d}%".format(v))

def slider_event_cb(e):
    slider = e.get_target()
    code = e.get_code()
    if code == lv.EVENT.VALUE_CHANGED:
        v = slider.get_value()
        # print("slider_event_cb: value: {:d}".format(v))
        v_ptr = lv.C_Pointer()
        v_ptr.uint_val = v
        # print("*v: {:d}".format(v_ptr.uint_val))
        lv.msg_send(MSG_SET, v_ptr)
        
    elif code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg()
        if m.get_id() == MSG_UPDATE:
            v = m.get_payload()
            slider.set_value(v, lv.ANIM.OFF)

lv.msg_subscribe(MSG_INC, value_handler, None)
lv.msg_subscribe(MSG_DEC, value_handler, None)
lv.msg_subscribe(MSG_SET, value_handler, None)
lv.msg_subscribe(MSG_UPDATE, value_handler, None)
lv.msg_subscribe(MSG_UPDATE_REQUEST, value_handler, None)

panel = lv.obj(lv.scr_act())
panel.set_size(250, lv.SIZE_CONTENT)
panel.center()
panel.set_flex_flow(lv.FLEX_FLOW.ROW)
panel.set_flex_align(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.START)

# Up button
btn = lv.btn(panel)
btn.set_flex_grow(1)
btn.add_event_cb(btn_event_cb, lv.EVENT.ALL, None)
label = lv.label(btn)
label.set_text(lv.SYMBOL.LEFT)
label.center()

# Current value
label = lv.label(panel)
label.set_flex_grow(2)
label.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)
label.set_text("?")
lv.msg_subscribe_obj(MSG_UPDATE, label, None)
label.add_event_cb(label_event_cb, lv.EVENT.MSG_RECEIVED, None)

# Down button
btn = lv.btn(panel)
btn.set_flex_grow(1)
btn.add_event_cb(btn_event_cb, lv.EVENT.ALL, None)
label = lv.label(btn)
label.set_text(lv.SYMBOL.RIGHT)
label.center()

# Slider
slider = lv.slider(panel)
slider.set_flex_grow(1)
slider.add_flag(lv.OBJ_FLAG_FLEX_IN_NEW_TRACK)
slider.add_event_cb(slider_event_cb, lv.EVENT.ALL, None)
lv.msg_subscribe_obj(MSG_UPDATE, slider, None)


# As there are new UI elements that don't know the system's state
# send an UPDATE REQUEST message which will trigger an UPDATE message with the current value
lv.msg_send(MSG_UPDATE_REQUEST, None)


