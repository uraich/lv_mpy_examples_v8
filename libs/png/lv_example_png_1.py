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
    with open('wink.png','rb') as f:
        png_data = f.read()
except:
    print("Could not find wink.png")
    sys.exit()

wink_argb = lv.img_dsc_t({
  'data_size': len(png_data),
  'data': png_data 
})

img = lv.img(lv.scr_act())
img.set_src(wink_argb)
img.center()
