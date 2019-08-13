def convert_to_dict(obj):
    # add obj metadata to the dictionary:
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__,
    }
    obj_dict.update(obj.__dict__)
    return obj_dict


def convert_to_obj(d):
    if "__class__" in d:
        class_name = d.pop("__class__")
        module_name = d.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        obj = class_(**d)
    else:
        obj = d
    return obj


testdata1 = [
    "1882,1,30,Franklin Roosevelt born.",
    "1880,12,31,George C. Marshall born.",
    "1889,4,20,Adolf Hitler born",
    "1905,3,19,Albert Speer born",
    "1878,12,18,Josef Stalin born",
    "1882,10,2,Boris Shaposhnikov born",
    "1874,11,30,Winston Churchill born",
    "1892,4,13, Arthur ('Bomber') Harris born",
]
