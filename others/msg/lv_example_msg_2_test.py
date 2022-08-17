#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
from micropython import const
import sys

# Define a message ID
MSG_LOGIN_ATTEMPT = 1
MSG_LOG_OUT       = 2
MSG_LOGIN_ERROR   = 3
MSG_LOGIN_OK      = 4


def auth_manager(m):

    pin_act = m.get_payload()
    # pin_expected = m.get_user_data()
    # print("auth_manager: pin: {:d}".format(pin_expected))
    pin_expected = "hello"
    if pin_act == pin_expected:
        lv.msg_send(MSG_LOGIN_OK, None)
    else:
        lv.msg_send(MSG_LOGIN_ERROR, "Incorrect PIN")
        
def textarea_event_cb(e):
    ta = e.get_target()
    code = e.get_code()
    if code == lv.EVENT.READY:
        lv.msg_send(MSG_LOGIN_ATTEMPT, ta.get_text())
    elif code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg()
        id = m.msg_get_id()
        if id == MSG_LOGIN_ERROR:
            # If there was an error, clean the text area
            if len(lv.msg_get_payload(m)):
                   ta.set_text("")
        elif id == MSG_LOGIN_OK:
            ta.add_state(lv.STATE.DISABLED)
            ta.clear_state(lv.STATE.FOCUSED | lv.STATE.FOCUS_KEY)
        elif id == MSG_LOG_OUT:
            ta.set_text("");
            ta.clear_state(lv.STATE.DISABLED)

def log_out_event_cb(e):
    code = e.get_code()
    if code == lv.EVENT_CLICKED:
        lv.msg_send(MSG_LOG_OUT, None)
    elif code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg(e)
        btn = e.get_target()
        id = m.msg_get_id()
        if id == MSG_LOGIN_OK:
            btn.clear_state(lv.STATE.DISABLED)
        elif id == MSG_LOG_OUT:
            btn.add_state(lv.STATE.DISABLED)

def start_engine_msg_event_cb(e):

    m = e.get_msg()
    btn = e.get_target(e)
    id = m.get_id()
    if id == MSG_LOGIN_OK:
        btn.clear_state(lv.STATE.DISABLED)
    elif id == MSG_LOG_OUT:
        btn.add_state(lv.STATE.DISABLED)


def info_label_msg_event_cb(e):
    label = e.get_target(e)
    m = e.get_msg()
    id = m.get_id()
    if id ==  MSG_LOGIN_ERROR:
        label.set_text(m.get_payload())
        label.set_style_text_color(lv.palette_main(lv.PALETTE.RED), 0)
    elif id == MSG_LOGIN_OK:
        label.set_text("Login successful")
        label.set_style_text_color(lv.palette_main(lv.PALETTE.GREEN), 0)
    elif id == MSG_LOG_OUT:
        label.set_text("Logged out")
        label.set_style_text_color(lv.palette_main(lv.PALETTE.GREY), 0)

#
# Simple PIN login screen.
# No global variables are used, all state changes are communicated via messages.
def textarea_event_cb(e):
    ta = e.get_target()
    code = e.get_code()
    if code == lv.EVENT.READY:
        print("textarea_event_cb: Text in text area: ",ta.get_text())
        lv.msg_send(MSG_LOGIN_ATTEMPT, ta.get_text())
    elif code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg()
        id = m.get_id()
        if id == MSG_LOGIN_ERROR:
            # If there was an error, clean the text area
            # if len(m.get_payload()):
            ta.set_text("")
        elif id == MSG_LOGIN_OK:
            ta.add_state(lv.STATE.DISABLED)
            ta.clear_state(lv.STATE.FOCUSED | lv.STATE.FOCUS_KEY)
        elif id == MSG_LOG_OUT:
            ta.set_text("");
            ta.clear_state(lv.STATE.DISABLED)

def log_out_event_cb(e):
    code = e.get_code()
    if code == lv.EVENT.CLICKED:
        lv.msg_send(MSG_LOG_OUT, None)
    elif code == lv.EVENT.MSG_RECEIVED:
        m = e.get_msg()
        btn = e.get_target()
        id = m.get_id()
        if id == MSG_LOGIN_OK:
            btn.clear_state(lv.STATE.DISABLED)
        elif id == MSG_LOG_OUT:
            btn.add_state(lv.STATE.DISABLED)

def start_engine_msg_event_cb(e):

    m = e.get_msg()
    btn = e.get_target()
    id = m.get_id()
    if id == MSG_LOGIN_OK:
        btn.clear_state(lv.STATE.DISABLED)
    elif id == MSG_LOG_OUT:
        btn.add_state(lv.STATE.DISABLED)


def info_label_msg_event_cb(e):
    label = e.get_target()
    m = e.get_msg()
    id = m.get_id()
    if id ==  MSG_LOGIN_ERROR:
        label.set_text(m.get_payload())
        label.set_style_text_color(lv.palette_main(lv.PALETTE.RED), 0)
    elif id == MSG_LOGIN_OK:
        label.set_text("Login successful")
        label.set_style_text_color(lv.palette_main(lv.PALETTE.GREEN), 0)
    elif id == MSG_LOG_OUT:
        label.set_text("Logged out")
        label.set_style_text_color(lv.palette_main(lv.PALETTE.GREY), 0)


lv.msg_subscribe(MSG_LOGIN_ATTEMPT, auth_manager, None)

# Create a slider in the center of the display
ta = lv.textarea(lv.scr_act())
ta.set_pos(10, 10)
ta.set_width(200)
ta.set_one_line(True)
ta.set_password_mode(True)
ta.set_placeholder_text("The password is: hello")
ta.add_event_cb(textarea_event_cb, lv.EVENT.ALL, None)
lv.msg_subscribe_obj(MSG_LOGIN_ERROR, ta, None)
lv.msg_subscribe_obj(MSG_LOGIN_OK, ta, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, ta, None)

kb = lv.keyboard(lv.scr_act())
kb.set_textarea(ta)

# Create a log out button which will be active only when logged in
btn = lv.btn(lv.scr_act())
btn.set_pos(240, 10)
btn.add_event_cb(log_out_event_cb, lv.EVENT.ALL, None)
lv.msg_subscribe_obj(MSG_LOGIN_OK, btn, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, btn, None)

label = lv.label(btn);
label.set_text("LOG OUT")

# Create a label to show info
label = lv.label(lv.scr_act());
label.set_text("")
label.add_event_cb(info_label_msg_event_cb, lv.EVENT.MSG_RECEIVED, None)
label.set_pos(10, 60)
lv.msg_subscribe_obj(MSG_LOGIN_ERROR, label, None)
lv.msg_subscribe_obj(MSG_LOGIN_OK, label, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, label, None)

#Create button which will be active only when logged in
btn = lv.btn(lv.scr_act())
btn.set_pos(10, 80)
btn.add_event_cb(start_engine_msg_event_cb, lv.EVENT.MSG_RECEIVED, None)
btn.add_flag(lv.obj.FLAG.CHECKABLE)
lv.msg_subscribe_obj(MSG_LOGIN_OK, btn, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, btn, None)

label = lv.label(btn)
label.set_text("START ENGINE")

lv.msg_send(MSG_LOG_OUT, None)
kb = lv.keyboard(lv.scr_act())
kb.set_textarea(ta)

# Create a log out button which will be active only when logged in
btn = lv.btn(lv.scr_act())
btn.set_pos(240, 10)
btn.add_event_cb(log_out_event_cb, lv.EVENT.ALL, None)
lv.msg_subscribe_obj(MSG_LOGIN_OK, btn, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, btn, None)

label = lv.label(btn);
label.set_text("LOG OUT")

# Create a label to show info
label = lv.label(lv.scr_act());
label.set_text("")
label.add_event_cb(info_label_msg_event_cb, lv.EVENT.MSG_RECEIVED, None)
label.set_pos(10, 60)
lv.msg_subscribe_obj(MSG_LOGIN_ERROR, label, None)
lv.msg_subscribe_obj(MSG_LOGIN_OK, label, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, label, None)

#Create button which will be active only when logged in
btn = lv.btn(lv.scr_act())
btn.set_pos(10, 80)
btn.add_event_cb(start_engine_msg_event_cb, lv.EVENT.MSG_RECEIVED, None)
btn.add_flag(lv.obj.FLAG.CHECKABLE)
lv.msg_subscribe_obj(MSG_LOGIN_OK, btn, None)
lv.msg_subscribe_obj(MSG_LOG_OUT, btn, None)

label = lv.label(btn)
label.set_text("START ENGINE")

lv.msg_send(MSG_LOG_OUT, None)
