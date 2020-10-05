import xlrd
import Course
import icalendar import Calendar, Event
from datetime import datetime, timedelta

data = xlrd.open_workbook("C:\\Users\\guoxiao\\Desktop\\学生选课课表.xlsx")
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
numberOfClass = nrows - 1
courses = []
for i in range(numberOfClass):
    information = table.row_values(i + 1)
    courses.append(Course(*information))

for lesson in course:
    for i in range()
    #创建一个事件，一个课
    event = Event()
    #
    event.add('summary', lesson.name)
    lessonStartTime = semesterStartDate \
                      + timedelta(weeks=week-1, )



