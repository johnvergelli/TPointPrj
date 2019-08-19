import json
from TPoint import TPoint
from util_step1 import convert_to_obj
# from util_step1 import convert_to_dict


def filter(tl, kw):
    filtered_list = []
    for tp in tl:
        if kw in tp.keywords:
            filtered_list.append(tp)
    return filtered_list


def main():
    timeline = []
    infamy = TPoint(1941, 12, 7, "Japan bombs Pearl Harbor", "Yamamoto")
    infamy.keywords = "WWII"
    infamy.keywords = "Pacific"
    barbarossa = TPoint(1941, 6, 22, "Germany invades USSR (Operation Barbarossa)")
    barbarossa.keywords = "WWII"
    barbarossa.keywords = "Europe"
    barbarossa.keywords = "Eastern Front"
    valkyrie = TPoint(1944, 7, 20, "Failed assassination attempt on Hitler")
    valkyrie.keywords = "Europe"
    timeline.append(infamy)
    timeline.append(barbarossa)
    timeline.append(valkyrie)

    json_string = json.dumps([tp.to_dict() for tp in timeline], indent=4)
    # print(f"json_string: {json_string}")

    with open("data.json", "w") as outfile:
        outfile.write(json_string)

    tl2 = json.loads(json_string, object_hook=convert_to_obj)

    sublist = filter(tl2, "Europe")
    for tp in sublist:
        print(tp)

    '''
    s1 = json.dumps(d1, indent=4)
    print(f"s1 | {s1}")
    print("-------------------------------------------------------------------")
    dejavu = json.loads(s1, object_hook=convert_to_obj)
    print(f"type: {type(dejavu)} | {dejavu}")
    '''


if __name__ == "__main__":
    main()

print("Exiting.")
'''
timeline = []
for datum in testdata1:
    templist = datum.split(",")
    timeline.append(TPoint(*templist))
timeline.sort()
for tl in timeline:
    print(tl)
--------------------------------------------------------------------------------
deadline = datetime(2019, 9, 1)
today = datetime.now()
print(f"time left: {deadline - today}")
john = TPoint(1960, 8, 21, "John Vergelli birthday")
tempstr = john.as_csv_str()
print(f"tempstr: {tempstr}")
print(f"type(tempstr): {type(tempstr)}")
with open("tempdata.txt", "w") as outfile:
    outfile.write(tempstr)
instring = ""
with open("tempdata.txt", "r") as infile:
    instring = infile.readline()
print(f"instring: {instring}")
templist = instring.split(",")
print(f"templist: {templist}")
j2 = TPoint(*templist)
print(f"j2: {j2}")
'''
