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
                classTimeNumber = classTime[1]
                classTimeStartNumber = classTimeNumber[0]
                classTimeEndNumber = classTimeNumber[-1]
                # 创建一个事件，一个课
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
                lessonEndHour = {
                    '1': 8,
                    '2': 9,
                    '3': 10,
                    '4': 11,
                    '5': 14,
                    '6': 15,
                    '7': 16,
                    '8': 17,
                    '9': 18,
                    '10': 19,
                    '11': 20,
                    '12': 21
                }
                lessonEndMinute = {
                    '1': 45,
                    '2': 35,
                    '3': 50,
                    '4': 40,
                    '5': 15,
                    '6': 5,
                    '7': 20,
                    '8': 10,
                    '9': 45,
                    '10': 40,
                    '11': 35,
                    '12': 30
                }
                event.add('summary', course.name + " {}/{}".format(week, course.lessons["weeks"][-1]))
                lessonStartTime = semesterStartDate \
                                  + timedelta(weeks=week - 1, days=classTimeDay,
                                              hours=lessonStartHour.get(str(classTimeStartNumber)),
                                              minutes=lessonStartMinute.get(str(classTimeStartNumber)),
                                              seconds=0,
                                              milliseconds=0
                                              )
                lessonEndTime = lessonStartTime + timedelta(weeks=week - 1, days=classTimeDay,
                                              hours=lessonStartHour.get(str(classTimeEndNumber)),
                                              minutes=lessonStartMinute.get(str(classTimeEndNumber)),
                                              seconds=0,
                                              milliseconds=0
                                              )
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