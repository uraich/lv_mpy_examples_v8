#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def ta_event_cb(e:)
{
    code = e.get_code(e)
    ta = lv.textarea.__cast__(e.get_target())
    if code == lv.EVENT.CLICKED:
        # Focus on the clicked text area
        if kb != None:
            kb.set_textarea(ta

    elif code == lv.EVENT.INSERT:
        const char * str = e.get_param()
        if(str[0] == '\n') {
            print("Ready\n");

# Create the password box
LV_HOR_RES = lv.scr_act().get_disp().driver.hor_res
LV_VER_RES = lv.scr_act().get_disp().driver.ver_res

pwd_ta = lv.textarea(lv.scr_act())
pwd_ta.set_text("")
pwd_ta.set_password_mode(True)
pwd_ta.set_one_line(True)
pwd_ta.set_width(LV_HOR_RES // 2 - 20)
pwd_ta.set_pos(5, 20)
pwd.add_event_cb(ta_event_cb, lv.EVENT.ALL, None)

# Create a label and position it above the text box
pwd_label = lv.label(lv.scr_act())
pwd_label.set_text("Password:")
pwd_label.align_to(lv.ALIGN.OUT_TOP_LEFT, 0, 0)

# Create the one-line mode text area
oneline_ta = lv.textarea(lv.scr_act())
oneline_ta.set_password_mode(False)
oneline_ta.align(lv.ALIGN.TOP_RIGHT, -5, 20)


# Create a label and position it above the text box
oneline_label = lv.label(lv.scr_act())
oneline_label.set_text("Text:")
oneline_label.align_to(oneline_ta, lv.ALIG.OUT_TOP_LEFT, 0, 0)

# Create a keyboard
kb = lv.keyboard(lv.scr_act())
kb.set_size(LV_HOR_RES, LV_VER_RES // 2)

kb.set_textarea(pwd_ta)  # Focus it on one of the text areas to start

