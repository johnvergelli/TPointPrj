from TPoint import TPoint
from util_step1 import testdata1


def main():
    timeline = []
    for datum in testdata1:
        templist = datum.split(",")
        timeline.append(TPoint(*templist))
    timeline = timeline.sort(TPoint.__lt__)
    for tl in timeline:
        print(tl)


if __name__ == "__main__":
    main()

print("Exiting.")
'''
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
