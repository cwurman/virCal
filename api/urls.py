from django.conf.urls import url
from django.contrib import admin

from api.views import *

urlpatterns = [
    url(r'^instructors', InstructorViews.as_view()),
    url(r'^courses', CourseViews.as_view()),
    url(r'^meetings', MeetingViews.as_view()),
    url(r'^location/(?P<targetBuilding>[A-Za-z0-9-_]+)/(?P<targetRoom>[A-Za-z0-9-_]+)/$', RoomViews.as_view()),
]