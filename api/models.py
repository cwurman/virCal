from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')

class Course(models.Model):
    course_id = models.CharField(max_length=200, blank=True, default='')
    name = models.CharField(max_length=200, blank=True, default='')
    department = models.CharField(max_length=200, blank=True, default='')
    units = models.IntegerField(blank = True, null = True)
    desc = models.TextField(blank=True, null=True)
    prereqs = models.ManyToManyField('Course', related_name="classes_unlocked_prereq")
    coreqs = models.ManyToManyField('Course', related_name="classes_unlocked_coreq")

    def __str__(self):
        return self.name

class Meeting(models.Model):
    # instructors = models.ManyToManyField(Instructor, related_name="lectures")
    location = models.CharField(max_length=200, blank=True, null=True,default='')
    building = models.CharField(max_length=200, blank=True, null=True,default='')
    room = models.CharField(max_length=200, blank=True, null=True,default='')
    begin_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    days = models.CharField(max_length=200, blank=True, null=True, default='')
    meeting_type = models.CharField(max_length=200, default="")
    course = models.ForeignKey(Course, related_name="meetings", blank=True, null=True)

    def __str__(self):
        return self.course.name + "  " + str(self.begin_time)
