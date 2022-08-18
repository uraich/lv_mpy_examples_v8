#!/opt/bin/lv_micropython -i
import sys
import lvgl as lv
import display_driver

#
# Open a video from a file
#

# birds.mp4 is downloaded from http://www.videezy.com (Free Stock Footage by Videezy!)
# https://www.videezy.com/abstract/44864-silhouettes-of-birds-over-the-sunset
player = lv.ffmpeg_player(lv.scr_act())
player.player_set_src("birds.mp4")
#  lv_ffmpeg_player_set_src(player, "/opt/ucc/micros/esp32/lvgl/simulator-V8/lvgl/examples/libs/ffmpeg/birds.mp4");
player.player_set_auto_restart(True)
print("LV_GRIDNAV_CTRL: ",lv.GRIDNAV_CTRL)
print("LV_FFMPEG_PLAYER_CMD: ",lv.FFMPEG_PLAYER_CMD)
#cmd = lv.FFMPEG_PLAYER_CMD.START
player.player_set_cmd(0)
player.center()
