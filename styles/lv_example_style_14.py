#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

# Will be called when the styles of the base theme are already added
# to add new styles
def new_theme_apply_cb(th, obj):

    if type(obj) == type(lv.btn()):
        obj.add_style(style_btn, 0)

def new_theme_init_and_set():

    # Initialize the styles
    style_btn = lv.style_t()
    style_btn.init()
    style_btn.set_bg_color(lv.palette_main(lv.PALETTE.GREEN))
    style_btn.set_border_color(lv.palette_darken(lv.PALETTE.GREEN, 3))
    style_btn.set_border_width(3)

    # Initialize the new theme from the current theme
    '''
    display = lv.scr_act().get_disp()
    th_act = display.get_theme()
    th_new = th_act
    # Set the parent theme ans the style applay callback for the new theme
    th_new.set_parent(th_act)
    # th_new.set_apply_cb(new_theme_apply_cb)

    # Assign the new theme the the current display
    lv.disp_t.set_theme(display, th_new)
    '''

    th_act = lv.theme_get_from_obj(lv.scr_act())
    th_new =th_act
    th_new.set_apply_cb(new_theme_apply_cb)
    # Activate this theme on default display
    lv.disp_get_default().set_theme(th_new)
    
# 
# Extending the current theme
#

btn = lv.btn(lv.scr_act())
btn.align(lv.ALIGN.TOP_MID, 0, 20)

label = lv.label(btn)
label.set_text("Original theme")

new_theme_init_and_set()

btn = lv.btn(lv.scr_act())
btn.align(lv.ALIGN.BOTTOM_MID, 0, -20)

label = lv.label(btn)
label.set_text("New theme")

