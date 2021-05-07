#!//opt/bin/lv_micropython -i
import time
import lvgl as lv
import display_driver

#
# Demonstrate flex grow.
#

cont = lv.obj(lv.scr_act())
cont.set_size(300, 220
cont.center()
cont.set_flex_flow(lv.FLEX_FLOW.ROW)

obj = lv.obj(cont)
obj.set_size(40, 40)           # Fix size

    obj = lv_obj_create(cont);
    lv_obj_set_height(obj, 40);
    lv_obj_set_flex_grow(obj, 1);           /*1 portion from the free space*/

    obj = lv_obj_create(cont);
    lv_obj_set_height(obj, 40);
    lv_obj_set_flex_grow(obj, 2);           /*2 portion from the free space*/

    obj = lv_obj_create(cont);
    lv_obj_set_size(obj, 40, 40);           /*Fix size. It is flushed to the right by the "grow" items*/
}

#endif
