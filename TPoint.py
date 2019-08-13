from datetime import datetime


class TPoint:
    def __init__(self, year, month, day, narrative):
        if(type(year) != int):
            year = int(year)
        if(type(month) != int):
            month = int(month)
        if(type(day) != int):
            day = int(day)
        self.point = datetime(year, month, day)
        self.narrative = narrative

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

    def as_csv_str(self):
        return(f"{str(self.point.year)},{str(self.point.month)},{str(self.point.day)},{self.narrative}")

# end class TPoint ------------------------------------------------------------
