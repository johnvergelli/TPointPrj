import json
import pathlib
# from TPoint import TPoint
from TLine import TLine
from util_step1 import convert_to_obj
# from util_step1 import convert_to_dict


def setup(tl):
    if type(tl) is not TLine:
        raise TypeError("setup() called with object not a Tline")
    print("***** Welcome to the TPoint/TLine testbed. *****")
    print(f"The cwd is: {pathlib.Path.cwd()}")
    loop = True
    while(loop is True):
        print("1. Open an existing file...")
        print("2. Start a new file...")
        choice = input("Enter 1 or 2: ")
        if(choice == "1"):
            filename = input("Enter existing file name: ")
            if(filename != ""):
                path = pathlib.Path.cwd() / filename
                with open(path, "r") as input_file:
                    tl.points = json.load(input_file, object_hook=convert_to_obj)
            loop = False
        elif(choice == "2"):
            print("Two")
            loop = False
        else:
            print("Invalid selection -- try again:")
    # print("test __getitem__ implementation in TLine:")
    # print(f"tl[1] -- {tl[1]}")
    return tl


def display(tl):
    n = 0
    for tp in tl.points:
        print(f"{n}. {tp}")
        n += 1


def save(tl):
    json_string = json.dumps([tp.to_dict() for tp in tl.points], indent=4)
    filename = input("Enter save file name: ")
    path = pathlib.Path.cwd() / filename
    with open(path, "w") as outfile:
        outfile.write(json_string)


def main_menu(tl):
    loop = True
    while(loop is True):
        print("***** Main Menu: *****")
        print("1. Display current timeline: ")
        print("2. Add point...")
        print("3. Save.")
        print("9. Quit.")
        choice = input("Enter your selection: ")
        if(choice == "1"):
            display(tl)
        if(choice == "2"):
            tl.add_point()
        if(choice == "3"):
            save(tl)
        if(choice == "9"):
            loop = False


def main():
    tl = TLine("test_article")
    print(f"Type of tl #1: {type(tl)}")
    tl = setup(tl)
    display(tl)
    main_menu(tl)


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
"""
tl = TLine("test")
tl.add_point()
tl.add_point()
tl.add_point()
for tp in tl:
    print(tp)
    print(tp.keywords)
family = tl.filter_by_kw("Family")
for tp in family:
    print(tp)
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
"""
'''
print("Add a time point: ")
loop = True
while(loop is True):
    print(f"Type of tl: {type(tl)}")
    tl.add_point()
    choice = input("Do you want to add another time point?")
    if(choice.lower() != "y" or choice.lower() != "yes"):
        loop = False
for tp in tl.points:
    print(tp)
'''
