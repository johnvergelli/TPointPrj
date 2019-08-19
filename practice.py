import json
from expert import *


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


e1 = Expert("John", "Vergelli", "7-4416", ["Biometrics", "RT", "Secure Flight", "Vetting"])
print(e1)

with open("data.json", "w") as out_file:
    json.dump(e1, out_file, default=convert_to_dict, indent=4, sort_keys=True)

with open("data.json", "r") as in_file:
    e2 = json.load(in_file, object_hook=convert_to_obj)
print(e2)

print("Exiting.")


# print(data_str)
# with open("data.json", "w") as out_file:
#    out_file.write(data_str)
