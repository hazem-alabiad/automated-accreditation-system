from django import forms

from main.models import *


class instructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['name', 'surname', 'dept_code',]


class departmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['code', 'name',]

class curriculumForm(forms.ModelForm):

    class Meta:
        model = Curriculum
        fields = ['version', 'dept_code',]

class courseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['code', 'name', 'credit']

class courseofferingForm(forms.ModelForm):

    class Meta:
        model = Courseoffering
        fields = ['semester', 'course_code']

class studentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'dep_code']

class semesterForm(forms.ModelForm):

    class Meta:
        model = Semester
        fields = ['type', 'year']