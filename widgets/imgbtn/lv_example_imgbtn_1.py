#!/opt/bin/lv_micropython -i
import sys
import lvgl as lv
import display_driver
from imagetools import get_png_info, open_png

# Register PNG image decoder
decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

# Create an image from the png file
try:
    with open('../../assets/imgbtn_left.png','rb') as f:
        imgbtn_left_data = f.read()
except:
    print("Could not find imgbtn_left.png")
    sys.exit()
    
imgbtn_left_dsc = lv.img_dsc_t({
  'data_size': len(imgbtn_left_data),
  'data': imgbtn_left_data 
})

try:
    with open('../../assets/imgbtn_mid.png','rb') as f:
        imgbtn_mid_data = f.read()
except:
    print("Could not find imgbtn_mid.png")
    sys.exit()
    
imgbtn_mid_dsc = lv.img_dsc_t({
  'data_size': len(imgbtn_mid_data),
  'data': imgbtn_mid_data 
})

try:
    with open('../../assets/imgbtn_right.png','rb') as f:
        imgbtn_right_data = f.read()
except:
    print("Could not find imgbtn_right.png")
    sys.exit()
    
imgbtn_right_dsc = lv.img_dsc_t({
  'data_size': len(imgbtn_right_data),
  'data': imgbtn_right_data 
})

# Create a transition animation on width transformation and recolor.
    static lv_style_prop_t tr_prop[] = {LV_STYLE_TRANSFORM_WIDTH, LV_STYLE_IMG_RECOLOR_OPA, 0};
    static lv_style_transition_dsc_t tr;
    lv_style_transition_dsc_init(&tr, tr_prop, lv_anim_path_linear, 200, 0);

    static lv_style_t style_def;
    lv_style_init(&style_def);
    lv_style_set_text_color(&style_def, lv_color_white());
    lv_style_set_transition(&style_def, &tr);

    /*Darken the button when pressed and make it wider*/
    static lv_style_t style_pr;
    lv_style_init(&style_pr);
    lv_style_set_img_recolor_opa(&style_pr, LV_OPA_30);
    lv_style_set_img_recolor(&style_pr, lv_color_black());
    lv_style_set_transform_width(&style_pr, 20);

    /*Create an image button*/
    lv_obj_t * imgbtn1 = lv_imgbtn_create(lv_scr_act());
    lv_imgbtn_set_src(imgbtn1, LV_IMGBTN_STATE_RELEASED, &imgbtn_left, &imgbtn_mid, &imgbtn_right);
    lv_obj_add_style(imgbtn1, &style_def, 0);
    lv_obj_add_style(imgbtn1, &style_pr, LV_STATE_PRESSED);

    lv_obj_align(imgbtn1, LV_ALIGN_CENTER, 0, 0);

    /*Create a label on the image button*/
    lv_obj_t * label = lv_label_create(imgbtn1);
    lv_label_set_text(label, "Button");
    lv_obj_align(label, LV_ALIGN_CENTER, 0, -4);
}

