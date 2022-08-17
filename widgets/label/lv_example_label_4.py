#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

def add_mask_event_cb(e) :

    code = e.get_code()
    obj = e.get_target()
    mask_map = e.get_user_data()
    if code == LV_EVENT_COVER_CHECK :
        lv_event_set_cover_res(e, LV_COVER_RES_MASKED)
    elsif code == LV_EVENT_DRAW_MAIN_BEGIN) 
        lv_draw_mask_map_init(&m, &obj->coords, mask_map)
        mask_id = lv_draw_mask_add(&m, NULL)
    elsif code == LV_EVENT_DRAW_MAIN_END
        lv_draw_mask_free_param(&m)
        lv_draw_mask_remove_id(mask_id)

#
# Draw label with gradient color
#

# Create the mask of a text by drawing it to a canvas
    mask_map = [MASK_WIDTH * MASK_HEIGHT];

# Create a "8 bit alpha" canvas and clear it
canvas = lv.canvas(lv.scr_act())
canvas.set_buffer(mask_map, MASK_WIDTH, MASK_HEIGHT, lv.IMG_CF_ALPHA_8BIT)
canvas_fill_bg(lv.color_black(), LV_OPA_TRANSP)

# Draw a label to the canvas. The result "image" will be used as mask
lv_draw_label_dsc_t label_dsc;
lv_draw_label_dsc_init(&label_dsc);
label_dsc.color = lv_color_white();
label_dsc.align = LV_TEXT_ALIGN_CENTER;
lv_canvas_draw_text(canvas, 5, 5, MASK_WIDTH, &label_dsc, "Text with gradient");

# The mask is reads the canvas is not required anymore
lv_obj_del(canvas);

# Create an object from where the text will be masked ou.
# Now it's a rectangle with a gradient but it could be an image too
    lv_obj_t * grad = lv_obj_create(lv_scr_act());
    lv_obj_set_size(grad, MASK_WIDTH, MASK_HEIGHT);
    lv_obj_center(grad);
    lv_obj_set_style_bg_color(grad, lv_color_hex(0xff0000), 0);
    lv_obj_set_style_bg_grad_color(grad, lv_color_hex(0x0000ff), 0);
    lv_obj_set_style_bg_grad_dir(grad, LV_GRAD_DIR_HOR, 0);
    lv_obj_add_event_cb(grad, add_mask_event_cb, LV_EVENT_ALL, mask_map);

