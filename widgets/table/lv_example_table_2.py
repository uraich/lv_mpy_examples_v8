#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

ITEM_CNT = 200

def draw_event_cb(e):
    obj = lv.table.__cast__(e.get_target())
    dsc = lv_obj_draw_dsc_t.cast(e.get_param())
    # If the cells are drawn...
    if dsc.part == lv.PART.ITEMS:
        chk = obj.has_cell_ctrl(dsc.id, 0, lv.TABLE_CELL.CTRL_CUSTOM_1)

        rect_dsc = lv.draw_rect_dsc_t()
        rect_dsc.init()
'''
        if chk:
    
        rect_dsc.bg_color = chk ? lv_theme_get_color_primary(obj) : lv_palette_lighten(LV_PALETTE_GREY, 2);
        rect_dsc.radius = LV_RADIUS_CIRCLE;

        lv_area_t sw_area;
        sw_area.x1 = dsc->draw_area->x2 - 50;
        sw_area.x2 = sw_area.x1 + 40;
        sw_area.y1 =  dsc->draw_area->y1 + lv_area_get_height(dsc->draw_area) / 2 - 10;
        sw_area.y2 = sw_area.y1 + 20;
        lv_draw_rect(&sw_area, dsc->clip_area, &rect_dsc);

        rect_dsc.bg_color = lv_color_white();
        if(chk) {
            sw_area.x2 -= 2;
            sw_area.x1 = sw_area.x2 - 16;
        } else {
            sw_area.x1 += 2;
            sw_area.x2 = sw_area.x1 + 16;
        }
        sw_area.y1 += 2;
        sw_area.y2 -= 2;
        lv_draw_rect(&sw_area, dsc->clip_area, &rect_dsc);
    }
}

static void change_event_cb(lv_event_t * e)
{
    lv_obj_t * obj = lv_event_get_target(e);
    uint16_t col;
    uint16_t row;
    lv_table_get_selected_cell(obj, &row, &col);
    bool chk = lv_table_has_cell_ctrl(obj, row, 0, LV_TABLE_CELL_CTRL_CUSTOM_1);
    if(chk) lv_table_clear_cell_ctrl(obj, row, 0, LV_TABLE_CELL_CTRL_CUSTOM_1);
    else lv_table_add_cell_ctrl(obj, row, 0, LV_TABLE_CELL_CTRL_CUSTOM_1);
}

'''
#
# A very light-weighted list created from table
#

# Measure memory usage
mon1 = lv.mem_monitor_t()
mon1.mem_monitor()

t = lv.tick_get()

table = lv.table(lv.scr_act())

# Set a smaller height to the table. It'll make it scrollable
table.set_size(150, 200)

table.set_col_width(0, 150)
table.set_row_cnt(ITEM_CNT)  # Not required but avoids a lot of memory reallocation lv_table_set_set_value
table.set_col_cnt(1)

# Don't make the cell pressed, we will draw something different in the event
table.remove_style(None, lv.PART.ITEMS | lv.STATE.PRESSED)

for i in range(ITEM_CNT):
    table.set_cell_value(i, 0, "Item " * str(i), i + 1)

table.align(lv.ALIGN.CENTER, 0, -20);

# Add an event callback to to apply some custom drawing
# table.add_event_cb(draw_event_cb, lv.EVENT.DRAW_PART_END, None)
# table.add_event_cb(change_event_cb, lv.EVENT.VALUE_CHANGED, None)

mon2 = lv.mem_monitor_t()
lv..mem_monitor(mon2)

mem_used = mon1.free_size - mon2.free_size;

elaps = lv.tick_elaps(t)

label = lv.label(lv.scr_act())
label.set_text(str(ITEM_CNT) + " items were created in " + str(elaps) + " ms\n using " + str(mem_used) + "bytes of memory")

label.align(lv.ALIGN.BOTTOM_MID, 0, -10)

