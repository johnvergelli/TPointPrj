from TPoint import TPoint


class TLine():
    def __init__(self, name, points=None):
        self.name = name
        if points is None:
            self.points = []

    def __getitem__(self, item):
        return self.points[item]

    def add_point(self):
        """
        Prompts the user for the data with which to create a new TPoint;
        then add it to the timeline.
        """
        print("Add a new point to the timeline:")
        date = input("Enter date in yyyy/mm/dd format:")
        if("-" in date):
            year, month, day = date.split("-")
        else:
            year, month, day = date.split("/")
        narrative = input("Enter narrative:")
        keywords = input("Enter keywords separated by commas:")
        self.points.append(TPoint(year, month, day, narrative, keywords))
        print("Time point added.")

    def filter_by_year(self, y):
        if(type(y) != int):
            y = int(y)
        return_list = []
        for tp in self:
            if int(tp.year) == y:
                return_list.append(tp)
        return return_list

    def filter_by_kw(self, kw):
        return_list = []
        for tp in self:
            if kw in tp.keywords:
                return_list.append(tp)
        return return_list
