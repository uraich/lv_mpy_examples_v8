#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

#
# Style a button from scratch
#

trans = lv.style_transition_dsc_t()
#props = [lv.STYLE.OUTLINE_WIDTH, lv.STYLE.OUTLINE_OPA, 0]
#trans.init(props,lv.anim_t.path_linear,300,0)

style = lv.style_t()
style.init()
style.set_outline_opa(lv.OPA.COVER)
style.set_outline_color(lv.palette_main(lv.PALETTE.BLUE))

style_pr = lv.style_t()
style_pr.init()
style_pr.set_outline_width(30)
style_pr.set_outline_opa(lv.OPA.TRANSP)
style_pr.set_transition(trans)

#
#    /*Init the default style*/
#    lv_style_set_radius(&style, 3);
#
#    lv_style_set_bg_opa(&style, LV_OPA_100);
#    lv_style_set_bg_color(&style, lv_color_blue());
#    lv_style_set_bg_grad_color(&style, lv_color_blue_darken_2());
#    lv_style_set_bg_grad_dir(&style, LV_GRAD_DIR_VER);
#
#    lv_style_set_border_opa(&style, LV_OPA_40);
#    lv_style_set_border_width(&style, 2);
#    lv_style_set_border_color(&style, lv_color_grey());
#
#    lv_style_set_shadow_width(&style, 8);
#    lv_style_set_shadow_color(&style, lv_color_grey());
#    lv_style_set_shadow_ofs_y(&style, 8);
#
#    lv_style_set_text_color(&style, lv_color_white());
#
#    lv_style_set_pad_all(&style, 10);
#    lv_style_set_pad_all(&style_pr, 40);

# Init the pressed style
style_pr.set_shadow_ofs_y(3)
style_pr.set_bg_color( lv.palette_darken(lv.PALETTE.BLUE, 2))
style_pr.set_bg_grad_color(lv.palette_darken(lv.PALETTE.BLUE,4))

btn1 = lv.btn(lv.scr_act())
#    lv_obj_remove_style(btn1, LV_PART_ANY, LV_STATE_ANY, NULL);
btn1.add_style(style, 0)
btn1.add_style(style_pr, lv.STATE.PRESSED)
btn1.set_size(lv.SIZE.CONTENT, lv.SIZE.CONTENT)
btn1.center()

label = lv.label(btn1)
label.set_text("Button")
label.center()

