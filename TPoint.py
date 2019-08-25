from datetime import datetime


class TPoint:
    """
    Instances of this class represent the facts about a particular event.
    This class is designed work with class TLine, which represents a timeline
    comprised of such events.
    """

    def __init__(self, year, month, day, narrative, keywords_string=""):
        if(type(year) != int):
            year = int(year)
        if(type(month) != int):
            month = int(month)
        if(type(day) != int):
            day = int(day)
        self.point = datetime(year, month, day)
        self.narrative = narrative
        self.keywords_string = keywords_string

    @property
    def year(self):
        return self.point.year

    @year.setter
    def year(self, new_year):
        self.point = self.point.replace(year=new_year)

    @property
    def month(self):
        return self.point.month

    @month.setter
    def month(self, new_month):
        self.point = self.point.replace(month=new_month)

    @property
    def day(self):
        return self.point.day

    @day.setter
    def day(self, new_day):
        self.point = self.point.replace(day=new_day)

    @property
    def keywords(self):
        return str(self.keywords_string)

    @keywords.setter
    def keywords(self, kw):
        if(self.keywords_string != ""):
            self.keywords_string += ", "
        self.keywords_string += kw

    def __str__(self):
        return(f"{self.point.date()} | {self.narrative}")

    def __lt__(self, other):
        """custom less than operator for instances of TPoint.  Throws a
        TypeError if the second argument is not a TPoint."""
        if(type(other) != TPoint):
            raise TypeError("Other argument is not an instance of class TPoint.")
        else:
            if(self.point.date() < other.point.date()):
                return True
            elif(self.point.date() > other.point.date()):
                return False
            else:
                if(self.point.time() < other.point.time()):
                    return True
                elif(self.point.time() > other.point.time()):
                    return False
                else:
                    return True

    def to_dict(self):
        d = {
            "__class__": self.__class__.__name__,
            "__module__": self.__module__,
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "narrative": self.narrative,
            "keywords_string": self.keywords_string
        }
        return d

    def as_csv_str(self):
        return(f"{str(self.point.year)},{str(self.point.month)},{str(self.point.day)},{self.narrative}")

# end class TPoint ------------------------------------------------------------
