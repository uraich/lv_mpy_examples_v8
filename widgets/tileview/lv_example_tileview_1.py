#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

#
# Create a 2x2 tile view and allow scrolling only in an "L" shape.
# Demonstrate scroll chaining with a long list that
# scrolls the tile view when it cant't be scrolled further.
#
tv = lv.tileview(lv.scr_act())

# Tile1: just a label
tile1 = tv.add_tile(0, 0, lv.DIR.BOTTOM)
label = lv.label(tile1)
label.set_text("Scroll down")
label.center()

# Tile2: a button
tile2 = tv.add_tile(0, 1, lv.DIR.TOP | lv.DIR.RIGHT)

btn = lv.btn(tile2)

label = lv.label(btn)
label.set_text("Scroll up or right")

btn.set_size(lv.SIZE.CONTENT, lv.SIZE.CONTENT)
btn.center()

# Tile3: a list
tile3 =  tv.add_tile(1, 1, lv.DIR.LEFT)
list = lv.list(tile3)
list.set_size(lv.pct(100), lv.pct(100))

list.add_btn(None, "One", None);
list.add_btn(None, "Two", None);
list.add_btn(None, "Three", None);
list.add_btn(None, "Four", None);
list.add_btn(None, "Five", None);
list.add_btn(None, "Six", None);
list.add_btn(None, "Seven", None);
list.add_btn(None, "Eight", None);
list.add_btn(None, "Nine", None);
list.add_btn(None, "Ten", None);

