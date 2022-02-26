#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

#
# Show customizing the circular scrolling animation of a label with `LV_LABEL_LONG_SCROLL_CIRCULAR`
# long mode.
#

animation_template = lv.anim_t()
label_style = lv.style_t()

animation_template.init()
animation_template.set_delay(1000)           # Wait 1 second to start the first scroll
animation_template.set_repeat_delay(3000)    # Repeat the scroll 3 seconds after the label scrolls back to the initial position

# initialize the label style with the animation template

label_style.init()
label_style.set_anim(animation_template)

label1 = lv.label(lv.scr_act())
label1.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)       # Circular scroll
label1.set_width(150)
label1.set_text("It is a circularly scrolling text. ")
label1.align(lv.ALIGN.CENTER, 0, 40)
label1.add_style(label_style, lv.STATE.DEFAULT)           # Add the style to the label

