from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import *

# Create your views here.

class InstructorViews(APIView):
    def get(self, request):
        instructors = Instructor.objects.all()
        serialized = []
        for i in instructors:
            i_data = {}
            i_data["name"] = i.name
            serialized.append(i_data)
        return Response({"instructors": serialized})

class CourseViews(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serialized = [] #what is serialized

        for course in courses:
            json_thingy = dict()
            json_thingy['name'] = course.name
            json_thingy['department'] = course.department
            json_thingy['units'] = course.units
            json_thingy['desc'] = course.desc
            json_thingy['lectures'] = course.lectures
            json_thingy['sections'] = course.sections

            serialized.append(json_thingy)

        return Response({"courses": serialized})

class MeetingViews(APIView):
    def get(self, request):
        meetings = Meeting.objects.all()
        serialized = [] #what is serialized

        for meeting in meetings:
            data = dict()
            data['location'] = meeting.location
            data['building'] = meeting.building
            data['room'] = meeting.room
            data["begin_time"] = meeting.begin_time
            data['end_time'] = meeting.end_time
            data['days'] = meeting.days

            serialized.append(data)


        return Response({"meetings": serialized})


class RoomViews(APIView):
    def get(self, request, targetBuilding, targetRoom):
        meetings = Meeting.objects.all()
        serialized = []

        for meeting in meetings:
            if meeting.building == targetBuilding and meeting.room == targetRoom:
                data = dict()
                data['location'] = meeting.location
                data['building'] = meeting.building
                data['room'] = meeting.room
                data["begin_time"] = meeting.begin_time
                data['end_time'] = meeting.end_time
                data['days'] = meeting.days
                data['courseName'] = meeting.course.name
                data['class_type'] = meeting.meeting_type

                serialized.append(data)

        return Response({"matching courses": serialized})



