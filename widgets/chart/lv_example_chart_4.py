#!/opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver
from lv_colors import lv_colors

def event_cb(e):
    code = e.get_code()
    chart = e.get_target()

    if code == lv.EVENT.VALUE_CHANGED:
        chart.invalidate()

    if code == lv.EVENT.REFR_EXT_DRAW_SIZE:
        p = lv.C_Pointer()
        p.ptr_val = e.get_param()
        print("s: ",p.int_val)
        # s = e.get_param()
        # *s = max(*s, 20)

    elif code == lv.EVENT.DRAW_POST_END:
        id = lv.chart.get_pressed_point(chart)
        if id == lv.CHART_POINT.NONE:
            return
        print("Selected point ", id)

        ser = lv.chart.get_series_next(chart,None)
        '''
        while ser: 
            p = lv.point_t()
            chart.get_point_pos_by_id(ser, id, p)
            print("id: ",id)
            lv_coord_t * y_array = lv_chart_get_array(chart, ser);
            lv_coord_t value = y_array[id];

            char buf[16];
            lv_snprintf(buf, sizeof(buf), LV_SYMBOL_DUMMY"$%d", value);
        '''
        value = ser1_p[id]
        buf = lv.SYMBOL.DUMMY + "$" + str(value)
        draw_rect_dsc = lv.draw_rect_dsc_t()
        draw_rect_dsc.init()
        draw_rect_dsc.bg_color = lv_colors.BLACK
        draw_rect_dsc.bg_opa = lv.OPA._50
        draw_rect_dsc.radius = 3
        draw_rect_dsc.bg_img_src = buf;
        draw_rect_dsc.bg_img_recolor = lv_colors.WHITE
        
        a = lv.area_t()
        a.x1 = chart.coords.x1 + p.x - 20
        a.x2 = chart.coords.x1 + p.x + 20
        a.y1 = chart.coords.y1 + p.y - 30
        a.y2 = chart.coords.y1 + p.y - 10
        
        clip_area = lv_area_t.cast(e.get_param())
        lv.draw_rect(a, clip_area, draw_rect_dsc)
        
        # ser = lv_chart_get_series_next(chart, ser)

# 
# Add ticks and labels to the axis and demonstrate scrolling
#

# Create a chart
chart = lv.chart(lv.scr_act())
chart.set_size(200, 150)
chart.center()

chart.add_event_cb(event_cb, lv.EVENT.ALL, None)
chart.refresh_ext_draw_size()

# Zoom in a little in X
chart.set_zoom_x(800)

# Add two data series
ser1 = chart.add_series(lv.palette_main(lv.PALETTE.RED), lv.chart.AXIS.PRIMARY_Y)
ser2 = chart.add_series(lv.palette_main(lv.PALETTE.GREEN), lv.chart.AXIS.PRIMARY_Y)

ser1_p = []
ser2_p = []
series = [ser1_p,ser2_p]

for i in range(10):
    ser1_p.append(lv.rand(60,90))
    ser2_p.append(lv.rand(10,40))
ser1.points = ser1_p
ser2.points = ser2_p


