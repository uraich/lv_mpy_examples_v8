#!/opt/bin/lv_micropython -i
import sys
import lvgl as lv
import display_driver

try:
    print("LV_RES: ",lv.RES)
except:
    print("lv.RES is not defined")

try:
    print("LV_ALIGN: ",lv.ALIGN)
except:
    print("lv.ALIGN is not defined")

try:
    print("LV_ALIGN: ",lv.DIR)
except:
    print("lv.DIR is not defined")
    
try:
    print("LV_FONT_SUBPX: ",lv.FONT_SUBPX)
except:
    print("lv.FONT_SUBPX is not defined")

try:
    print("LV_TEXT_CMD_STATE: ",lv.TEXT_CMD_STATE)
except:
    print("lv.TEXT_CMD_STATE is not defined")

try:
    print("LV_STYLE_RES: ",lv.STYLE_RES)
except:
    print("lv.STYLE_RES is not defined")

try:
    print("LV_FS_RES: ",lv.FS_RES)
except:
    print("lv.FS_RES is not defined")

try:
    print("LV_FS_MODE: ",lv.FS_MODE)
except:
    print("lv.FS_MODE is not defined")

try:
    print("LV_IMG_CF: ",lv.IMG_CF)
except:
    print("lv.IMG_CF is not defined")

try:
    print("LV_IMG_SRC: ",lv.IMG_SRC)
except:
    print("lv.IMG_SRC is not defined")

try:
    print("LV__DRAW_MASK_RES: ",lv._DRAW_MASK_RES)
except:
    print("lv._DRAW_MASK_RES is not defined")

try:
    print("LV_METER_INDICATOR_TYPE: ",lv.METER_INDICATOR_TYPE)
except:
    print("lv.METER_INDICATOR_TYPE is not defined")

try:
    print("LV_METER_DRAW_PART: ",lv.METER_DRAW_PART)
except:
    print("lv.METER_DRAW_PART is not defined")

try:
    print("LV_GRIDNAV_CTRL: ",lv.GRIDNAV_CTRL)
except:
    print("lv.GRIDNAV_CTRL is not defined")
