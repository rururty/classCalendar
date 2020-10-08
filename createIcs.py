from icalendar import Calendar, Event
from datetime import datetime, timedelta


def icsCreate(courses, semesterStartDate):
    cal = Calendar()
    cal.add('prodid', '-//rururty//classCalendar//EN')
    cal.add('version', '2.0')
    cal.add('X-WR_TIMEZONE', "Asia/Shanghai")

    for course in courses:
        for week in course.lessons["weeks"]:
            for classTime in course.lessons["classTime"]:
                classTimeDay = classTime[0]
                for classTimeStartNumber in classTime[1]:
                    #创建一个事件，一个课
                    event = Event()
                    lessonStartHour = {
                        '1': 8,
                        '2': 8,
                        '3': 10,
                        '4': 10,
                        '5': 13,
                        '6': 14,
                        '7': 15,
                        '8': 16,
                        '9': 18,
                        '10': 18,
                        '11': 19,
                        '12': 20
                    }
                    lessonStartMinute = {
                        '1': 0,
                        '2': 50,
                        '3': 5,
                        '4': 55,
                        '5': 30,
                        '6': 20,
                        '7': 35,
                        '8': 25,
                        '9': 0,
                        '10': 55,
                        '11': 50,
                        '12': 45
                    }


                    event.add('summary', course.name)
                    lessonStartTime = semesterStartDate \
                            + timedelta(weeks=week-1, days=classTimeDay,
                                        hours=lessonStartHour.get(str(classTimeStartNumber)),
                                        minutes=lessonStartMinute.get(str(classTimeStartNumber)),
                                        seconds=0,
                                        milliseconds=0
                                        )
                    lessonEndTime = lessonStartTime + timedelta(minutes=45)
                    event.add('dtstart', lessonStartTime)
                    event.add('dtend', lessonEndTime)
                    event.add('location', course.classRoom.rstrip())
                    event.add('description', "教师：" + course.teacher.rstrip() +
                              "\n" + \
                              "课程序号：" + str(course.number) + "\n" \
                              + "是否为必修课：" + course.compulsory + "\n" \
                              + "学分为：" + str(course.credit) + "\n" \
                              + "power by: classCalendar author: rururty")
                    cal.add_component(event)
    return cal