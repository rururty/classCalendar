import re

class Course:
    def __init__(self, className, classRoom, faculty, number,
                 name, teacher, str, time, credit, compulsory):
        self.name = name
        self.className = className
        self.teacher = teacher
        self.number = int(number)
        self.classRoom = classRoom
        self.faculty = faculty
        self.lessons = Course.strToLessons(str)
        self.time = time
        self.credit = float(credit)
        self.compulsory = compulsory

    @classmethod
    def strToLessons(cls, str):
        result = re.findall("(\d+)-(\d+)", str)
        result = list(map(int, list(result[0])))
        result1 = re.findall("[单双]+", str)
        result1 = {"单": 2, "双": 2, "单双": 1}[result1[0]]
        result2 = re.findall("星期([一二三四五六日]) [上下晚][午上](\d+(?:,\d+)*)", str)
        changeName = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4,
                      "六": 5, "日": 6}
        result2New = []
        for i in result2:
            new = list(i)
            new[0] = changeName[new[0]]
            new[1] = list(map(int, new[1].split(",")))
            new = tuple(new)
            result2New.append(new)
        weeks = list(range(result[0],result[1]+1,result1))
        return {'weeks':weeks, 'classTime': result2New}