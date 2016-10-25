
from api.models import *
import os 

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

import time
daysOfWeekList = ['U', 'M', 'T', 'W', 'R', 'F', 'S'] #all possible days of week w classes

def convertToMeeting(courseToAdd, meetingObjectList, meetingType):
    # print(meetingObjectList)
    result = []

    #returns a list of all the meeting times for a lecture or a section
    for meetingObject in meetingObjectList:
        # print(meetingObject)
        # print(meetingObject['instructors'])
        meetingInstructors = ':'.join(meetingObject['instructors'])
        meetingInstructors = Instructor(name = meetingInstructors)
        meetingInstructors.save()
        # print(meetingInstructors)


        meetingTimes = meetingObject['times']

        if meetingTimes != None:
            for timeObj in meetingTimes:
                #days of the week the class meets
                # print("timeObjects woo")
                days = ""
                if timeObj['days'] != None:
                    for weekDay in timeObj['days']:
                        days += daysOfWeekList[weekDay]


                    # beginTime = time.strptime(timeObj['begin'], "%I:%M%p")
                    # endTime = time.strptime(timeObj['end'], "%I:%M%p") 
                    beginTime = timeObj['begin']
                    endTime = timeObj['end']

                    location = timeObj['location']
                    building = timeObj['building']
                    room = timeObj['room']

                    myMeeting = Meeting(location = location, building = building, 
                        room = room, begin_time = beginTime, end_time = endTime, 
                        days = days, meeting_type = meetingType, course=courseToAdd)
                    myMeeting.save()

                    result.append(myMeeting)
    return result

    # instructors = models.ManyToManyField(Instructor, related_name="lectures")
    # location = models.CharField(max_length=50, blank=True, default='')
    # building = models.CharField(max_length=50, blank=True, default='')
    # room = models.CharField(max_length=50, blank=True, default='')
    # begin_time = models.TimeField()
    # end_time = models.TimeField()
    # days = models.CharField(max_length=50, blank=True, default='')


def addAPIData():
    print("entering function")
    courseText = readFile("scottyLabsData.txt")
    apiData = eval(courseText) #oops
    print(apiData["semester"])
    allCourses = apiData['courses']
    for courseID in allCourses:


        courseInfo = allCourses[courseID]
        print(courseInfo['name'])
        name = courseInfo['name']
        department = courseInfo['department']
        units = courseInfo['units'] #int
        desc = courseInfo['desc']
        #DO PREREQS AND COREQS LATER WOO

        courseToAdd = Course(course_id = courseID, name = name, department = department, units = units, desc = desc)
        courseToAdd.save()

        lectures = convertToMeeting(courseToAdd, courseInfo['lectures'], 'lecture')
        sections = convertToMeeting(courseToAdd, courseInfo['sections'], 'recitation')



        # yay add a courseModel thing
        # print (name, department, units, desc, lectures, sections)


def makeInstructor():
    print("helpme")
    inst = Instructor(name="Simmons")
    inst.save() 

# makeInstructor()
# addAPIData()