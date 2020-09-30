import xlrd
import json
import Date
import re
import json


class Course:
    def __init__(self):
        self.name = ""
        self.className = ""
        self.teacher = ""
        self.number = 0
        self.classRoom = ""
        self.faculty = ""
        self.lesson = []
        self._lessonTime = ""


    @property
    def lessonTime(self):
        return self._lessonTime

    @lessonTime.setter
    def lessonTime(self, str):


data = xlrd.open_workbook("C:\\Users\\guoxiao\\Desktop\\学生选课课表.xlsx")
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
numberOfClass = nrows - 1
course = Course[numberOfClass]
for i in range(numberOfClass):
    information = table.row_values(i + 1)
    course[i].className = information[0]
    course[i].classRoom = information[1]
    course[i].faculty = information[2]
    course[i].number = information[3]
    course[i].name = information[4]
    course[i].teacher = information[5]
    course[i].lessonTime = information[6]

