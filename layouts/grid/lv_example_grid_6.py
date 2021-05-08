#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

LV_GRID_TEMPLATE_LAST = 24576

#
# Demonstrate RTL direction on grid
#
col_dsc = [60, 60, 60, LV_GRID_TEMPLATE_LAST]
row_dsc = [40, 40, 40, LV_GRID_TEMPLATE_LAST]

# Create a container with grid
cont = lv.obj(lv.scr_act())
cont.set_size(300, 220)
cont.center()
cont.set_base_dir(lv.BIDI_DIR.RTL)
cont.set_grid_dsc_array(col_dsc, row_dsc)

for i in range(9):
    col = i % 3
    row = i // 3

    obj = lv.obj(cont)
    # Stretch the cell horizontally and vertically too
    # Set span to 1 to make the cell 1 column/row sized
    obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, col, 1,
                      lv.GRID_ALIGN.STRETCH, row, 1);
    
    label = lv.label(obj)
    label.set_text("{:d},{:d}".format(col, row))
    label.center()

