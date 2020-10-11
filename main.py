import xlrd
from Course import Course
from createIcs import icsCreate
import os
from datetime import datetime

if __name__ == '__main__':
    data = xlrd.open_workbook("class.xlsx")
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    numberOfClass = nrows
    courses = []
    for i in range(numberOfClass):
        information = table.row_values(i)
        courses.append(Course(*information))
    semesterStartDate = datetime(2020, 9, 14)
    cal = icsCreate(courses, semesterStartDate)
    filename = "classCalendar.ics"
    f = open(os.path.join(filename), 'wb')
    f.write(cal.to_ical())
    f.close()
    print("日历文件已导出到 \"" + os.path.abspath(filename) + "\"。")



