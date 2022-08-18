#!/opt/bin/lv_micropython -i
import lvgl as lv
import display_driver
#
# file: lv_example_fragment_1.c
# brief: Basic usage of obj fragment
#

def sample_container_del(e,manager):
    lv.fragment_manager_del(manager)

root = lv.obj(lv.scr_act())
root.set_size(lv.pct(100), lv.pct(100))
manager = lv.fragment_manager_create(None)
# Clean up the fragment manager before objects in containers got deleted

root.add_event_cb(lambda evt: sample_container_del(evt,manager), lv.EVENT.DELETE, None)

sample_cls = lv.fragment_class_t()
'''
fragment = lv.fragment(sample_cls, "Fragment");
manager.replace(fragment, root)

static void sample_fragment_ctor(lv_fragment_t * self, void * args)
{
    ((struct sample_fragment_t *) self)->name = args;
}

static lv_obj_t * sample_fragment_create_obj(lv_fragment_t * self, lv_obj_t * parent)
{
    lv_obj_t * label = lv_label_create(parent);
    lv_obj_set_style_bg_opa(label, LV_OPA_COVER, 0);;
    lv_label_set_text_fmt(label, "Hello, %s!", ((struct sample_fragment_t *) self)->name);
    return label;
}

static void sample_container_del(lv_event_t * e)
{
    lv_fragment_manager_t * manager = (lv_fragment_manager_t *) lv_event_get_user_data(e);
    lv_fragment_manager_del(manager);
}

#endif
'''
