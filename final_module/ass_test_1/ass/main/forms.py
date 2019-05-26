from django import forms

from main.models import *


class create_admin_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class instructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['name', 'surname', 'dept_code',]


class departmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['code', 'name',]

class departmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name',]

class curriculumForm(forms.ModelForm):

    class Meta:
        model = Curriculum
        fields = ['version', 'dept_code',]

class courseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['code', 'name', 'credit']

class courseUpdateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'credit']

class courseofferingForm(forms.ModelForm):

    class Meta:
        model = Courseoffering
        fields = ['semester', 'course_code']

class studentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'dep_code']

class studentUpdateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'surname', 'dep_code']

class semesterForm(forms.ModelForm):

    class Meta:
        model = Semester
        fields = ['type', 'year']

class KeylearningoutcomeForm(forms.ModelForm):

    class Meta:
        model = Keylearningoutcome
        fields = ['dept_code', 'body']

class CourselearningobjectiveForm(forms.ModelForm):

    class Meta:
        model = Courselearningobjective
        fields = ['id', 'course_code', 'body']

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['id', 'courseoffering', 'number']


class QuizForm(forms.ModelForm):

    q_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "dd/mm/yyyy", format:"%m/%d/%Y"}
        )
    )

    class Meta:
        model = Quiz
        fields = ['duration', 'q_date',]

class AssignmentForm(forms.ModelForm):

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "dd/mm/yyyy", format:"%m/%d/%Y"}
        )
    )
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "dd/mm/yyyy", format:"%m/%d/%Y"}
        )
    )
    class Meta:
        model = Assignment
        fields = ['start_date', 'due_date']

class ExaminationForm(forms.ModelForm):

    m_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "dd/mm/yyyy", format:"%m/%d/%Y"}
            )
        )
    class Meta:
            model = Examination
            fields = ['room', 'm_date', 'duration', 'type']

class AssessmentForm(forms.ModelForm):

    class Meta:
        model = Assessment
        fields = ['courseoffering', 'weight',]


class QuestionForm(forms.ModelForm):
    body = forms.CharField(max_length=1000, widget=forms.Textarea(
                                            attrs={'placeholder': 'The question body'}
                                            )
        )

    class Meta:
        model = Question
        fields = ['assessment', 'weight','body',]